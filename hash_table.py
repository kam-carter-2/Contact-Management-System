# hash_table.py
# Contact Management System implemented with a custom hash table

# -----------------------------
# Step 1: Contact Class
# -----------------------------
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


# -----------------------------
# Step 2: Node Class (for Separate Chaining)
# -----------------------------
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# -----------------------------
# Step 3: Hash Table Class
# -----------------------------
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        # Simple hash function: sum of character codes % table size
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
            return

        current = self.data[index]
        while current is not None:
            if current.key == key:
                # Update number if name already exists
                current.value.number = number
                return
            if current.next is None:
                break
            current = current.next

        current.next = new_node  # Add to end of linked list

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if not node:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# -----------------------------
# Step 4: Test the Implementation
# -----------------------------
if __name__ == "__main__":
    table = HashTable(10)
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  # May collide with Amy depending on hash
    table.insert("Rebecca", "999-444-9999")  # Updates Rebecca's number

    table.print_table()
    print("\nSearch result:", table.search("John"))
    print("Search result:", table.search("Chris"))
