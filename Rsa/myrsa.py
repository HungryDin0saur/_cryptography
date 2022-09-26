from encodings import codecs

p = 2411; q = 4957
print("p = %d; q = %d"%(p,q))

n = p * q 
Fn = (p-1)*(q-1)

print("n = %d; f(n) = %d\n"%(n, Fn))

e = 4769 
print("e =", e,'\n')

k = 2
d = int((1 + k * Fn) / e)

print("k = %d; d = %d\n"%(k,d))

public_key = [e, n]
private_key = [d, n]

print("public_key:",public_key)
print("private_key:",private_key,'\n')

Keys = ("Rodina!", "Narayd", "Yvalnenie", "Pennivays", "qwerty", "Kamaz", "Lom", "Moskva", "Raketa", "KHO")

A = []

#преобразование слова в число

for i in range(len(Keys)):
    A.append(codecs.encode(Keys[i].encode(), 'HEX'))
    A[i] = int(A[i].decode(), 16)
    print(A[i])
   
print(Keys)  
Message = []

print('*********************')

for i in range(len(A)):
     buf = pow(A[i], e, n)
     Message.append(buf)

'''
for i in range(10):
  for j in range(len(Keys[i])):
     buf = ord(Keys[i][j]) ** e % n
     Message.append(buf)
'''    
print(Message)

for i in range(len(Message)):
     buf = pow(Message[i], d, n)
     Message[i] = buf
     
print(Message)