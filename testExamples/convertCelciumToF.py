'''A=input("Enter temperature in Celcius")
A=int(A)
B=A*9
C=B/5
D=C+32
print(D)

if D > 90:
    print ('hot')
else :
    print ("cold")
    print("cold 1")
print ("this is outside if")
'''
import datetime
now = datetime.datetime.now()
'''print(now)
print(str(now))
print(repr(now))
'''
now_new = repr(now)
print(now_new)
print(str(now_new))
print(repr(now_new))
#print(isinstance(now_new, datetime))
