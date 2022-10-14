import heapq
import sys
import math

class Binaerheap:
    def __init__(self, arr):
        self.heap = arr
        self.comps = 0
        self.swaps = 0
    
    def parentOf(self, i):
        return math.floor((i-1) / 2)
    
    def leftOf(self, i):
        return 2 * i + 1
    
    def rightOf(self, i):
        return 2 * i + 2

    def insert(self, i):
        self.heap.append(i)
        index = len(self.heap) - 1
        while self.heap[self.parentOf(index)] > i and index != 0:
            self.comps += 2
            self.heap[index] = self.heap[self.parentOf(index)]
            self.heap[self.parentOf(index)] = i
            index = self.parentOf(index)

    def removeMin(self):
        x = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.swaps += 1
        
        index = 0
        while self.rightOf(index) < len(self.heap):
            j = self.leftOf(index) if self.heap[self.leftOf(index)] else self.rightOf(index)
            self.comps += 2
            if self.heap[j] <= self.heap[index]:
                self.heap[index], self.heap[j] = self.heap[j], self.heap[index]
                self.comps += 1
                self.swaps += 1
                index = j
            else:
                break
        if self.leftOf(index) < len(self.heap) - 1 and self.heap[self.leftOf(index)] <= self.heap[index]:
            self.heap[index], self.heap[self.leftOf(index)] = self.heap[self.leftOf(index)], self.heap[index]
            self.swaps += 1
            self.comps += 2
        return x


def heapSort(arr): # ikke in-place
    comps = 0
    swaps = 0
    heap = Binaerheap([])
    
    for element in arr:
        heap.insert(element)
    sortertArr = []

    for _ in range(0, len(arr)):
        sortertArr.append(heap.removeMin())
    return [sortertArr, heap.comps, heap.swaps]

def lesInput():
    arr = []
    
    input_fil = open(sys.argv[1], "r") # krever at filnavnet skrives i terminalen ved kjoering av program
    for linje in input_fil:
        arr.append(int(linje))
    input_fil.close()
    
    output_fil = open(sys.argv[1].split("\\")[-1] + "_heap.out", "w")
    for element in heapSort(arr):
        output_fil.write(str(element) + "\n")
    output_fil.close()

if __name__ == "__main__":
    lesInput()