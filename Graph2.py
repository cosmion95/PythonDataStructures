from random import *

class Link:
    def __init__(self, nod, weight):
        self.nod = nod
        self.weight = weight


class Distance:
    def __init__(self, nod, distance):
        self.nod = nod
        self.distance = distance


listaVerificate = []
cale = []
componenteConexe = []


class Graph2:
    def __init__(self, node):
        self.node = node
        self.connections = []
        self.distances = []
        self.next = None

    def addNode(self, newNode):
        # creez noul nod si il adaug in lista de noduri
        newElement = Graph2(newNode)
        if self.next is None:
            self.next = newElement
        else:
            currentElement = self.next
            while currentElement.next is not None:
                currentElement = currentElement.next
            currentElement.next = newElement
        return self

    def addLink(self, nodeA, nodeB, weight=1):
        # adaug legatura in lista de la ambele noduri
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                link = Link(nodeB, weight)
                currentElement.connections.append(link)
            if currentElement.node == nodeB:
                link = Link(nodeA, weight)
                currentElement.connections.append(link)
            currentElement = currentElement.next

    def addDistance(self, nodeA, nodeB, distance):
        # adaug legatura in lista de la ambele noduri
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                dist = Distance(nodeB, distance)
                currentElement.connections.append(dist)
            if currentElement.node == nodeB:
                dist = Distance(nodeA, distance)
                currentElement.connections.append(dist)
            currentElement = currentElement.next

    def delLink(self, nodeA, nodeB):
        # sterg legaturile dintre cele doua noduri
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                # sterg legatura catre nodul b
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i].nod == nodeB:
                        currentElement.connections.pop(i)
                        break
            elif currentElement.node == nodeB:
                # sterg legatura catre nodul a
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i].nod == nodeA:
                        currentElement.connections.pop(i)
                        break
            currentElement = currentElement.next

    def delLinks(self, node):
        # sterge toate legaturile existente catre node
        currentElement = self
        while currentElement is not None:
            if currentElement.node != node:
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i].nod == node:
                        currentElement.connections.pop(i)
                        break
            currentElement = currentElement.next

    def delNode(self, node):
        # sterg nodul si toate legaturile care exista catre el
        currentElement = self
        if currentElement.node == node:
            # e elementul de pe prima pozitie
            # verific daca mai are si alte elemente
            if currentElement.next is not None:
                self = currentElement.next
            else:
                print("Eroare: nu exista alt nod in afara de acesta!", end="")
        else:
            previousElement = currentElement
            while currentElement is not None:
                if currentElement.node == node:
                    # verific daca e nodul care trebuie sters
                    if currentElement.next is not None:
                        previousElement.next = currentElement.next
                    else:
                        # e elementul de pe ultima pozitie
                        previousElement.next = None
                previousElement = currentElement
                currentElement = currentElement.next
        # sterg legaturile pe care le avea nodul
        self.delLinks(node)
        return self

    def printNodesAndConnections(self):
        currentElement = self
        while currentElement is not None:
            print("Nod: " + str(currentElement.node) + " ---> [ ", end=" ")
            for i in range(len(currentElement.connections)):
                # print(str(currentElement.connections[i].nod) + ":" + str(currentElement.connections[i].weight) + " ",
                #       end=" ")
                print(str(currentElement.connections[i].nod) + " ", end=" ")
            print("] ")
            currentElement = currentElement.next

    def checkAdiacenta(self, nodeA, nodeB):
        # verific daca exista legatura de la nodul A la nodul B
        currentElement = self
        while currentElement is not None:
            if currentElement.node == nodeA:
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i] == nodeB:
                        return 1
            if currentElement.node == nodeB:
                for i in range(len(currentElement.connections)):
                    if currentElement.connections[i] == nodeA:
                        return 1
            currentElement = currentElement.next
        return 0

    def getNumberofNodes(self):
        currentElement = self
        counter = 0
        while currentElement is not None:
            counter += 1
            currentElement = currentElement.next
        return counter

    def getNode(self, value):
        currentElement = self
        while currentElement is not None:
            if currentElement.node == value:
                return currentElement
            currentElement = currentElement.next
        return None

    def checkLantRec(self, nodeA, nodeB):
        # adaug nodul in lista de noduri verificate
        listaVerificate.append(nodeA)
        # obtin nodul A
        currentElement = self.getNode(nodeA)
        found = 0
        # verific daca copii lui A au legatura directa cu nodul cautat B
        for i in range(len(currentElement.connections)):
            if found == 0:
                if currentElement.connections[i].nod == nodeB:
                    # am gasit nodul cautat
                    found = 1
                else:
                    if nodVerificat(currentElement.connections[i].nod) is False:
                        found = self.checkLantRec(currentElement.connections[i].nod, nodeB)
        # construiesc calea la intoarcere
        if found == 1:
            cale.append(nodeA)
        return found

    def getLant(self, nodeA, nodeB):
        listaVerificate.clear()
        cale.clear()
        found = self.checkLantRec(nodeA, nodeB)
        if found == 1:
            cale.reverse()
            cale.append(nodeB)
            print("Exista lant.")
            return cale
        print("Nu exista lant intre cele doua noduri.")
        return None

    def checkLant(self, nodeA, nodeB):
        listaVerificate.clear()
        cale.clear()
        found = self.checkLantRec(nodeA, nodeB)
        if found == 1:
            # print("Exista lant")
            return True
        else:
            # print("Nu exista lant intre cele doua noduri")
            return False

    def getComponenteConexe(self):
        componenteConexe.clear()
        # verific daca din primul nod din graf am lant la toate celelalte
        currentELement = self.next
        elementeRamase = []
        componentaCurenta = [self.node]
        # adaug toate elementele catre care nu exista lant intr-o alta lista
        while currentELement is not None:
            if self.checkLant(self.node, currentELement.node) is True:
                # adaug in componenta curenta
                componentaCurenta.append(currentELement.node)
            else:
                # adaug in elementele ramase
                elementeRamase.append(currentELement.node)
            currentELement = currentELement.next
        # adaug componenta conexa in lista si o eliberez
        componenteConexe.append((componentaCurenta[:]))
        componentaCurenta.clear()
        while elementeRamase:
            currentELement = elementeRamase[0]
            componentaCurenta = [currentELement]
            elementeRamase.pop(0)
            # verific catre care alte elemente din lista mai are lant
            total = len(elementeRamase)
            i = 0
            while i < total:
                if self.checkLant(currentELement, elementeRamase[i]):
                    # adaug in componenta curenta si sterg din elementele ramase
                    componentaCurenta.append(elementeRamase[i])
                    elementeRamase.pop(i)
                    total -= 1
                    i -= 1
                i += 1
            # adaug componenta conexa in lista si o eliberez
            componenteConexe.append((componentaCurenta[:]))
            componentaCurenta.clear()
        return componenteConexe

    def verificaConexitate(self):
        comp = self.getComponenteConexe()
        if len(comp) > 1:
            return False
        return True

    def transformInConex(self):
        componenteConexe.clear()
        # obtin lista cu componente conexe si leg care cum apuc
        completConex = self.verificaConexitate()
        while completConex is not True:
            # iau un nod random din prima componenta si il leg de un nod random din alte componente
            nod1 = componenteConexe[0][randrange(len(componenteConexe[0]))]
            comp2 = randrange((len(componenteConexe) - 1)) + 1
            nod2 = componenteConexe[comp2][randrange(len(componenteConexe[comp2]))]
            print("adaug legatura intre " + str(nod1) + " si " + str(nod2))
            self.addLink(nod1, nod2)
            completConex = self.verificaConexitate()
        return self

    def getSubgrafConex(self):

        return None


def nodVerificat(node):
    for i in range(len(listaVerificate)):
        if listaVerificate[i] == node:
            return True
    return False




