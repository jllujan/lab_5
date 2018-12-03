from lab_5 import Heap
from lab_5 import heap_sort

# heap to populate
heap = Heap()

# hard coded list of values
list = [7, 4, 8, 10, 4, 6, 9, 5, 6, 3, 5, 11, 7, 8, 2]

# populate the heap
for elem in list:
    heap.insert(elem)

# apply heapsort to the heap and return the sorted array
result = heap_sort(list)

# print the values in the sorted array
for i in result:
    print(i)