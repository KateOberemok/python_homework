n = int(input("введите размерность матрицы А:  ")) #вводим число строк матрицы А
inverse_matrix = 1

def identity_matrix(n): #единичная матрица
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix

def enter_matrix(n): #ввод матрицы nxn
    matrix = []
    for i in range(n):
        list = (input("введите " + str(i + 1) + "-ю строку через пробел: ")).split()
        if len(list) != n:
            print ("error")
            break
        else:
            for element in range(len(list)):
                list[element] = int(list[element])
            matrix.append(list)
    return matrix

def divide_string(str, div): #деление строки на число
    for j in range(len(str)):
        str[j] = str[j] / div
    return str

def subtraction_string(str1, str2, multiplier): #вычитание из строки другой. умноженной на число
    for j in range(len(str1)):
        str2[j] = str2[j] - str1[j] * multiplier
    return str2

def rewriting_row(matrix, first_str, second_str): #меняем строки местами
    additional_list = matrix[first_str]
    matrix[first_str] = matrix[second_str]
    matrix[second_str] = additional_list
    return matrix

def straight_run(matrix1, matrix2, count): #обнуляем столбец под диагональю
    divident = matrix1[count][count]
    divide_string(matrix1[count], divident)
    divide_string(matrix2[count], divident)
    for i in range(n - count - 1):
        multiplier = matrix1[i + count + 1][count]
        subtraction_string(matrix1[count], matrix1[i + count + 1], multiplier)
        subtraction_string(matrix2[count], matrix2[i + count + 1], multiplier)



matrix_E = identity_matrix(n)
matrix_R = enter_matrix(n)

for counter in range(n): #прямой ход
    if matrix_R[counter][counter] != 0:
        straight_run(matrix_R, matrix_E, counter)
    else:
        marker = 0
        for k in range(n - counter - 1):
            if matrix_R[counter + k + 1][counter] != 0:
                rewriting_row(matrix_R, counter, counter + k + 1)
                rewriting_row(matrix_E, counter, counter + k + 1)
                marker = 1
        if marker == 1:
            straight_run(matrix_R, matrix_E, counter)
        else:
            inverse_matrix = 0
            break

if inverse_matrix == 1:
    for counter in range(n - 1): #обратный ход
        for i in range(n - counter - 1):
            multiplier = matrix_R[n - i - counter - 2][n - counter - 1]
            subtraction_string(matrix_R[n - counter - 1], matrix_R[n - i - counter - 2], multiplier)
            subtraction_string(matrix_E[n - counter - 1], matrix_E[n - i - counter - 2], multiplier)

    print("обратная матрица")
    for i in range(n):
        for j in range(n):
            matrix_E[i][j] = round(matrix_E[i][j], 2)
        print(matrix_E[i])
else:
    print("обратной матрицы нет!")