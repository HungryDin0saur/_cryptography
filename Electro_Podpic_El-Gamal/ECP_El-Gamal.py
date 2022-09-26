from encodings import codecs
from decimal import *

"""
Функции нахождения обратного по модулю: k^-1 (mod(p-1))
"""
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


#большое простое целое число 
p = 94034392403249090263
#большое целое число
a = 17364354
#случайное число-закрытый ключ
x = 2342329437249729347

messages = ["Zemlya", "Topol", "Linux", "Baykonur", "AK-47", "Kalibr", "Moskva", "Elbrus", "Perlovka", "Tank"]

#отрытый ключ
y = pow(a, x, p)
print("Public key:")
print(y)

for i in range(len(messages)):
   messages[i] = int(codecs.encode(messages[i].encode(), 'HEX').decode(), 16)
   print(messages[i])

#случайное целое число   
k = [321323123, 923323325, 821323165, 455323735, 525393761, 785295763, 624187721, 134187521, 334987529, 721683529]
print("Случайное целое число k= ")
print(k)

r = []
for i in range(len(k)):
   r.append(pow(a, k[i], p))
   print("r= ")
   print(r[i])

#messages[0] = Х * r + К * s mod(Р-1) - формула для вычисления s
#s = (m- (x * r))*k^(-1) mod(p-1)

ko = []
for i in range(len(k)):
   ko.append(modinv(k[i], (p-1)))
   print("Обратное по модулю к k: ")
   print(ko[i])

s = []

for i in range(len(messages)):
   s.append(((messages[i] - (x * r[i]))*ko[i])%(p-1))
   print("s -", i, ":")
   print(s[i])


#Проверка подлиннности сообщения: 

for i in range(len(messages)):
  if(pow(a,messages[i],p) == (pow(y,r[i],p) * pow(r[i],s[i],p))%p):
     print("Yes")
     print((pow(y,r[i],p) * pow(r[i],s[i],p))%p)
  else:
      print("++++++++++++++++++++++++++++++")
      print(pow(a,messages[i],p))
      print((pow(y,r[i],p) * pow(r[i],s[i],p))%p)
      
     
print("STOP!")





