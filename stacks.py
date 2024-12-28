class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def reverse_paragraph(paragraph):
    stack = Stack()

    for char in paragraph:
        stack.push(char)

    reversed_paragraph = ""
    while not stack.is_empty():
        reversed_paragraph += stack.pop()

    return reversed_paragraph

def main():
    print("Enter a paragraph to reverse: ")
    user_input = input()

    reversed_paragraph = reverse_paragraph(user_input)

    print("Reversed paragraph:")
    print(reversed_paragraph)

if __name__ == "__main__":
    main()
