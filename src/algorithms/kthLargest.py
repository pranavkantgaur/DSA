# Refer https://gitlab.com/pranav/my-sprints/-/snippets/2221721

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


def removeTopFromHeap(heap):
    '''
    1. compute last child id of current node
    2. if last child is rigjt child:
       2.1. compare parent with max of left and right child:
            2.1.1. if left child is less than right child:
                   2.1.1.1. swap parent with right child
                            parent = right child
                            right child = 2*parent + 2
                            left_child = 2*parent + 1

                   else:
                            swap parent with left child
 
    3. if last child is left child:
       3.1. compare parent with left child:
            3.1.1 if parent is less than left child:
                  swap parent with left child
    4. if no last child:
       break 
    5.  if right_child >= len(heap ) - 1:
        last_child = right_child
        elseif left_child >= len(heap) - 1:
           last_child = left_child
        else:
           break  
    '''
    parent = 0
    
    # remove the leaf which we have just overwritten to the top
    topElement = heap[parent]
    heap[parent] = heap[len(heap)  - 1] # may violate heap property
    heap.pop(-1) 

    left = 1
    right = 2
    if right <= len(heap) - 1:
        last = right
    elif left <= len(heap) - 1:
        last = left
    else:
        return topElement 

    # heapify, since the heap property may have violated
    while(last <= len(heap) - 1):
        if right == last:
            if heap[parent] < max(heap[left], heap[right]):
                if heap[left] < heap[right]:
                    t = heap[parent]
                    heap[parent] = heap[right]
                    heap[right] = t
                    parent = right
                else:
                    t = heap[parent]
                    heap[parent] = heap[left]
                    heap[left] = t
                    parent = left
            else:
                break
        elif left == last:
            if heap[parent] < heap[left]:
                t = heap[parent]
                heap[parent] = heap[left]
                heap[left] = t
            else:
                break    
        else:
            break
        left = 2 * parent + 1
        right = 2 * parent + 2
        if right <= len(heap) - 1:
            last = right
        elif left <= len(heap) - 1:
            last = left
        else:
            break
    return topElement

def partition(arr, l, r):
    '''
    1. select a pivot element
    2. set tail of smaller elements pointed to by j
    3. set head of larger elements pointed to by i
    4. update head of larger elements if current element pointed by j is smaller than pivot
       4.1. increment the tail of smaller eelements
       4.2. increment the gead of larger elements as you have one less now
    5. at the end, swap head of larger elements with pivot, to put pivot at its appropritate place
       (this will put current head of larger elements to the right of pivot and will give appropruitate place
       to the pivot between smaller and larger elements)
    '''
    x = arr[r] # pivot , x = 10, r = 6
    i = l # head of larger elements than pivot, i = 0
    for j in range(i, r): # 0, 5
        if arr[j] < x: # 2 < 10
            #swap(arr[i], arr[j]), 
            if i != j:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
            i+=1
    #swap(arr[i], arr[r])  
    t = arr[i]
    arr[i] = arr[r]
    arr[r] = t
    return i

def getKthLargestQuickSelect(arr, k): # [2, 5, 6, 8, 3, 1, 10], k = 3
    '''
    Runs partition method but on only one partition per level
    if index of pivot after partition is less than k: call parituib in index+1 to r
    ekse call partition to l, index - 1
    '''
    l = 0 
    r = len(arr) - 1 # r = 6
    while(l < r):# 0 < 6
        index = partition(arr, l, r) # arr, 0, 6
        print("The {}th largest element is: {}".format(len(arr) - index, arr[index]))
        if index < len(arr) - k:
            l = index + 1
        elif index > len(arr) - k:
            r = index - 1
        else:
            return arr[index]                    



def getKthLargest(arr, k, method = 'heap'):
    
    if method == 'heap':
        heap = []
        for element in arr:
            heap.append(element)
            bottomUpHeapify(heap)
        assert(len(heap) >= k) 
        print('Heap: ', heap)
        for i in range(k-1):
#        _ = removeTopFromHeap(heap)
            print('Element removed: ', removeTopFromHeap(heap))
            print('Heap: ', heap)

        return removeTopFromHeap(heap)
    
    if method == 'quick-sort':
        return getKthLargestQuickSelect(arr, k)



if __name__  == '__main__':
  arr = [2, 5, 6, 8, 3, 1, 10] # [1, 2, 3, 5, 6, 8, 10]
  k = 2
  print("{}th largest: {}".format(k, getKthLargest(arr, k, 'quick-sort')))
