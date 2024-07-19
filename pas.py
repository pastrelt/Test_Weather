#string = input("Введите числа через пробел:")
string = input("Введите числа через пробел:").split()
print(string)
# f = string[0:1]
# #print(f)
# end_s = string[-1:]
# #print(end_s)
# string.pop(0)
# string.pop(-1)
# print(string)
# string.append(f)
# print(string)
# string.append(end_s)
# print(string)
string[0], string[-1] = string[-1], string[0]
#sum_s = sum(map(int, string))
string.append(sum(map(int, string)))
print(string)