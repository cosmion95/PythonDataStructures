class Stack:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.top = self
        self.previous = None

def stackPush(stack, key, value):
    newElement = Stack(key, value)
    if stack.top is None:
        stack.top = newElement
    else:
        currentTop = stack.top
        newElement.previous = currentTop
        stack.top = newElement
    return stack

def stackPop(stack):
    if stack.top is None:
        print("Stiva nu contine niciun element")
    else:
        #print("Elimin elementul " + stack.top.value)
        stack.top = stack.top.previous
    return stack

def afisareStack(stack):
    if stack.top is not None:
        currentElement = stack.top
        print("-------------TOP-------------")
        while currentElement is not None:
            print("              " + currentElement.value)
            currentElement = currentElement.previous
        print("------------BOTTOM-------------")
    else:
        print("Nu exista elemente in stiva")
