#Дана строка. Вывести ее три раза через запятую и показать количество символов в ней.

#
# string=input('Enter string  ')
# for i in range(3):
#     print(f'{string}, ',end='')
#
# print(len(string))


#Дана строка. Вывести первый, последний и средний (если он есть)) символы.
#
# string=input('Enter string  ')
# print(string[0])
# print(string[len(string)-1])
# print(string[(len(string))//2])

#Дана строка. Показать номера символов, совпадающих с последним символом строки.

#string=input('enter string  ')
#for i in range(len(string)):
#    if string[i]==string[-1]:
#        print(i)


import random as rm


# class Die():
#     def __init__(self, num_sides=6):
#         self.__num_sides = num_sides
#
#     def roll(self):
#         return rm.randint(1, self.__num_sides)
#     def kilk_sides(self):
#         return self.__num_sides
#
# die = Die()
#
# results=[]
#
# for i in range(10):
#     results.append(die.roll())
#
# #print(results)
#
# frequence=[]
# sides_for_cycles=die.kilk_sides()+1
# for i in range(1,sides_for_cycles):
#     frequency=results.count(i)
#     frequence.append(frequency)
#
# print(frequence)



class Die():
    def __init__(self, num_sides=6):
        self.__num_sides = num_sides

    def roll(self):
        return rm.randint(1, self.__num_sides)
    def kilk_sides(self):
        return self.__num_sides

die = Die()

results=[]

print("HELLO WORLD")

for i in range(1000):
    results.append(die.roll()+die.roll())

print(results)

frequence=[]
sides_for_cycles=(2*die.kilk_sides())+1
for i in range(2,sides_for_cycles):
    frequency=results.count(i)
    frequence.append(frequency)

print(frequence)