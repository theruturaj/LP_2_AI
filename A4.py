class NQueensProblem:
    def __init__(self, n):
        self.n = n
        self.columns = [-1] * n
        self.rows = set()
        self.up_diagonals = set()
        self.down_diagonals = set()
        self.solutions = []
 
    def solve(self):
        self.backtrack(0)
        return self.solutions
 
    def backtrack(self, col):
        if col == self.n:
            solution = self.columns[:]
            self.solutions.append(solution)
            return
 
        for row in range(self.n):
            if row in self.rows or col + row in self.up_diagonals or col - row in self.down_diagonals:
                continue
 
            self.columns[col] = row
            self.rows.add(row)
            self.up_diagonals.add(col + row)
            self.down_diagonals.add(col - row)
 
            self.backtrack(col + 1)
 
            self.columns[col] = -1
            self.rows.remove(row)
            self.up_diagonals.remove(col + row)
            self.down_diagonals.remove(col - row)

n = 4
problem = NQueensProblem(n)
solutions = problem.solve()
for solution in solutions:
    print(solution)
