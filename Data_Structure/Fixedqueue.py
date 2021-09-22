from typing import Any

class FixedQueue:

    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass

    def __init__(self, capacity : int) -> None:
        self.no = 0 #Current Number of Data
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None]*capacity
        
    def __len__(self) -> int:
        return self.no #Returns current data number
    
    def is_empty(self) -> bool:
        return self.no <=0

    def is_full(self) ->bool:
        return self.no >= self.capacity
    
    def enque(self, x : Any) ->None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.no+=1
        self.rear +=1
        if self.rear == self.capacity:
            self.rear = 0
        
    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.no -=1
        self.front +=1
        if self.front == self.capacity:
            self.front = 0 
        return x
    
    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def count(self, value : Any) -> bool:
        c = 0 
        for i in range(self.no):
            idx = (i + self.front)%self.capacity
            if self.que[idx] == value:
                c+=1
        return c

    def __contains__(self, value : Any) -> bool:
        return self.count(value)
    
    def clear(self) -> None:
        self.no = self.rear = self.front = 0
    
    def dump(self) -> None:
        if self.is_empty():
            print("큐가 비었습니다.")
        for i in range(self.no):
            idx = (i+self.front)%self.capacity
            print(f'{self.que[idx]}', end = '\n')
