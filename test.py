class Heap_Item:
    """
    Heap item.
    """

    def __init__(self, k, v):
        """
        Generates a heap item with key k and value v.
        """
        self.key = k
        self.value = v


    def __repr__(self):
        """
        Represents a heap item.
        """
        return "({},{})".format(self.key, self.value)



class Min_Heap:
    """
    Min-Heap.
    """

    def __init__(self, L=None):
        """
        Generates a min-heap containing the pairs (key, value) 
        in L.
        """
        self.heap = [] if L == None else [Heap_Item(k,v) for (k,v) in L]
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.min_heapify(i)


    def left(self, i):
        """
        Returns the i-th item's left child index.
        """
        return 2*i+1


    def right(self, i):
        """
        Returns the i-th item's right child index.
        """
        return 2*(i+1)


    def parent(self, i):
        """
        Returns the i-th item's parent index.
        """
        return (i-1)//2


    def min(self):
        """
        Returns the pair (key, value) containing the smallest
        key in the heap.
        """
        return self.heap[0] if self else None


    def min_heapify(self, i):
        """
        Restores the min-heap property on the i-th item assuming
        that its left and right sub-heaps are correct min-heaps.
        """
        l = self.left(i)
        r = self.right(i)
        min = i

        if l < len(self) and self.heap[l].key < self.heap[min].key:
            min = l

        if r < len(self) and self.heap[r].key < self.heap[min].key:
            min = r

        if min != i:
            self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
            self.min_heapify(min)


    def extract_min(self):
        """
        Extracts the pair (key, value) containing the smallest key
        from the heap.
        """
        if not self:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min = self.heap.pop().value
        self.min_heapify(0)
        return min


    def sort(self):
        """
        Returns a list of values sorted in non-decreasing
        order by key.
        """
        heap = self.heap[:]
        sorted_pairs = [self.extract_min() for _ in range(len(self))]
        self.heap = heap
        return sorted_pairs


    def insert(self, k, v):
        """
        Inserts the pair (k, v) into the heap.
        """
        self.heap.append(Heap_Item(k,v))
        self.decrease_key(len(self)-1,k)


    def increase_key(self, i, k):
        """
        Increases the i-th item's key to k.
        """
        # NOTE: assumes a valid index i
        # NOTE: assumes heap[i].key <= k

        self.heap[i].key = k
        self.min_heapify(i)


    def decrease_key(self, i, k):
        """
        Decreases the i-th item's key to k.
        """
        # NOTE: assumes a valid index i
        # NOTE: assumes heap[i] >= k

        self.heap[i].key = k
        item = self.heap[i]
        p = self.parent(i)

        while i > 0 and k < self.heap[p].key:
            self.heap[i] = self.heap[p]
            i = p
            p = self.parent(i)

        self.heap[i] = item


    def update_key(self, i, k):
        """
        Sets the i-th item's key to k.
        """
        if self.heap[i].key < k:
            self.increase_key(i, k)
        elif self.heap[i].key > k:
            self.decrease_key(i, k)


    def __len__(self):
        """
        Returns the number of items in the heap.
        """
        return len(self.heap)


    def __bool__(self):
        """
        Returns True if the heap is not empty, and False otherwise.
        """
        return len(self.heap) > 0


    def _str(self, i):
        """
        Computes the representation of the i-th item's sub-heap.
        """
        if not self.heap:
            return [], 0, 0

        label = str(self.heap[i])
        l = self.left(i)
        r = self.right(i)
        p = self.parent(i)

        left_lines, left_pos, left_width = ([], 0, 0) if l >= len(self.heap) else self._str(l)
        right_lines, right_pos, right_width = ([], 0, 0) if r >= len(self.heap) else self._str(r)

        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos

        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)

        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)

        if (middle - len(label)) % 2 == 1 \
            and p >= 0 \
            and i == self.left(p) \
            and len(label) < middle:
                label += '.'

        label = label.center(middle, '.')

        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '

        lines =  [' '*left_pos + label + ' '*(right_width - right_pos),
                  ' '*left_pos + '/' + ' '*(middle-2) +
                  '\\' + ' '*(right_width - right_pos)]

        lines += [left_line + ' '*(width - left_width - right_width) + right_line
                         for left_line, right_line in zip(left_lines, right_lines)]

        return lines, pos, width


    def __repr__(self):
        """
        Represents the heap.
        """
        return '\n'.join(self._str(0)[0])+"\n"

hp= Min_Heap()
hp.insert(8,2)
hp.insert(29,12)