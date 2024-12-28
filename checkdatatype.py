a=5
print("type of a: ", type(a))

b=6.5
print("type of b: ", type(b))

c=True
print('type of c: ', type(c))

d="codingal"
print('type of d: ', type(d))


a=str(a)
print(a, type(a))

b=int(b)
print(b, type(b))

c=str(c)
print(c, type(c))

num=int(input("Please enter any number: "))
print(num, type(num))



str1="Hello"
str2="World"

print("Joined form: ", str1+str2)
print(len(str1+str2))

print(str1[1:3:])
print(str1[::-1])
print(str2[1::])