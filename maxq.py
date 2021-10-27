heap_size = 0
tree_array_size = 20
INF = 1000

# function to get right child of a node of a tree
def get_right_child(A, index):
  if((((2*index)+1) < len(A)) and (index >= 1)):
    return (2*index)+1
  return -1

# function to get left child of a node of a tree
def get_left_child(A, index):
    if(((2*index) < len(A)) and (index >= 1)):
        return 2*index
    return -1

# function to get the parent of a node of a tree
def get_parent(A, index):
  if ((index > 1) and (index < len(A))):
    return index//2
  return -1

def max_heapify(A, index):
  left_child_index = get_left_child(A, index)
  right_child_index = get_right_child(A, index)

  # finding largest among index, left child and right child
  largest = index

  if ((left_child_index <= heap_size) and (left_child_index>0)):
    if (A[left_child_index] > A[largest]):
      largest = left_child_index

  if ((right_child_index <= heap_size and (right_child_index>0))):
    if (A[right_child_index] > A[largest]):
      largest = right_child_index

  # largest is not the node, node is not a heap
  if (largest != index):
    A[index], A[largest] = A[largest], A[index]
    max_heapify(A, largest)

def build_max_heap(A):
  for i in range(heap_size//2, 0, -1):
    max_heapify(A, i)

def maximum(A):
  return A[1]

def extract_max(A):
  global heap_size
  max = A[1]
  A[1] = A[heap_size]#replace with last 
  heap_size = heap_size-1
  max_heapify(A, 1)
  return max

def increase_key(A, index, key):
  A[index] = key
  while((index>1) and (A[get_parent(A, index)] < A[index])):#compares with parent
    A[index], A[get_parent(A, index)] = A[get_parent(A, index)], A[index]
    index = get_parent(A, index)
    

def decrease_key(A, index, key):
  A[index] = key
  max_heapify(A, index)

def insert(A , key):
  global heap_size
  heap_size = heap_size+1
  A[heap_size] = -1*INF
  increase_key(A, heap_size, key)

if __name__ == '__main__':
  A = [None]*tree_array_size

  insert(A, 20)
  insert(A, 15)
  insert(A, 40)
  
  insert(A, 10)
  insert(A, 5)
  insert(A, 7)
  insert(A, 12)
  insert(A, 2)
  insert(A, 9)
  insert(A, 1)
  insert(A, 39)

  print(A[1:heap_size+1])

  increase_key(A, 6, 22)
  print(A[1:heap_size+1])

  decrease_key(A,1,3)
  print(A[1:heap_size+1])

  print(maximum(A))
  print(extract_max(A))

  print(A[1:heap_size+1])

  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))
  print(extract_max(A))

