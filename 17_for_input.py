Напишите программу, которая считывает с клавиатуры два числа a и b, 
считает и выводит на консоль среднее арифметическое всех чисел из 
отрезка [a;b], которые делятся на 3.

В приведенном ниже примере среднее арифметическое считается для чисел 
на отрезке [−5;12]. Всего чисел, делящихся на 3, на этом 
отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда 
есть хотя бы одно число, которое делится на 3.

a = int(input())
b = int(input())
s = 0
c = 0
for j in range (a,b+1):
    if j%3 == 0:
        s = s+j #42
        c = c+1
    j+=1
print(s/c)
