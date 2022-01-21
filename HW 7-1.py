a = [[5, 3, 1, 6], [4, 3, 2, 2], [9, 0, 8, 7]]
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 1]]
from typing import Union, List

class Matrix:

    def __init__(self, lists: List[Union[list, str]]):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrx1 = Matrix(a)
matrx2 = Matrix(b)

print(matrx1, '\n')
print(matrx2, '\n')
print(matrx1 + matrx2)


