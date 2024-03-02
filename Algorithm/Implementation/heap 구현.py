class Heap:
    def __init__(self):
        self.heap = [None]
    
    def push(self, num):
        self.heap.append(num)
        idx = len(self.heap)-1
        while idx>1:
            p_node_idx = idx//2
            if self.heap[idx]<self.heap[p_node_idx]:
                self.heap[idx],self.heap[p_node_idx] = self.heap[p_node_idx],self.heap[idx]
            else:
                return
            idx//=2

    def pop(self):
        if len(self.heap)>1:
            val = self.heap[1] 
            self.heap[1] = self.heap[-1] 
            self.heap.pop()
            idx = 1
            while True:
                l_node_idx = idx*2
                r_node_idx = idx*2+1

                if r_node_idx<=len(self.heap)-1:
                    if self.heap[l_node_idx]<self.heap[r_node_idx]:
                        if self.heap[l_node_idx] < self.heap[idx]:
                            self.heap[l_node_idx], self.heap[idx] = self.heap[idx], self.heap[l_node_idx]
                            idx*=2
                        else:
                            return val
                    else:
                        if self.heap[r_node_idx] < self.heap[idx]:
                            self.heap[r_node_idx], self.heap[idx] = self.heap[idx], self.heap[r_node_idx]
                            idx=idx*2+1
                        else:
                            return val
                elif l_node_idx<=len(self.heap)-1:
                    if self.heap[l_node_idx] < self.heap[idx]:
                            self.heap[l_node_idx], self.heap[idx] = self.heap[idx], self.heap[l_node_idx]
                            idx*=2
                    else:
                            return val
                else:
                    return val
                
h = Heap()
for i in [1,5,7,10,15]:
    h.push(i)

print(h.heap)
print(h.pop())
print(h.heap)
print(h.pop())
print(h.heap)