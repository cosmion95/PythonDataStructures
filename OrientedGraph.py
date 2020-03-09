class OrientedGraph:
    def __init__(self, node):
        self.node = node
        self.connections = []
        self.next = None

    def addNode(self, newNode):
        # creez noul nod si il adaug in lista de noduri
        newElement = OrientedGraph(newNode)
        if self.next is None:
            self.next = newElement
        else:
            currentElement = self.next
            while currentElement.next is not None:
                currentElement = currentElement.next
            currentElement.next = newElement
        return self

    def addLink(self, nodeA, nodeB):
        # in lista cu legaturi a nodului A, adaug nodul B
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                currentElement.connections.append(nodeB)
            currentElement = currentElement.next

    def delNode(self, node):
        # sterg nodul si toate legaturile care exista catre el
        currentElement = self
        while currentElement is not None:
            if currentElement.node == node:
                # verific daca e nodul care trebuie sters
                if currentElement.next is not None:
                    # e elementul de pe ultima pozitie
                    previousElement.next = None
                else:
                    previousElement.next = currentElement.next
            else:
                # verific daca contine legaturi catre nodul care trebuie sters
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i] == node:
                        currentElement.connections.remove(node)
            previousElement = currentElement
            currentElement = currentElement.next
        return self

    def delLink(self, nodeA, nodeB):
        # sterg legatura pe care o are nodul A catre nodul B
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i] == nodeB:
                        currentElement.connections.remove(nodeB)
            currentElement = currentElement.next
        return self

    def length(self):
        # intoarce numarul de noduri din graf
        counter = 0
        currentElement = self
        while currentElement is not None:
            counter = counter + 1
            currentElement = currentElement.next
        return counter

    def printNodesAndConnections(self):
        currentElement = self
        while currentElement is not None:
            print("Nod: " + str(currentElement.node) + " ---> [ ", end=" ")
            for i in range(len(currentElement.connections)):
                print(str(currentElement.connections[i]) + " ", end=" ")
            print("] ")
            currentElement = currentElement.next

    def checkAdiacenta(self, nodeA, nodeB):
        # verific daca exista legatura de la nodul A la nodul B
        # print("verific" + str(nodeA) + " cu " + str(nodeB))
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i] == nodeB:
                        return 1
            currentElement = currentElement.next
        return 0


def createOGfromMatrix():
    nodeNumber = int(input('Numarul de noduri: '))
    graph = None
    for i in range(1, nodeNumber + 1):
        # creez nodul
        if graph is None:
            graph = OrientedGraph(i)
        else:
            graph.addNode(i)
        for j in range(1, nodeNumber + 1):
            # aflu legatura nodului i cu celelalte noduri j
            if i != j:
                link = int(input(str(i) + " -- " + str(j) + ": "))
                if link == 1:
                    # adaug legatura de la nodul i catre nodul j
                    graph.addLink(i, j)
    return graph


drumGasit = []


def checkDrumRec(og, nodeA, nodeB):
    # verific daca am legatura directa intre ele
    if og.checkAdiacenta(nodeA, nodeB) == 1:
        drumGasit.append(nodeB)
        drumGasit.append(nodeA)
        return 1
    # merg pe nodul curent pentru a ajunge la lista lui
    currentElement = og
    myElem = None
    while currentElement is not None:
        if currentElement.node == nodeA:
            myElem = currentElement
        currentElement = currentElement.next
    # adaug intr-o lista toate legaturile de la nodul A
    nodeList = []
    for i in range(len(myElem.connections)):
        nodeList.append(myElem.connections[i])
    # parcurg lista noua creata si sterg fiecare element dupa verificare
    for i in range(len(nodeList)):
        check = checkDrumRec(og, nodeList[i], nodeB)
        if check == 1:
            drumGasit.append(nodeA)
            return 1
        # nodeList.remove(nodeList[i])
        # i = i-1
    return 0


def checkDrum(og, nodeA, nodeB):
    # apelata din main, apeleaza functia recursiva
    x = checkDrumRec(og, nodeA, nodeB)
    drumGasit.reverse()
    if x == 0:
        print("Nu am gasit drum")
    else:
        print("Exista drum")
    return drumGasit


listaVerificate = [[]]


def checkTareConex(og):
    counter = og.length()
    for i in range(1, counter + 1):
        for j in range(1, counter + 1):
            if i == j:
                continue
            # verific daca combinatia a fost deja verificata

            # adaug combinatia in lista de verificate
            listaVerificate.append([i, j])
            # verific daca exista drum intre ele
            check = checkDrumRec(og, i, j)
            if check == 0:
                # daca cel putin 1 nu exista, graful nu e tare conex
                print("Graful nu e tare conex")
                return 0
    print("Graful este tare conex")
    return 1


def matriceAdiacenta(og):
    # construieste matricea de adiacenta
    adi = [[0 for x in range(og.length())] for y in range(og.length())]
    for i in range(0, og.length()):
        for j in range(0, og.length()):
            if i == j:
                adi[i][j] = 0
            else:
                adi[i][j] = og.checkAdiacenta(i + 1, j + 1)
    return adi


def matriceDrum(og):
    a = matriceAdiacenta(og)
    for k in range(1, og.length()):
        for j in range(1, og.length()):
            for i in range(1, og.length()):
                if i != j and a[i][j] == 0 and a[i][k] == 1 and a[k][j] == 1:
                    a[i][j] = 1
    return a
