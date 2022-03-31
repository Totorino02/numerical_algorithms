import copy

class Matrix():
    def __init__(self, nb_row, nb_col, initial_value = 1):
        self.row = nb_row
        self.col = nb_col
        self.data = [[initial_value for i in range(self.col)] for j in range(self.row)]

        self.is_extended = False
        self.extended_col_A = None
        self.extended_col_B = None


    def is_squared(self):
        return self.row == self.col

    def is_col_matrix(self):
        return self.col == 1

    def is_row_matrix(self):
        return self.row == 1

    def is_symetric(self):
        condition = [self.data[i][j] == self.data[j][i] for i in range(self.row) for j in range(self.col)]
        return all(condition)

    def is_tridiagonal(self):
        for i in range(self.row):
            for j in range(self.col):
                cell = self.data[i][j]
                if i == j or i == j-1 or i == j+1:
                    if cell == 0:
                        return False
                else:
                    if cell != 0:
                        return False
        return True


    def set_data(self, array=None):
        """
            set matrix data :
                manually, row by row, column by column.
                or with a given 2D array 
        """

        if array:
            """
                compare the length of all subarrays of the 2D array to first one_s
                if one is different: stop the process
                if none is different (the loop didn_t break): update matrix dimensions and data
            """
            try :
                n = len(array[0])
                for arr in array[1:]:
                    if len(arr) != n:
                        print("The array passed in parameter is not a matrix...")
                        break
                else:
                    self.row = len(array)
                    self.col = n
                    self.data = array
            except :
                print("There is some issues with the array passed in parameter")

        else:
            n = self.row
            m = self.col
            self.data = []

            print("Enter elements one by one, row by row, confirm each with Return key")
            for i in range(n):
                row = []
                for j in range(m):
                    row.append(float(input(f"enter val {i}, {j} : ")))

                self.data.append(row)


    def display(self):

        """
            Displays the matrix into a given format whether it is extended or not
        """

        if self.is_extended :
            n = self.row
            m = self.col
            x = self.extended_col_A
            y = self.extended_col_B

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

    def none_matrix(self):
        n = self.row
        m = self.col
        matrix = Matrix(n, m)
        matrix.set_data([[None for i in range(m)] for j in range(n)])
        return matrix

    def multiply(self, another_matrix):
        if self.col == another_matrix.row:
            a = self
            b = another_matrix
            matrix = Matrix(a.row, b.col)
            for i in range(a.row):
                for j in range(b.col):
                    matrix.data[i][j] = sum([a.data[i][k] * b.data[k][j] for k in range(a.col)])
        else :
            matrix = self.noneMatrix()
        return matrix
    
    def extend(self, another_matrix):
        if another_matrix.row != self.row:
            matrix = self.noneMatrix()
        else: 
            matrix = copy.deepcopy(self)
            n = matrix.row
            m = another_matrix.col
            
            for i in range(n):
                for j in range(m):
                    matrix.data[i].append(another_matrix.data[i][j])
                
            matrix.is_extended = True
            matrix.extended_col_A = matrix.col
            matrix.extended_col_B = m
            matrix.col += m

        return matrix

    def triangularize(self, upper=True):

        if self.is_squared :
            matrix = copy.deepcopy(self)
            n = matrix.row
            m = matrix.col    
            
            if upper:
                range_I = range(n-1)
                range_J = lambda i : range(i+1, n)
            else:
                range_I = range(n-1, 0, -1)
                range_J = lambda i : range(i-1, -1, -1)

            for i in range_I:
                for j in range_J(i):
                    if matrix.data[i][i] == 0:
                        foundPivot = False
                        for a in range(i, n):
                            if matrix.data[a][i] != 0:
                                matrix.data[a], matrix.data[i] = matrix.data[i], matrix.data[a]
                                foundPivot = True
                                break
                        else:
                            print("Non inversible matrix")

                    pivotRow = matrix.data[i]
                    pivot = pivotRow[i]
                    a = matrix.data[j][i] / pivot
                    for k in range(i, m):
                        matrix.data[j][k] = matrix.data[j][k] - a * pivotRow[k]
        else :
            matrix = self.noneMatrix()

        return matrix


    def diagonalize(self):
        if self.is_squared :
            matrix = copy.deepcopy(self)
            # applying upper and triangularization to a matrix diagonalize it
            matrix = matrix.triangularize(upper=True).triangularize(upper=False)
        else :
            matrix = self.noneMatrix()

        return matrix

    def transpose(mat):
        if mat.is_squared:
            n = mat.row
            matrix = Matrix(n, n)
            for i in range(n):
                for j in range(n):
                    matrix.data[i][j] = mat.data[j][i]
        else:
            matrix = mat.none_matrix()
        
        return matrix

