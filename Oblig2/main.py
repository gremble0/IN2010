from gnome import gnomeSort
from insertion import insertionSort
from quick import quickSort
from heap import heapSort
import time
import sys
import math

def lesInput():
    arr = []
    
    input_fil = open(sys.argv[1], "r") # krever at filnavnet skrives i terminalen ved kjoering av program
    for linje in input_fil:
        arr.append(int(linje))
    input_fil.close()
    
    output_fil = open(sys.argv[1].split("\\")[-1] + "_results.csv", "w")    
    
    output_fil.write("n, insert_cmp, insert_swaps, insert time,quick_cmp, quick_swaps, quick_time,gnome_cmp, gnome_swaps, gnome_time,heap_cmp, heap_swaps, heap_time \n")

    for x in range (0, len(arr)):
        # print(arr[x:], arr[:x], math.floor(len(arr) - 1))
        insertionTime = time.time_ns()
        insertionSorted = insertionSort(arr[:x])
        insertionTime = (time.time_ns() - insertionTime) / 1000
        output_fil.write(str(x) + ", " + str(insertionSorted[1]) + ", " + str(insertionSorted[2]) + ", " + str(insertionTime))

        gnomeTime = time.time_ns()
        gnomeSorted = gnomeSort(arr[:x])
        gnomeTime = (time.time_ns() - gnomeTime) / 1000
        output_fil.write(str(gnomeSorted[1]) + ", " + str(gnomeSorted[2]) + ", " + str(gnomeTime))

        quickTime = time.time_ns()
        quickSorted = quickSort(arr[:x], 0, math.floor(len(arr[:x]) - 1), 0, 0)
        quickTime = (time.time_ns() - quickTime) / 1000
        output_fil.write(str(quickSorted[1]) + ", " + str(quickSorted[2]) + ", " + str(quickTime))
        
        heapTime = time.time_ns()
        heapSorted = heapSort(arr[:x])
        heapTime = (time.time_ns() - heapTime) / 1000
        output_fil.write(str(heapSorted[1]) + ", " + str(heapSorted[2]) + ", " + str(heapTime) + "\n")

    output_fil.close()

if __name__ == "__main__":
    lesInput()