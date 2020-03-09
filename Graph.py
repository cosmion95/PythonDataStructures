from Queue import *
from array import *

class Node:
    def __init__(self, varf):
        self.varf = varf
        self.next = None

class Graph:
    def __init__(self, varfuri):
        #nr de varfuri
        self.nrV = varfuri
        #lista cu listele pentru fiecare nod - initial sunt goale(none)
        self.graph = [None] * self.nrV # inmultit cu nr de varfuri pentru a crea nrV liste

    def add_muchie(self, sursa, dest):
        #leg nodul destinatie de nodul sursa
        node = Node(dest)
        node.next = self.graph[sursa]
        self.graph[sursa] = node

        #leg nodul sursa de nodul destinatie
        node = Node(sursa)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_matriceA(self):
        print("Matricea de adiacenta")
        matrice = {}
        for i in range(self.nrV):
            # pentru fiecare element, mai formez o bucla nu nr total de elemente
            # pentru a trece zero-uri in locurile unde nu exista muchie
            for j in range(self.nrV):
                # verific daca elementul exista in lista cu muchii
                temp = self.graph[i]
                found = False
                while temp:
                    if temp.varf == j:
                        found = True
                    temp = temp.next
                if found:
                    matrice[i, j] = 1
                    print("1", end = " ")
                else:
                    matrice[i, j] = 0
                    print("0", end = " ")
            print()
        return matrice

    def printGrad(self, nod):
        counter = 0;
        temp = self.graph[nod]
        while temp:
            counter += 1
            temp = temp.next
        print("Gradul nodului", nod, "este", counter)

    def getGrad(self, nod):
        counter = 0;
        temp = self.graph[nod]
        while temp:
            counter += 1
            temp = temp.next
        return counter

    vizitate = []
    def parcurgereAdancime(self, nod, start = True):
        if start:
            self.vizitate = []
        # verific daca nodul a fost deja vizitat
        for i in range(len(self.vizitate)):
            if self.vizitate[i] == nod:
                #am mai vizitat acest nod
                return
        #marchez nodul ca si vizitat
        self.vizitate.append(nod)
        print(nod, end=" ")
        #aflu muchiile nodului curent
        temp = self.graph[nod]
        while temp:
            self.parcurgereAdancime(temp.varf, False)
            temp = temp.next


    def parcurgereLatime(self, nodStart):
        v = []
        print(nodStart, end=" ")
        v.append(nodStart)
        queue = Queue(nodStart, nodStart)
        while queue:
            # obtin lista cu muchii pentru elementul curent din coada
            muchii = self.graph[queue.value]
            #pentru elementele din lista care nu au fost vizitate, le adaug in coada
            while muchii:
                #verific daca varful a fost deja vizitat
                if muchii.varf not in v:
                    v.append(muchii.varf)
                    print(muchii.varf, end=" ")
                    queue = enqueue(queue, muchii.varf, muchii.varf)
                muchii = muchii.next
            queue = dequeue(queue)


    def isConex(self):
        for i in range(self.nrV):
            #aflu gradul fiecarui nod, daca exista nod cu grad = 0, graful este conex
            grad = self.getGrad(i)
            if grad == 0:
                return False
        return True


    def getComponentConex(self):
        if self.isConex():
            print("Graful este conex.")
            return self.nrV
        else:
            #componentele conexe sunt cele care au grad mai mare decat 0
            counter = 0
            nodCurent = None
            for i in range(self.nrV):
                grad = self.getGrad(i)
                if grad > 0:
                    print("Componenta conexa: ", i)
                    counter = counter + 1
                    nodCurent = i
            print("Graful are ", counter, " componente conexe")
            return nodCurent

    def makeConex(self):
        if self.isConex():
            print("Graful este conex.")
            return
        else:
            #determin nodurile care au grad 0
            componenteConexe = []
            for i in range(self.nrV):
                grad = self.getGrad(i)
                if grad == 0:
                    #acest nod i trebuie legat de un alt nod conex
                    nodConex = self.getComponentConex()
                    self.add_muchie(i, nodConex)


def printMuchii(matrice, length):
    for i in range(length):
        print("Varful", i, "are legatura catre: ")
        for j in range(length):
            if matrice[i, j] == 1:
                print(j, "", end = "")
        print()



