print('------------------------------------------')

#TUPLESINPYTHON
t1=()
print(type(t1))

t2=(23,12,35,668,654,58)
print(t2)

t3=(31,'vineet',77.5,'maithon')
print(t3)

print(t2[1])

print(t2[2:4])

print(t2[:3])

print('------------------------------------------')

t4=(3,4,5,6,3,4,9,5,3,8,3,1)
print(t4)

#count
print(t4.count(3))

#To add Tuple
print(sum(t4))

#to find max
print(max(t4))

#to find min
print(min(t4))

#DELETE A tUPLE
del t1

print('------------------------------------------')

#ADD MORE THAN 1 TUPLE
t5=(1,2,3,4,5)
t6=(6,7,8,9,10)
t7=t5+t6
print(t7)

#length
print(len(t4))

#IN
if(9 in t4):
    print("available")
else:
    print(" not available")

#convert into list
l1=list(t4)
l1[2]=100
t4=tuple(l1)
print(t4)