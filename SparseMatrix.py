class SparseMatrix:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.next = None

    def add(self, row, column, value):
        # creez noul obiect cu cheia si valoarea
        newElement = SparseMatrix(row, column, value)
        if self.next is None:
            self.next = newElement
        else:
            currentElement = self.next
            while currentElement.next is not None:
                currentElement = currentElement.next
            currentElement.next = newElement
        return self

    def delete(self, row, column):
        if self.row == row and self.column == column:
            self = self.next
        else:
            currentElement = self
            while currentElement.next is not None:
                previousElement = currentElement
                currentElement = currentElement.next
                if currentElement.row == row and currentElement.column == column:
                    if currentElement.next is None:
                        # e elementul de pe ultima pozitie
                        previousElement.next = None
                    else:
                        previousElement.next = currentElement.next
        return self

    def print(self):
        currentElement = self
        while currentElement is not None:
            print(str(currentElement.row) + " | " + str(currentElement.column) + "  --  " + str(currentElement.value))
            currentElement = currentElement.next

    def getValue(self, row, column):
        currentElement = self;
        while currentElement is not None:
            if currentElement.row == row and currentElement.column == column:
                return currentElement.value
            currentElement = currentElement.next
        return 0

    def getRows(self):
        #intoarce numarul de randuri
        maxRow = 0
        currentElement = self
        while currentElement is not None:
            if currentElement.row > maxRow:
                maxRow = currentElement.row
            currentElement = currentElement.next
        return maxRow

    def getColumns(self):
        #intoarce numarul de coloane
        maxCol = 0
        currentElement = self
        while currentElement is not None:
            if currentElement.column > maxCol:
                maxCol = currentElement.column
            currentElement = currentElement.next
        return maxCol

    def printAsMatrix(self):
        currentElement = self
        maxRow = self.getRows()
        maxCol = self.getColumns()
        for i in range(1, maxRow+1):
            for j in range(1, maxCol+1):
                value = self.getValue(i, j)
                print(str(value), end = " ")
            print("")

def addTwoMatrixes(matA, matB):
    #verific daca au acelasi numar de randuri si coloane
    if matA.getRows() != matB.getRows() or matA.getColumns() != matB.getColumns():
        print("Nu au acelasi numar de randuri si coloane")
    else:
        matResult = None
        for row in range(1, matA.getRows()+1):
            for col in range(1, matA.getColumns()+1):
                resultValue = matA.getValue(row, col) + matB.getValue(row, col)
                if resultValue != 0:
                    if matResult is None:
                        matResult = SparseMatrix(row, col, resultValue)
                    else:
                        matResult.add(row, col, resultValue)
        return matResult



