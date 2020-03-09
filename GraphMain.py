from Graph2 import *
from Drawing import *

drawCircle()


graph = Graph2(1)
graph.addNode(2)
graph.addNode(3)
graph.addNode(4)
graph.addNode(5)
graph.addNode(6)
graph.addNode(7)
graph.addNode(8)
graph.addNode(9)
graph.addNode(10)

graph.addLink(1, 2)
graph.addLink(2, 3)
graph.addLink(2, 6)
graph.addLink(3, 6)

graph.addLink(7, 8)
graph.addLink(8, 9)

graph.addLink(4, 5)

# cale = graph.getLant(1, 6)

lista = graph.getComponenteConexe()
graph.transformInConex()

print("----------------------------------------")

print(lista)

graph.printNodesAndConnections()

turtle.mainloop()