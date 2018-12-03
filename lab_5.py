# Lab 5 option B : Min-Heap
# Name: Jose Lujan
# ID: 80572649
# class: cs2302
# class time 10:30-11:50

class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)

        # TODO: Complete implementation
        self.sort_up(len(self.heap_array) - 1)

    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array[0]

        # TODO: Complete implementation

        # move the last value in the array to the first index
        last_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = last_value

            self.heap_sort_sort_down(0)

        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0

    # Used in the insert function to sort the heap after an element has been inserted
    def sort_up(self, node_index):
        # sort the heap starting from the node that passed into the method and traverse through its parents
        while node_index > 0:
            # get the index of the parent of the node
            parent_index = (node_index - 1) // 2

            # if the value of the parent is larger, make the switch
            if self.heap_array[node_index] < self.heap_array[parent_index]:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp

                node_index = parent_index
            else:
                return

    def heap_sort_sort_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and (i + child_index) < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i += 1

            if min_value == value:
                return

            temp = self.heap_array[node_index]
            self.heap_array[node_index] = self.heap_array[min_index]
            self.heap_array[min_index] = temp

            node_index = min_index
            child_index = 2 * node_index + 1


def create_list_from_file(file):
    file = open(file)
    list = []
    for line in file:
        list_line = line.split(",")
        for num in list_line:
            list.append(int(num))

    return list


def sort_heap(list):
    heap = Heap()
    result = []

    # heapify the list
    for elem in list:
        heap.insert(elem)

    while not heap.is_empty():
        result.append(heap.extract_min())

    return result


def main():
    list = create_list_from_file("Test.txt")

    result = sort_heap(list)

    for i in result:
        print(i)


main()
