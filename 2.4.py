def fun(a, b):
    try:
        rez = a / b
        print("Результат:", rez)
    except ZeroDivisionError:
        print("Деление на 0 невозможно")
    finally:
        print("Этот блок будет выполняться всегда")


fun(5, 0)
fun(10, 2)

try:
    a=int(input("Введите число"))
    print(a)
except ValueError:
    print("Вы ввели не число")
finally:
    print("Этот блок выполняется всегда")
