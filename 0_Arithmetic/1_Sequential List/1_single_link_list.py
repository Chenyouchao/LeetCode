class Node(object):
    
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLindList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self): 
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self): 
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        return ''

    def add(self, item): 
        '''链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item): 
        '''链表尾部添加元素'''
        node = Node(item)
        
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            # cur移到None就回不去了
            while cur.next != None:
                cur = cur.next
            cur.next = node
        
    def insert(self, pos, item): 
        '''指定位置添加元素
        :param pos 从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0 
            while count < pos-1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
        
    def remove(self, item): 
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return True
            pre = cur
            cur = cur.next
        return False

    def search(self, item): 
        '''
        查找节点是否存在
        return 第一个元素位置
        '''
        cur  = self.__head
        count = 0
        while cur != None:
            if cur.elem == item:
                return count
            cur = cur.next
            count += 1
        return -1


if __name__ == "__main__":

    ll = SingleLindList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    print("remove", ll.remove(2))
    print(ll.is_empty())
    print(ll.length())
    print(ll.travel())
    print(ll.search(10))