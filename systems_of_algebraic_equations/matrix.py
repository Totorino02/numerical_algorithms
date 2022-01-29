import copy

class Matrix():
    def __init__(self, nbRow, nbCol, initialValue = 1):
        self.row = nbRow
        self.col = nbCol
        self.data = [[initialValue for i in range(self.col)] for j in range(self.row)]

        self.isSquared = self.row == self.col
        self.isExtended = False
        self.extendedColA = None
        self.extendedColB = None


    def setDataManually(self):
        """
            set matrix data manually, row by row, column by column.
        """

        n = self.row
        m = self.col
        self.data = []

        print("Enter elements one by one, row by row, confirm each with Return key")
        for i in range(n):
            row = []
            for j in range(m):
                row.append(float(input(f"enter val {i}, {j} : ")))

            self.data.append(row)

    def setDataByArray(self, twoDArray):
        """
            Function to update the matrix data with a given 2D array 
            compare the length of all subarrays of the 2D array to first one_s
            if one is different: stop the process
            if none is different (the loop didn_t break): update matrix dimensions and data
        """

        n = len(twoDArray[0])
        for arr in twoDArray[1:]:
            if len(arr) != n:
                print("The array passed in parameter is not a matrix...")
                break
        else:
            self.row = len(twoDArray)
            self.col = n
            self.data = twoDArray

    def display(self):

        """
            Displays the matrix into a given format whether it is extended or not
        """

        if self.isExtended :
            n = self.row
            m = self.col
            x = self.extendedColA
            y = self.extendedColB

            print("[")
            for i in range(n):
                row = "\t[ "
                for j in range(x):
                    row += f"{round(self.data[i][j], 4):10}"
                row += "  |  "
                for j in range(x, x + y):
                    row += f"{round(self.data[i][j], 4):10}"

                row += " ]"
                print(row)
            print("]")

        else:
            n = self.row
            m = self.col
            print("[")
            for i in range(n):
                row = "\t[ "
                for j in range(m):
                    row += f"{round(self.data[i][j], 4):10}"
                row += " ]"
                print(row)
            print("]")
    
    def extend(self, another_matrix):
        if another_matrix.row != self.row:
            return None
        else: 
            matrix = copy.deepcopy(self)
            n = matrix.row
            m = another_matrix.col
            
            for i in range(n):
                for j in range(m):
                    matrix.data[i].append(another_matrix.data[i][j])
                
            matrix.isExtended = True
            matrix.extendedColA = matrix.col
            matrix.extendedColB = m
            matrix.col += m

            return matrix

    def triangularize(self, upper=True):
        matrix = copy.deepcopy(self)
        n = matrix.row
        m = matrix.col

        if upper:
            rangeI = range(n-1)
            rangeJ = lambda i : range(i+1, n)
        else:
            rangeI = range(n-1, 0, -1)
            rangeJ = lambda i : range(i-1, -1, -1)
            

        for i in rangeI:

            for j in rangeJ(i):
                pivotRow = matrix.data[i]
                pivot = pivotRow[i]

                try:
                    a = matrix.data[j][i] / pivot
                    for k in range(i, m):
                        matrix.data[j][k] = matrix.data[j][k] - a * pivotRow[k]
                except:
                    # TODO handle this case
                    # TODO change lines
                    print("interchangez les lignes et reesayez svp")
                    
        return matrix

    def diagonalize(self):
        matrix = copy.deepcopy(self)
        # applying upper and triangularization to a matrix diagonalize it
        matrix = matrix.triangularize(upper=True).triangularize(upper=False)

        return matrix


""" 
m = Matrix(4, 3)
m.display() """