



class HashTable(object):

    def  __init__(self,size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]


if __name__ == '__main__':
