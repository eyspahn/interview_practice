class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head):
        self.head = None

    def append(self, new_element):
        """Append new element to end of list."""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if self.head:
            while self.head and counter<position:
                current = current.next
                counter += 1
            return current
        else:
            return None

    def get_position_solution(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None


    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position<1:
            return None
        elif position >1:
            while current and counter < position:
                if counter + 1 == position:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        else: #position == 1
            new_element.next = current.next
            current = new_element

    def insert_solution(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element



    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.next and current.value != value:
            previous = current
            current = current.next
        # current.value == value
        if current.value == value:
            if previous:
                 previous.next = current.next
            else: # previous is None
                self.head = current.next


    def delete_solution(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
