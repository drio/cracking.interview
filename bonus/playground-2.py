import random

# matrix[row][col]
#
def set_to_zero(m):
    if not m:
        return

    n_rows, n_cols = len(m), len(m[0])

    zero_rows, zero_cols = [], []
    for r in range(0, n_rows):
        for c in range(0, n_cols):
            if m[r][c] == 0:
                zero_rows.append(r)
                zero_cols.append(c)

    for r in zero_rows:
        for c in range(0, n_cols):
            m[r][c] = 0

    for c in zero_cols:
        for r in range(0, n_rows):
            m[r][c] = 0


def bsearch(i_list, p_start, p_end, target):
    if p_start > p_end:
        return None

    p_middle = p_start + ((p_end - p_start) / 2)

    if i_list[p_middle] == target:
        return p_middle

    if target < i_list[p_middle]:
        return bsearch(i_list, p_start, p_middle-1, target)
    else:
        return bsearch(i_list, p_middle+1, p_end, target)

def qsort(i_list, p_start, p_end):
    if p_end <= p_start:
        return

    p_curr = p_start + 1
    p_change = p_curr
    while p_curr <= p_end:
        if i_list[p_curr] < i_list[p_start]:
            i_list[p_change], i_list[p_curr] = i_list[p_curr], i_list[p_change]
            p_change += 1
        p_curr += 1
    i_list[p_change-1], i_list[p_start] = i_list[p_start], i_list[p_change-1]

    qsort(i_list, p_start, p_change-2)
    qsort(i_list, p_change, p_end)

class tNode(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def bst_insert(root, d):
    if not root:
        return tNode(d)

    p_current, p_parent = root, None
    while p_current:
        p_parent = p_current
        if p_current.data > d:
            p_current = p_current.right
        else:
            p_current = p_current.left

    if p_parent.data > d:
        p_parent.right = tNode(d)
    else:
        p_parent.left = tNode(d)

    return root

def bst_lookup(root, d):
    if not root:
        return None

    if root.data == d:
        return root

    if d > root.data:
        return bst_lookup(root.left, d)
    else:
        return bst_lookup(root.right, d)

def bst_core_walk_bfs(l, stack):
    if not stack:
        return

    new_stack = []
    while stack:
        n = stack.pop()
        if n:
            l.append(n.data)
            new_stack.insert(0, n.right)
            new_stack.insert(0, n.left)

    bst_core_walk_bfs(l, new_stack)

def bst_walk_bfs(root):
    if not root:
        return
    l = []
    bst_core_walk_bfs(l, [root])
    return l


def int_to_string(i_int):
    o_list = []

    if i_int == 0:
        return '0'

    is_neg = False
    if i_int < 0:
        is_neg = True
        i_int *= -1

    while i_int:
        d = i_int % 10
        d_string = chr(d + ord('0'))
        o_list.insert(0, d_string)
        i_int /= 10

    if is_neg:
        o_list.insert(0, '-')

    return ''.join(o_list)

def string_to_int(i_string):
    i_list = list(i_string)

    is_neg = False
    if i_list[0] == '-':
        is_neg = True
        del i_list[0]

    p_ten = 1
    output = 0
    for c in i_list[::-1]:
        d = (ord(c) - ord('0')) * p_ten
        print c, d
        output += d
        p_ten *= 10

    # add sign if necessary ..
    if is_neg:
        output *= -1

    return output


def merge(i_list, a_start, a_end, b_start, b_end):
    o_list = []
    pa, pb = a_start, b_start

    while pa <= a_end and pb <= b_end:
        if i_list[pa] <= i_list[pb]:
            o_list.append(i_list[pa])
            pa += 1
        else:
            o_list.append(i_list[pb])
            pb += 1

    while pa <= a_end:
        o_list.append(i_list[pa])
        pa += 1

    while pb <= b_end:
        o_list.append(i_list[pb])
        pb += 1

    for idx, e in enumerate(o_list):
        i_list[a_start + idx] = e


def merge_sort(i_list, p_start, p_end):
    if (p_end - p_start) < 1:
        return

    off = (p_end - p_start) / 2
    merge_sort(i_list, p_start, p_start + off)
    merge_sort(i_list, p_start + off + 1, p_end)
    merge(i_list, p_start, p_start + off, p_start + off + 1, p_end)

def replace(i_string, rep_chr, new_str):
    o_list = []
    for c in i_string:
        if c == rep_chr:
            for nc in new_str:
                o_list.append(nc)
        else:
            o_list.append(c)
    return ''.join(o_list)

class Node(object):
    def __init__(self, d):
        self.data = d
        self.next = None

class Iter(object):
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def next(self):
        r = self.current
        if self.current:
            self.current = self.current.next
        return r

def add(head, new_node):
    if not head:
        return new_node

    new_node.next = head
    return new_node

def addEnd(head, new_node):
    if not head:
        return None

    cn = head
    while cn.next:
        cn = cn.next

    cn.next = new_node

    return head

def delete(head, d):
    if not head:
        return None, None

    if head.data == d:
        return True, head.next

    prev, curr = None, head
    found = None
    while curr:
        if curr.data == d:
            found = d
            prev.next = curr.next

        prev = curr
        curr = curr.next

    return found, head

def dump(head):
    l = []
    cn = head
    while cn:
        l.append(cn.data)
        cn = cn.next
    return l


def random_list(n=10, min=-1000, max=1000):
    l = []
    for i in range(0, n):
        l.append(random.randint(min, max))
    return l

# main
#
def test_sort(func):
    for i in range(1,100):
        l = random_list(random.randint(10, 99), 100, 0, 999)
        il = l[0:]
        sl = sorted(l)
        func(l, 0, len(l)-1)
        assert(sl == l)

def test_replace():
    assert(replace('Foo Bar', ' ', 'X') == 'FooXBar')
    assert(replace('Foo  Bar', ' ', 'X') == 'FooXXBar')
    assert(replace(' Bar', ' ', 'X') == 'XBar')
    assert(replace('Foo Bar', ' ', 'XXX') == 'FooXXXBar')
    assert(replace('Bar  ', ' ', 'XY') == 'BarXYXY')

def test_list():
    head = Node(1)
    assert(head.data == 1)

    head = addEnd(head, Node(2))
    assert(dump(head) == [1, 2])

    head = addEnd(head, Node(3))
    assert(dump(head) == [1, 2, 3])

    found, head = delete(head, 2)
    assert(found)
    assert(dump(head) == [1, 3])

    found, head = delete(head, 1)
    assert(found)
    assert(dump(head) == [3])

    found, head = delete(head, 3)
    assert(found)
    assert(dump(head) == [])

    head = Node(1)
    head = add(head, Node(2))
    head = add(head, Node(3))
    assert(dump(head) == [3, 2, 1])

    found, head = delete(head, 1)
    assert(dump(head) == [3, 2])

    head = Node(1)
    head = add(head, Node(2))
    head = add(head, Node(3))
    head = add(head, Node(4))

    t = range(1,5)
    t.reverse()
    for n in Iter(head):
        if not n:
            break
        assert(n.data == t[0])
        del t[0]

def test_bst():
    r = None
    r = bst_insert(r, 50)

    r = bst_insert(r, 25)
    r = bst_insert(r, 75)

    r = bst_insert(r, 10)
    r = bst_insert(r, 35)
    r = bst_insert(r, 55)
    r = bst_insert(r, 90)

    assert(bst_walk_bfs(r) == [50, 25, 75, 10, 35, 55, 90])

def test_bsearch():
    # num of elements in: list_size, min, max
    for i in range(0, 1000):
        size = random.randint(1, 1000)
        l = sorted(random_list(size, -999, 999))

        for idx, v in enumerate(l):
            idx_bs = bsearch(l, 0, len(l), v)
            try:
                assert(l[idx_bs] == v)
            except:
                print l, v, "|", idx, idx_bs
                assert(l[idx_bs] == v)

        idx_bs = bsearch(l, 0, len(l), -123123)
        assert(None == idx_bs)

def test_set_to_zero():
    m = [ [1,2,3], [4,0,6], [7,8,9] ]
    set_to_zero(m)
    assert(m[0][1] == 0)
    assert(m[1][1] == 0)
    assert(m[2][1] == 0)

    assert(m[1][0] == 0)
    assert(m[1][1] == 0)
    assert(m[1][2] == 0)

    assert(m[0][0] != 0)
    assert(m[0][2] != 0)


#test_bst()
# test_sort(qsort)
#test_bsearch()
test_set_to_zero()
