from __future__ import annotations

from typing import Any
# なんでもデータ入れていいよ

class Node(object):
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    # 全体を管理するイメージ
class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
#図では今３つデータが入っているけど、selfのHEAD以外何もない状態だと考える。
# appendは末尾から入れにいくN
    def append(self, data: Any) -> None:
        #　data: Any はどんなクラスのオブジェクトを入れてもいいですよ。
        
        # 上で作ったNode classにdataを入れる。よってdataとnextというオブジェクトがnew_nodeにできる。
        #new_nodeにNode(data)を入力する。
        new_node = Node(data)
        # ⇓headに何も入っていない時
        if self.head is None:
            self.head = new_node
            return
        # 一回目はdata1, next[]ができてreturn24で終了    
        # ??最後までリンクしても最初のself.headしかないよって意味かな???
        #　2回目はself.headにdata1.next[]があるからif文はskipする。
        last_node =self.head
        # この時点でノードのリストに入ったと言えるの？？？
        # 末尾を探しにいく。
        # whileはtrueの間だけ繰り返す。
        while last_node.next:
            last_node = last_node.next
        #　初回whileはfalseだからskip。    
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.insert("最初")
    l.print()
    l.remove(2)
    print("########")
    l.print()