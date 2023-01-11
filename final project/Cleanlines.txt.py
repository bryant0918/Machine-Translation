def clean_lines(file):
    """Go by line to hopefully not completely delete lines"""
    #Read in the text
    with open(file, 'r', encoding = 'utf-8') as myfile:
        lines = myfile.readlines()
        
    with open("hyphen.txt", 'r', encoding = 'utf-8') as data:
        characters = data.read()
        hyphen1 = characters[0]
        hyphen2 = characters[1]
        others = characters[2:]
        
    with open("nonbreakingspace.txt", 'r', encoding = 'utf-8') as data:
        nbs = data.read()
        
        cleaned = []
        print(len(lines))
        for text in lines:
            #Get rid of HTML characters
            newtext = html.unescape(text)
            text = html.unescape(newtext)
            
            """Using Regex"""
            #For weird % issues
            text = re.sub(r"(%\S\s|\s%\s|%.*%|%\S)", "", text)
            
            #Get rid of dumb Hyphens and make them dashes
            text = text.replace(hyphen1, "-")
            text = text.replace(hyphen2, "-")
            
            #For random characters I don't want anywhere
            text = text.replace(others,"")
            #text = text.replace(nbs," ")
            
            #For weird characters at the beginning of the line
            rando = re.compile(r"(^[,#)*-.\s\\\/]\s?)", re.MULTILINE)
            text = rando.sub(r"", text)
            beg = re.compile(r"^\W+",re.MULTILINE)
            text = beg.sub(r"",text)
            numbers = re.compile(r"^[\d\s]*")
            text = numbers.sub(r"", text)
            
            #Get rid of all nonword characters at the end of the line
            end = re.compile(r"\W+$", re.MULTILINE)
            text = end.sub(r"",text)
            numbers = re.compile(r"[\s\d\W]*$")
            text = numbers.sub(r"", text)
            
            #All extra space at the beginning and end of the line
            space = re.compile(r"^\s+", re.MULTILINE)
            space2 = re.compile(r"\s+$", re.MULTILINE)
            text = space.sub(r"", text)
            text = space2.sub(r"", text)
            
            #Ignore Case
            text = text.casefold()
            
            cleaned.append(text+"\n")
            
            
        print(len(cleaned))
        
        
    with open(file+"clean.txt",'w', encoding = 'utf-8') as myfile:
        myfile.writelines(cleaned)