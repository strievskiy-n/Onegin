my_text = open("testtext.txt",'r+')
new_text = my_text.readlines()
my_text.close()

print("Заголовок: ",new_text[0])
previous_endline_idx = 1
chapter = 0

for idx, line in enumerate(new_text):
    if (line == '\n'):
        if (idx - previous_endline_idx) > 2:
            text = ''.join(new_text[previous_endline_idx:idx])
            print("Текст:",text )
        else:
            if 'Глава' in new_text[idx-1] :
                print("Заголовок: ",new_text[idx-1])
            else:
                print("Номер: ",new_text[idx-1])
            # then not text
        previous_endline_idx = idx