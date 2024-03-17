class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse_list(self):
    cur = self.head.next
    self.head.next = self.head
    temp_1 = self.head.next
    self.head.next = None
    while cur.next:
      temp_2 = cur.next 
      cur.next = temp_1
      temp_1 = cur
      cur = temp_2

    cur.next = temp_1
    self.head = cur


# SORTING

  def merge_sort(self, head):
    if head is None or head.next is None:
      return head

    # Find the middle of the linked list
    middle = self.find_middle(head)

    # Split the linked list into two halves
    second_half = middle.next
    middle.next = None

    # Recursively sort each half
    sorted_first_half = self.merge_sort(head)
    sorted_second_half = self.merge_sort(second_half)

    # Merge the sorted halves
    return self.merge(sorted_first_half, sorted_second_half)

  def find_middle(self, head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

  def merge(self, l1, l2):
    dummy = Node()
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next

  def sort(self):
    self.head = self.merge_sort(self.head)




      


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Друк зв'язного списку
print("Реверсуємо список:")
llist.reverse_list()

llist.print_list()

llist.sort()

print("Linked list after merge sort:")
llist.print_list()