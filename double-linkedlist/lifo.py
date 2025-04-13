from uuid import uuid4

class Book:
    """
    Represents a book with its associated information.

    Attributes:
        nombre (str): The title of the book.
        descripcion (str): A brief synopsis or description of the book.
        codigo (uuid.UUID): A unique identifier for the book.
        año (int): The publication year of the book.
    """
    def __init__(self, nombre, descripcion, codigo=None, año=0):
        """
        Initialize a new Book instance.

        Args:
            nombre (str): The title of the book.
            descripcion (str): The synopsis or description of the book.
            codigo (uuid.UUID, optional): The unique identifier for the book.
                If not provided, a new UUID is generated.
            año (int, optional): The publication year of the book (default 0).
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.codigo = codigo if codigo is not None else uuid4()
        self.año = año

    def getNombre(self):
        """Return the book's title."""
        return self.nombre
    
    def getDescripcion(self):
        """Return the book's description."""
        return self.descripcion

    def getCodigo(self):
        """Return the book's unique code."""
        return self.codigo

    def getAño(self):
        """Return the publication year of the book."""
        return self.año

    def setNombre(self, nombre):
        """
        Set a new title for the book.
        
        Args:
            nombre (str): The new book title.
        """
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        """
        Set a new description for the book.
        
        Args:
            descripcion (str): The new description.
        """
        self.descripcion = descripcion

    def setCodigo(self, codigo):
        """
        Set a new unique code for the book.
        
        Args:
            codigo (uuid.UUID): The new unique code.
        """
        self.codigo = codigo

    def setAño(self, año):
        """
        Set a new publication year for the book.
        
        Args:
            año (int): The new publication year.
        """
        self.año = año

    def __str__(self):
        """
        Return a string representation of the book.
        
        Returns:
            str: A formatted string containing book details.
        """
        return (f"Nombre: {self.nombre}\n"
                f"Descripcion: {self.descripcion}\n"
                f"Codigo: {self.codigo}\n"
                f"Año: {self.año}\n")

class Node:
    """
    A Node for a singly linked list.

    Attributes:
        value (Book): The data stored in the node (typically a Book instance).
        next (Node): The reference to the next node in the list.
    """
    def __init__(self, value=None):
        """
        Initialize a new Node instance.

        Args:
            value (Book, optional): The data for the node.
        """
        self.value = value
        self.next = None

    def setValue(self, value):
        """
        Update the value stored in the node.
        
        Args:
            value (Book): The new data for the node.
        """
        self.value = value

    def getValue(self):
        """
        Retrieve the value stored in the node.
        
        Returns:
            Book: The data stored in the node.
        """
        return self.value
    
    def getNext(self):
        """
        Retrieve the next node in the list.
        
        Returns:
            Node or None: The next node.
        """
        return self.next

    def setNext(self, next):
        """
        Set the next node reference.

        Args:
            next (Node or None): The next node object or None if end of list.
        
        Raises:
            Exception: If 'next' is not a Node instance or None.
        """
        if not (isinstance(next, Node) or next is None):
            raise Exception("The next attribute must be a Node instance or None.")
        self.next = next

    def __str__(self):
        """
        Return a string representation of the node.
        
        Returns:
            str: A formatted string representing the node.
        """
        return f"{self.value}"

class LinkedListStack:
    """
    Implements an LIFO stack using a singly linked list.

    Attributes:
        top (Node): The top (head) of the stack.
        size (int): The current number of elements in the stack.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.top = None
        self.size = 0

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty; False otherwise.
        """
        return self.top is None

    def push(self, value):
        """
        Insert a new element at the top of the stack.

        Args:
            value (Book): The book instance to be pushed onto the stack.
        """
        new_node = Node(value)
        new_node.setNext(self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        """
        Remove and return the element at the top of the stack.

        Returns:
            Book or None: The book instance if the stack is not empty; otherwise, None.
        """
        if self.isEmpty():
            return None
        popped_node = self.top
        self.top = self.top.getNext()
        self.size -= 1
        return popped_node.getValue()

    def peek(self):
        """
        Retrieve the element at the top of the stack without removing it.

        Returns:
            Book or None: The book instance at the top if the stack is not empty; otherwise, None.
        """
        if self.isEmpty():
            return None
        return self.top.getValue()

    def __len__(self):
        """
        Return the number of elements in the stack.

        Returns:
            int: The size of the stack.
        """
        return self.size

    def __str__(self):
        """
        Return a string representation of the stack.
        The elements are listed from top to bottom.
        
        Returns:
            str: A string representing the stack's contents.
        """
        current = self.top
        elements = ""
        while current:
            elements += str(current.getValue()) + "\n"
            current = current.getNext()
        return elements

def main():
    """
    Demonstrate the usage of the LinkedListStack with Book objects.
    
    Operations performed:
      - Create several Book instances.
      - Push the books onto the stack.
      - Display the book at the top of the stack.
      - Pop one book from the stack.
      - Print the remaining books.
    """
    # Create several Book objects.
    book1 = Book("El Señor de los Anillos", "Una aventura épica en la Tierra Media", año=1954)
    book2 = Book("Orgullo y Prejuicio", "Una historia de amor y sociedad en la Inglaterra del siglo XIX", año=1813)
    book3 = Book("Cien años de soledad", "Una saga familiar en Macondo que abarca generaciones", año=1967)
    book4 = Book("El Principito", "Un relato poético sobre la amistad y la vida", año=1943)
    book5 = Book("1984", "Una novela distópica sobre un futuro controlado por el Gran Hermano", año=1949)

    # Create an empty stack and push the books onto it.
    stack = LinkedListStack()
    stack.push(book1)
    stack.push(book2)
    stack.push(book3)
    stack.push(book4)
    stack.push(book5)

    print("Current Stack (Top to Bottom):")
    print(stack)

    # Peek at the top element
    print("Top element (peek):")
    print(stack.peek())

    # Pop the top element and display it.
    removed_book = stack.pop()
    print("Popped element:")
    print(removed_book)

    print("Stack after popping (Top to Bottom):")
    print(stack)

if __name__ == "__main__":
    main()