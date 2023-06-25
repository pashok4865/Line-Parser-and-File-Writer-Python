fname= input("Please enter the file number ==> ")
parno= int(input("Please enter the paragraph number ==> "))
lineno= int(input("Please enter the line number ==> "))

def get_line(fname,parno,lineno):
    file_open= open(fname+'.txt', encoding='utf8')
    f=file_open.read()
    paragraph=list(filter(lambda x : x != '', f.split('\n\n')))
    user_paragraph= paragraph[parno-1]
    lines=list(filter(lambda x : x != '', user_paragraph.split('\n')))
    starting_line=lines[lineno-1]
    print(starting_line)
    string_text_file = ''
    end= False
    first_time= True

    return paragraph
        

    for i in paragraph[parno-1:len(paragraph)]:
        lines=list(filter(lambda x : x != '', i.split('\n')))
        if first_time == True:
            for line in lines[lineno-1:len(lines)]:
                string_text_file = string_text_file + line + '\n'
                if 'END/0/0/0' in line:
                    end = True
                    break
            first_time == False
        else:
            for line in lines:
                string_text_file = string_text_file + line + '\n'
                if 'END/0/0/0' in line:
                    end = True
                    break
        if end == True:
            break
        string_text_file = string_text_file + '\n'
        
    return string_text_file


print(get_line(fname,parno,lineno))
