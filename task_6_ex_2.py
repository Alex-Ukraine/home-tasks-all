from typing import Any


class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


class CustomList:
    def __init__(self, *data, node=None):
        self.__head = None
        for a in data[::-1]:
            print('appended: ', a)
            node = Item(a)
            node.next = self.__head
            self.__head = node
        self.cursor = node

    def append(self, value) -> None:
        node = Item(value)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def add_start(self, value) -> None:
        node = Item(value)
        node.next = self.__head
        self.__head = node

    def remove(self, value):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.value == value:
                if pre is None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        else:
            raise ValueError

    def clear(self) -> None:
        self.__head = None

    def __getitem__(self, index) -> Any:
        cur = self.__head
        idx = 0
        while cur is not None:

            if idx == index:
                return cur.value
            else:
                cur = cur.next
                idx += 1
        raise IndexError

    def __setitem__(self, index, data) -> None:
        cur = self.__head
        idx = 0
        while cur is not None:
            print(cur.value)
            if idx == index:
                cur.value = data
                break
            else:
                cur = cur.next
                idx += 1
        else:
            raise IndexError

    def __delitem__(self, index) -> None:
        cur = self.__head
        pre = None
        idx = 0
        while cur is not None:
            if idx == index:
                if pre is None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
                idx += 1
        else:
            raise IndexError

    def find(self, value) -> Any:
        cur = self.__head
        index = 0
        while cur is not None:

            if cur.value == value:
                return index
            else:
                cur = cur.next
                index += 1
        raise Exception

    def __len__(self) -> int:
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def __next__(self):
        cur = self.cursor
        if cur is not None:
            rt = cur.value
            self.cursor = cur.next
            return rt
        else:
            raise StopIteration

    def __iter__(self):
        self.cursor = self.__head
        return self

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.value)
            cur = cur.next
