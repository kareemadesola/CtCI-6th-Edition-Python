from linked_list import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head
    # current = current.next

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def example():
    ll = LinkedList.generate(4, 0, 125)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
