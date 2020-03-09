class Queue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.root = self
        self.next = None

    # def isNotEmpty(self):
    #     if self.root is None:
    #         return False
    #     else:
    #         return True

def isEmpty(root):
    if root.root is None:
        return False
    else:
        return True


    def getNextElement(self):
        if self.root is not None:
            return self.value
        else:
            return None


def enqueue(root, key, value):
    newElement = Queue(key, value)
    if root.root is None:
        root.root = newElement
    else:
        currentElement = root.root
        while currentElement.next is not None:
            currentElement = currentElement.next
        currentElement.next = newElement
    return root

def dequeue(root):
    if root.root is not None:
        #schimb radacina
        root.root = root.next
        return root.next
    else:
        print("Nu-i nimeni la coada")


def afisareCoada(coada):
    if coada.root is not None:
        currentElement = coada.root
        print("-----------Primul element----------")
        while currentElement is not None:
            print("                 " + currentElement.value)
            currentElement = currentElement.next
        print("-----------Ultimul element----------")
    else:
        print("Coada este goala")