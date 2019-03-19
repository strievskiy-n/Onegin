from SearchEngine import SearchEngine, load
from Bundles import Bundle

def parseOnegin(filename):
    my_text = open(filename,'r+')
    new_text = my_text.readlines()
    my_text.close()

    #print("Заголовок: ",new_text[0])
    previous_endline_idx = 1
    chapter = 0

    result = []

    header = None

    for idx, line in enumerate(new_text):        
        if (line == '\n'):
            if 'Глава' in new_text[idx-1] :
                if 'повес' in new_text[idx-1] :
                    pass
                if 'халдейских' in new_text[idx-1] :  
                    pass
                else:     
                    chapter+=1 
            if (idx - previous_endline_idx) > 2:
                text = ''.join(new_text[previous_endline_idx:idx])
                #print("Текст:",text )
                result.append( (header, text) )
            else:
                if 'Глава' in new_text[idx-1] :
                    #print("Заголовок: Глава ",chapter," Цитата")    
                    header = "Глава " + str(chapter) +" Цитата"
                else:
                    #print("Заголовок: Глава ",chapter," Номер: ",new_text[idx-1]) 
                    header = "Глава "+ str(chapter) + " " + new_text[idx-1]  
            previous_endline_idx = idx

    return result

pairs = parseOnegin("Евгений Онегин.txt")

se = SearchEngine()

i = 0
for p in pairs:    
    bundle = Bundle((i, p[0].strip()))
    bundle.data.append(p[1].strip())
    se.loadData(bundle)
    i+=1
    

r = se.search("Онегин Ольга")



se.save('index/index')





