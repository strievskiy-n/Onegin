from bottle import route, run, debug, static_file, request, template
from SearchEngine import SearchEngine, load

engine = load('index/index')

debug(mode=True)

'''@route('/Hello/<name>')
def index(name):
    return 'Hello ' + name'''

@route('/')
def main():
    f = open('Newsite.html')
    s = f.read()
    f.close()   

    return s

@route('/css/<filename:path>')
def send_static(filename): 
    return static_file(filename, root='css') 

@route('/img/<filename:path>')
def send_static(filename): 
    return static_file(filename, root='img')

@route('/search') 
def search():
    query = request.query.s
    result = engine.search(query)

    data = list(result)

    #print(data[:10])

    def sortByNumber(pair):
        return pair[1][0]
    
    data.sort(key=sortByNumber)

    return template("results", data=data, query=query)    


run(host='localhost', port=8085)
'''def index(name):
    return 'Hello ' + name

print(index("Иван"))''' 
