class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data: int):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, next_node: Node, data: int):
        if self.head == next_node:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = None
        new_node = self.head
        while new_node != next_node:
            prev_node = new_node
            new_node = new_node.next
        self.insert_after(prev_node, data)

    def delete_node(self, data: int):
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_node(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("\n")

    def reverse(self):
        prev_node = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def sort(self):
        if self.head is None:
            return
        sorted_list = None
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_list = self.sorted_insert(sorted_list, cur)
            cur = next_node
        self.head = sorted_list

    def sorted_insert(self, sorted_list: Node, new_node: Node) -> Node:
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node
        else:
            cur = sorted_list
            while cur.next is not None and cur.next.data < new_node.data:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
            return sorted_list

    def merge_sorted_lists(self, list1, list2):
        if list1.head is None:
            return list2.head
        if list2.head is None:
            return list1.head
        merged_list = LinkedList()
        cur1 = list1.head
        cur2 = list2.head
        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged_list.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                merged_list.insert_at_end(cur2.data)
                cur2 = cur2.next
        while cur1:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        while cur2:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next
        return merged_list


if __name__ == "__main__":

    list_1 = LinkedList()
    list_1.insert_at_begin(5)
    list_1.insert_at_begin(10)
    list_1.insert_at_begin(15)
    list_1.insert_at_end(20)
    list_1.insert_at_end(25)
    list_1.delete_node(10)
    node = list_1.search_node(20)
    list_1.insert_after(node, 7)
    list_1.insert_before(node, 4)
    print("List 1:")
    list_1.print()

    list_1.reverse()
    print("Reversed list 1:")
    list_1.print()

    list_1.sort()
    print("Sorted list 1:")
    list_1.print()

    list_2 = LinkedList()
    list_2.insert_at_begin(3)
    list_2.insert_at_begin(8)
    list_2.insert_at_begin(12)
    list_2.insert_at_begin(2)
    list_2.insert_at_begin(9)
    list_2.sort()
    print("Sorted list 2:")
    list_2.print()

    merged = list_1.merge_sorted_lists(list_1, list_2)
    print("Merged list:")
    merged.print()
