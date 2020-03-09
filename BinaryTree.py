from Queue import *
from Stack import *

class BinaryTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def addToTree(root, key, value):
    #creez un obiect cu key = value
    newNode = BinaryTree(key, value)
    #daca radacina e null, incep arborele
    if root is None:
        root = newNode
    else:
        #caut nodul unde trebuie adaugat
        if root.key == key:
            print("Cheia deja exista in arbore")
        elif key < root.key:
            #daca e mai mic si nu are copil stang, il adaug, altfel traversez arborele catre stanga
            if root.left is None:
                root.left = newNode
                root.left.parent = root
            else:
                addToTree(root.left, key, value)
        elif key > root.key:
            #daca e mai mare si nu are copil drept, il adaug sau traversez arborele catre dreapta
            if root.right is None:
               root.right = newNode
               root.right.parent = root
            else:
                addToTree(root.right, key, value)

def deleteFromTreeKey(root, key):
    if root is None:
        return root
    else:
        if key < root.key:
            print("caut in copilul stang")
            deleteFromTreeKey(root.left, key)
        elif key > root.key:
            print("caut in copilul drept")
            deleteFromTreeKey(root.right, key)
        elif key == root.key:
            print("am gasit nodul")
            #verific tipul nodului: 1 copil sau frunza
            if root.left is None or root.right is None:
                return deleteSonOrFrunza(root)
            #daca am ajuns aici, nodul are 2 copii
            #nodul sters il inlocuiesc cu cel mai mic copil din subarborele drept
            temp = root.right;
            while(temp.left is not None):
                temp = temp.left
            #modific cheia nodului care trebuie sa il sterg
            root.key = temp.key
            #sterg nodul gasit cel mai mic in subarborele drept
            root.right = deleteFromTreeKey(root.right, temp.key)
        else:
            print("nu am gasit nodul cu cheia " + str(key))
        return root

def deleteSonOrFrunza(root):
    if root.left is None and root.right is not None:
        print("nodul are 1 copil")
        temp = root.right
        root.right.parent = root.parent
    elif root.right is None and root.left is not None:
        print("nodul are 1 copil")
        temp = root.left
        root.left.parent = root.parent
    else:
        print("nodul este frunza, nu are copii")
        temp = None
    # verific daca e copilul e in stanga sau drepta parintelui
    if root.parent.left.key == root.key:
        print("copilul e in stanga parintelui")
        root.parent.left = temp
    else:
        print("copilul e in dreapta parintelui")
        root.parent.right = temp
    return temp

def searchByKey(root, key):
    if root is None:
        print("Nu am gasit elementul cu cheia " + str(key))
    else:
        if key > root.key:
            #merg in dreapta
            searchByKey(root.right, key)
        elif key < root.key:
            #merg in stanga
            searchByKey(root.left, key)
        elif key == root.key:
            print("Elementul cu cheia " + str(key) + " are valoarea " + root.value)

def searchByValue(root, value):
    #caut in toate elementele arborelui pentru valoarea potrivita
    if root is None:
        return;
    if root.value == value:
        print("Elementul cu valoarea: " + value + " are cheia " + str(root.key));
        return;
    else:
        searchByValue(root.left, value)
        searchByValue(root.right, value)


def travelInOrder(root):
    if root:
        travelInOrder(root.left)
        print(str(root.key) + " --- " + root.value + " /// parinte: " + ifNullKey(root.parent) + " // copil direct stang: " + ifNullKey(root.left) + " // copil direct drept: " + ifNullKey(root.right))
        travelInOrder(root.right)

def travelPostOrder(root):
    if root:
        travelPostOrder(root.left)
        travelPostOrder(root.right)
        print(root.key)

def travelPreOrder(root):
    if root:
        print(root.key)
        travelPreOrder(root.left)
        travelPreOrder(root.right)

def ifNullKey(var):
    try:
        return str(var.key)
    except:
        return "None"

def displayTreeWithQueue(root):
    currentElement = root
    #adaug element in coada
    queue = Queue(root, currentElement.value)
    while currentElement is not None:
        #printez element
        print(str(queue.root.key.key))
        # scot element din coada
        queue = dequeue(queue)
        # adaug copiii elementului in coada
        if currentElement.left is not None:
            queue = enqueue(queue, currentElement.left, currentElement.left.value)
        if currentElement.right is not None:
            queue = enqueue(queue, currentElement.right, currentElement.right.value)
        if queue.root is not None:
            currentElement = queue.root.key
        else:
            currentElement = None


def displayTreeWithStack(root):
    currentElement = root;
    stack = Stack(currentElement, currentElement.value)
    while currentElement is not None:
        #printez elementul curent
        print(str(stack.top.key.key))
        stack = stackPop(stack)
        if currentElement.left is not None:
            stack = stackPush(stack, currentElement.left, currentElement.left.value)
        if currentElement.right is not None:
            stack = stackPush(stack, currentElement.right, currentElement.right.value)
        if stack.top is not None:
            currentElement = stack.top.key
        else:
            currentElement = None
