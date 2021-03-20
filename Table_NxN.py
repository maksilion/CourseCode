"""
stepik.org -> Программирование на Python

Выведите таблицу размером n×n,
заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и
закрученной по часовой стрелке,
как показано в примере (здесь n=5):

Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

n = int(input("Please, enter table dimension - "))
mat = [["0" for j in range(n)] for i in range(n)]
sumSubSq = int(len(mat) / 2) - 1
x = 1
subSq = 0
while subSq<=sumSubSq+3:
    #Up
    for j in range(subSq, n-(subSq+1)):
        mat[subSq][j] = x
        x += 1
    if subSq == n-(subSq+1):
        mat[subSq][n-(subSq+1)] = x
    #Left
    for i in range(subSq, n-(subSq+1)):
        mat[i][(n-1)-subSq] = x
        x += 1
    #Down
    for j in range((n-1)-subSq,subSq, -1):
        mat[(n-1)-subSq][j] = x
        x += 1
    #Right
    for i in range((n-1)-subSq, subSq, -1):
        mat[i][subSq] = x
        x += 1
    subSq +=1
for i in range(n):
    print(str(mat[i])[1:-1].replace(",",""))