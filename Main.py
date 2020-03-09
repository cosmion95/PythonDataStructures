from BinaryTree import *
from Queue import *
from Stack import *
from LSI import *
from Graph import *
from SparseMatrix import *
from OrientedGraph import *

# r = BinaryTree(5, "A")
# addToTree(r, 3, "B")
# addToTree(r, 2, "C")
# addToTree(r, 10, "D")
# addToTree(r, 9, "E")
# addToTree(r, 6, "F")
# addToTree(r, 7, "G")
# addToTree(r, 15, "G")
# addToTree(r, 13, "G")
# addToTree(r, 14, "G")
#
# deleteFromTreeKey(r, 10)
#
# travelInOrder(r)

#travelInOrder(r)
# print("cu coada")
# displayTreeWithQueue(r)
#
# print("-------------")
# print("cu stiva")
# displayTreeWithStack(r)

# q = Queue(1, "A")
# q = enqueue(q, 2, "B")
# q = enqueue(q, 3, "C")
#
# afisareCoada(q)
#
# q = dequeue(q)
#
# afisareCoada(q)

#s = Stack(1, "A")
# s = stackPush(s, 2, "B")
# s = stackPush(s, 3, "C")

#afisareStack(s)

# s = stackPop(s)
#
# afisareStack(s)


# l = LSI(1, "A")
# l = addToLSI(l, 2, "B")
# l = addToLSI(l, 3, "C")
# l = addToLSI(l, 4, "D")
#
# deleteFromLSI(l, 3)
#
# printLSI(l)

# graph = Graph(5)
# graph.add_muchie(0, 1)
# graph.add_muchie(0, 3)
# graph.add_muchie(1, 2)
# graph.add_muchie(1, 3)
#
# matrice = graph.print_matriceA()
#
# printMuchii(matrice, graph.nrV)
#
# graph.printGrad(2)

# print("Parcurgere in latime: ", end=" ")
# graph.parcurgereLatime(0)
# print()
#
# print("Parcurgere in adancime: ", end=" ")
# graph.parcurgereAdancime(0)
# print()
#
# conex = graph.isConex()
# print("Graf conex: ", conex)
#
# print("Transform in graf conex")
# graph.makeConex()
#
# matrice = graph.print_matriceA()

# matriceRara = SparseMatrix(2, 1, 1);
# matriceRara.add(2,3,1)
# matriceRara.add(3,1,1)
# matriceRara.add(4,3,5)
# matriceRara.add(3,4,7)
#
# #matriceRara.print()
# matriceRara.printAsMatrix()


# matA = SparseMatrix(2, 1, 1);
# matA.add(2,3,1)
# matA.add(3,1,1)
# #matA.add(4,1,1)
#
# matB = SparseMatrix(2, 1, 1);
# matB.add(2,3,1)
# matB.add(3,1,1)
#
# matC = addTwoMatrixes(matA, matB)
# matC.printAsMatrix()og = OrientedGraph(1)
# og.addNode(2)
# og.addNode(3)
# og.addNode(4)
# og.addNode(5)
# og.addNode(6)
# #
# og.addLink(1, 2)
# og.addLink(1, 3)
#
# og.addLink(2, 1)
# og.addLink(2, 3)
#
# og.addLink(3, 1)
# og.addLink(3, 2)
#
# #x = checkTareConex(og)
#
# drum = matriceDrum(og)
#
# for i in range(len(drum)):
#     for j in range(len(drum)):
#         print(str(drum[i][j]) + " ", end=" ")
#     print(" ")
#
#
# og.printNodesAndConnections()
#
# bla = checkDrum(og, 5, 1)
# print(bla)
#
# og1 = createOGfromMatrix()
# og1.printNodesAndConnections()


# og = OrientedGraph(1)
# og.addNode(2)
# og.addNode(3)
# # og.addNode(4)
# # og.addNode(5)
# # og.addNode(6)
# #
# og.addLink(1, 2)
# og.addLink(1, 3)
#
# og.addLink(2, 1)
# og.addLink(2, 3)
#
# og.addLink(3, 1)
# og.addLink(3, 2)
#
# #og.delNode(2)
#
# og.printNodesAndConnections()
#
# #x = checkTareConex(og)
#
# drum = matriceDrum(og)
#
# for i in range(len(drum)):
#     for j in range(len(drum)):
#         print(str(drum[i][j]) + " ", end=" ")
#     print(" ")
#
#
# og.printNodesAndConnections()
#
# bla = checkDrum(og, 5, 1)
# print(bla)
#
# og1 = createOGfromMatrix()
# og1.printNodesAndConnections()






