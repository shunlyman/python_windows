import hashlib



class HashTable(object):

    def  __init__(self,size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
    def hash(self, key) -> int:


if __name__ == '__main__':
    hash_table = HashTable()
    print(hash_table.table)
