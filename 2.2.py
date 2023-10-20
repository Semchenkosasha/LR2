def fun(a):
    if isinstance(a, list):
        p = 1
        for i in range(len(a)):
            if i % 2 == 1:
                p *= a[i]
        max_l = max(a)
        a.remove(max_l)
        return p, a
    elif isinstance(a, dict):
        sorted_dict = dict(sorted(a.items()))
        return sorted_dict
    elif isinstance(a, int):
        if a < 2:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True
    elif isinstance(a, str):
        gl = 0
        sgl = 0
        for c in a.lower():
            if c.isalpha():
                if c in 'aeyuioыяиэё':
                    gl += 1
                else:
                    sgl += 1
        return gl, sgl


elements = [1, 2, 3, 4, 5, 6, 7]
print("Список: ", elements)
p_elements, r_elements = fun(elements)
print("Произведение элементов с нечетными номерами:", p_elements)
print("Новый список с удаленным элементом: ", r_elements)

d = {'b': 9, 'l': 78, 'a': 8, 'i': 1}
s_d = fun(d)
print("Словарь: ", d)
print("Отсортированный словарь: ", s_d)

while True:
    try:
        numb = int(input("Введите число: "))
        break
    except ValueError:
        print("Вы ввели букву")
ch = fun(numb)
print("Число простое: ", ch)

print("Введите строку: ")
s = input()
glasn, soglasn = fun(s)
print("Количество гласных в строке: ", glasn)
print("Количество согласных в строке: ", soglasn)
