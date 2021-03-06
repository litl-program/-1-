'''
Серед усіх чисел діапазону [0; A] знайти кількість чисел,
сума цифр яких є квадратом цілого числа. 
Також знайти середнєарифметичне таких чисел.
'''

# Розбиття натурального числа N на цифри
# 5475 = 5*10**3 + 4*10**2 + 7*10**1 + 5*10**0
# Ми можемо завжди отримати ОСТАННЮ цифру числа N як остачу від ділення N на 10
# 7894 % 10 = 4 - остача (залишок) від ділення, оскільки 7894 = 789 * 10 + 4
# 7894: 7894 % 10 = 4
#       789 % 10 = 9    -> 7894 // 10 = 789
#       78 % 10 = 8     -> 789 // 10 = 78
#       7 % 10 = 7      -> 78 // 10 = 7
#                       -> 7 // 10 = 0
A = int (input("A = "))
while A < 0: # а нам за умовою задачі потрібно щоб A > 0
    A = int (input("A = "))
number = 0
count = 0 # кількість чисел, сума цифр яких є квадратом цілого числа
S = 0 # сума таких чисел
# тобі середнє арифметичне таких чисел дорівнює S / count
while number <= A: # пробігаємо числа number = 0, 1, 2 ... A - діапазон [0; A]
    sum_of_digits = 0
    _number = number
    while number > 0: # виходимо з циклу, коли number стане дорівнювати 0
        last_digit = number % 10 # остання цифра
        number = number // 10
        sum_of_digits = sum_of_digits + last_digit # знаходимо суму цифр
    int_sqrt_sum = int(sum_of_digits**(1/2))
     # 9 == (int(9**(1/2)))**2
    if int_sqrt_sum**2 == sum_of_digits: # число sum_of_digits є квадратом цілого числа
        S = S + _number
        count = count + 1
    number = number + 1
print ("Кількість чисел, сума цифр яких є квадратом цілого числа", count)
if count != 0:
    print("Середнє арифметичне таких чисел", S / count)
