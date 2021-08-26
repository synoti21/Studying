from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:

    def __init__(self, key: Any, value: Any, next: Node) -> None:

        self.key = key
        self.value = value
        self.next = next

class ChainedHash: #initiating the Hash table (or, hash array)
    
    def __init__(self, capacity: int)->None:
        self.capacity = capacity
        self.table = [None]*self.capacity

    def hash_value(self, key:Any)->int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)
    

    def search(self, key:Any) -> Any:
        hash = self.hash_value(key) #getting the hash value of key
        p = self.table[hash] #p is the pointer that searches the certain hash the key genuinely has

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next #go to next linked node
        return None

    def add(self, key:Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None: #this while statement checks if the same key exists
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash]) #First, make the 'New Node, and the empty table(=self.table[hash]) moves to the New Node's 'next'
        self.table[hash] = temp #makes the existing hash table point the New Node(=temp)
        return True

        """For example, let's say we want to add 46 at table[7], and 20 already exists.
            Consider line 46. Table[7] would be pointing the 20. Now consider line 47.
            We're making the new node that holds the value of 46, that has the "self.table[hash]" as the 'next',
            and that existing "self.table[hash]"is pointing the temp, which is 20. That means the new node will point the 20 from the moment it borns.
            So, at line 47, we update the table[7](self.table[hash]) to point the new node (46).

            ==> temp2 = Node(key, value, temp)
                table = temp2

            ==> temp.next =/= table[hash] ==> temp.self(temp).table[hash] =/= self(table[hash]).table[hash]"""

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None: #if there's only one element at following hash
                    self.table[hash] = p.next
                else:
                    pp.next = p.next #switches the node's next (pp points) to the other node's next (p points)
                return True
            pp=p
            p=p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key}({p.value})', end ='')
                p = p.next
            print()


    

    
