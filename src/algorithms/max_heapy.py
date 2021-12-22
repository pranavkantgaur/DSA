'''
input: [2, 5, 3, 9, 7, 1, 0, 4]
o/p: [9, 7, 3, 4, 5, 1, 0, 2]
'''
heap = []     

def bottomUpHeapify(heap):
    child_index = len(heap) - 1 
    parent_index = (child_index  - 1) // 2
    while(parent_index >= 0):
        if heap[parent_index] < heap[child_index]:
            t = heap[parent_index]
            heap[parent_index] = heap[child_index]
            heap[child_index] = t
            child_index = parent_index
            parent_index = (child_index - 1) // 2
        else:
            break
   
def buildHeap(arr):
    for element in arr:
        heap.append(element)
        bottomUpHeapify(heap)
    



if __name__ == '__main__':
    #arr = [2, 5, 3, 9, 7, 1, 0, 4]
    arr = [20, 22, 17, 19, 10, 12, 15, 7, 9, 18, 25]
    buildHeap(arr)
    print("Heap: ", heap)
