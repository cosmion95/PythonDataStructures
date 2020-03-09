class LSI:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.root = self
        self.next = None

def addToLSI(root, key, value):
    #creez noul obiect cu cheia si valoarea
    newElement = LSI(key, value)
    if root.root is None:
        root.root = newElement
    else:
        currentElement = root.root
        while currentElement.next is not None:
            currentElement = currentElement.next
        currentElement.next = newElement
    return root

def deleteFromLSI(root, key):
    if root.key == key:
        #cheia reprezinta radacina listei
        if root.next is not None:
            root = root.next
        else:
            root = None
        return
    elif root.next.key == key:
        #sunt pe elementul situat inaintea elementului cu cheia cautata
        if root.next.next is not None:
            #elementul cautat nu e ultimul, are un elment dupa el
            root.next = root.next.next
        else:
            root.next = None
        return
    deleteFromLSI(root.next, key)

def printLSI(root):
    currentElement = root
    while currentElement is not None:
        print(str(currentElement.key) + " ------ " + currentElement.value)
        currentElement = currentElement.next