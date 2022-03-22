import hashlib

class HashTable(object):

    def  __init__(self,size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size
        # hexdigest 文字列にする。
    
    def add(self, key, value) -> None:
        # index番号を取得
        index = self.hash(key)
        for data in self.table[index]:
        # dataの0番目はkey,型のことかな？？？
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    #printを見やすくする
    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')

                

            print()


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('car', 'Tesla')
    hash_table.add('car', 'Toyota')
    hash_table.add('pc', 'Mac')
    hash_table.add('SNS', 'Youtube')
    hash_table.print()
    # print(hash_table.table)
    # print(hash_table.hash("car"))
