class Person():
    def __init__(self, name):
        self.myname = name
    def hello(self):
        print("Hello! I am {}.".format(self.myname))
#これがインスタンス化
Peter = Person('peter')
#Peterインスタンスのhelloメソッド
Peter.hello()
Mary = Person('Mary')
Mary.hello()


