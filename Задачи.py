abc = int(123) 
a = abc % 10
b = abc % 100
b = b // 10
abc = abc // 100
print (str(abc) + str(a) + str(b))


a = 1234
a = (a // 100) % 10
print (a)


a = 101
if a == 0: print("Нулевое число")
elif a < 0 and a% 2 == 0: print ("отрицательное четное число")
elif a > 0 and a% 2 == 0: print ("положительное четное число")
elif a < 0 and a % 2 != 0: print ("отрицательное не четное число")
elif a > 0 and a% 2 != 0: print ("положительно не четное число")


a = int(2)
b = int(5)
q = a + b
w = a - b
e = a * b
r = a / b
print("Операция №1 = "+str(q))
print("Операция №2 = "+str(w))
print("Операция №3 = "+str(e))
print("Операция №4 = "+str(r))
print("Гойдаааа")