def fun(matrix):
    str_in = 0
    for i in range(len(matrix)):
        if all(element == 0 for element in matrix[i]):
            str_in = i
            break
    if str_in != 0:
        col_in = str_in
        for i in range(len(matrix)):
            matrix[i][col_in] /= 2
    if str_in == 0:
        print("В матрице нет строки со всеми нулевыми элементами")
    return matrix

while True:
    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))
        break
    except ValueError:
        print("Вы ввели букву")
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        while True:
            try:
                element = int(input("Введите элемент матрицы: "))
                break
            except ValueError:
                print("Вы ввели букву")
        row.append(element)
    matrix.append(row)
print("Матрица:")
for row in matrix:
    print(row)
rez_matrix = fun(matrix)
print("Результирующая матрица:")
for row in matrix:
    print(row)