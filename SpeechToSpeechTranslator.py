# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:03:27 2022

@author: Bryant McArthur
"""

import azure.cognitiveservices.speech as speechsdk
import requests
import uuid
import json


"""This will work fine if you call it from main
    Or you may adjust the TTS function call to change the language and speaker
    94d4c73e70fa4ae1821d98160e5b6009
    a5d1179eb1c14961b6ba8fdff1c25470
    105fcd7d-0707-4e33-9dc2-f0b055fce39f
"""


def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="94d4c73e70fa4ae1821d98160e5b6009", region="westus")
    
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    
    return result.text



#text = from_mic()


def MT(text, source = 'en', target = 'pl'):
    # Add your subscription key and endpoint
    subscription_key = "a5d1179eb1c14961b6ba8fdff1c25470"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    
    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "westus2"
    
    path = '/translate'
    constructed_url = endpoint + path
    
    params = {
        'api-version': '3.0',
        'from': source,
        'to': target
    }
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    # You can pass more than one object in body.
    body = [{
        'text': text
    }]
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    
    response = request.json()
    response = response[0]
    translation = response['translations']
    translation = translation[0]
    
    text = translation['text']
    
    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    
    return text


#text = MT(text)

def TTS(text, outfile, langcode = 'pl-PL', langname = 'pl-PL-MarekNeural'):
    """Parameters:
        text string to synthesize to speech
        outfile to store the audio file
        langcode defaulted to Polish
        Langname defaulted to Polish speaking Marek    
    """
    
    speech_config = speechsdk.SpeechConfig(subscription="94d4c73e70fa4ae1821d98160e5b6009", region="westus")
    
    # Note: if only language is set, the default voice of that language is chosen.
    speech_config.speech_synthesis_language = langcode # For example, "de-DE"
    # The voice setting will overwrite the language setting.
    # The voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = langname
    
    audio_config = speechsdk.audio.AudioOutputConfig(filename=outfile)
    
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)
    
    
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text)
    
    return


#TTS(text, "Taylor.wav", 'fil-PH', 'fil-PH-AngeloNeural')


if __name__ == "__main__":
    
    text = from_mic()
    text = MT(text)
    TTS(text, "translations.wav", 'pl-PL-MarekNeural')
        
    pass


