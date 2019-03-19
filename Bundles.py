class Bundle:
    def __init__(self, header):
        self.header = header
        self.data = list()


class FileBundle(Bundle):
    def __init__(self, header, path):
        super(FileBundle, self).__init__(header)

        with open(path, 'r') as f:
            self.data = f.read().split('\n')


class DiaryBundle(Bundle):
    def __init__(self, header, diary):
        super(DiaryBundle, self).__init__(header)

        for i in diary:
            self.data.append(str(i))