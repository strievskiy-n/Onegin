from Bundles import Bundle
import re
import pymorphy2
import shelve

class SearchEngine:

    morph = pymorphy2.MorphAnalyzer()

    def __init__(self):
        self.sources = {}

    def loadData(self, source):
        if not isinstance(source, Bundle):
            raise AttributeError("Invalid Argument")
        
        for p in source.data:
            words = p.split(' ')

            for w in words:
                w = w.lower()
                reg = re.compile('[^а-я]')
                w = reg.sub('', w)
                forms = []

                if w == '':
                   continue

                for i in self.morph.parse(w):
                    forms.append(i.normal_form)

                for word in forms:
                    try:
                        self.sources[word].add((p, source.header))
                    except KeyError:
                        self.sources[word] = set()
                        self.sources[word].add((p, source.header))

    def search(self, query):
        query = query.lower()
        words = query.split(' ')

        result = set()
        forms = []

        for w in words:
            for i in self.morph.parse(w):
                forms.append(i.normal_form)

        for word in forms:

            if len(result) == 0:
                result = self.sources.get(word, set())
            else:
                result = result.intersection(self.sources.get(word, set()))
                
                if len(result) == 0:
                    return result

        return result

    def save(self, filename):
        with shelve.open(filename) as f:
            f['0'] = self


def load(filename):
    with shelve.open(filename) as f:
        return f['0']
        
