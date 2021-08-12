import heapq 
from collections import Counter  
from collections import namedtuple

class Node(namedtuple("Node", ["left", "right"])): 
    def itr(self, binc, rep):
        self.left.itr(binc, rep + "0")  
        self.right.itr(binc, rep + "1") 

class Leaf(namedtuple("Leaf", ["char"])):  
    def itr(self, binc, rep):
        binc[self.char] = rep or "0"
        
def hufCode(s):  
    tmp = []  
    for ch, frq in Counter(s).items(): 
        tmp.append((frq, len(tmp), Leaf(ch)))
        heapq.heapify(tmp) 
    cnt = len(tmp) 
    while len(tmp) > 1:  
        frq1, _cnt1, left = heapq.heappop(tmp)  
        frq2, _cnt2, right = heapq.heappop(tmp) 
        heapq.heappush(tmp, (frq1 + frq2, cnt, Node(left, right)))                                                                      # потомки left и right соответственно
        cnt += 1  
    binCode = {}  
    if tmp:  
        [(_frq, _count, root)] = tmp 
        root.itr(binCode, "")  
    return binCode  


a = input()  
b = hufCode(a)
print(b)
encd = " ".join(b[i] for i in a)
print(f'Число символов: {len(b)}, длина закодированной строки: {len(encd)}')                   
for i in b: 
    print(f"Символ {i} и его код: {b[i]}")  
print(f'Закодированная строка: {encd}') 

    
