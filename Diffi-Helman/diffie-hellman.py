# Публичные ключи
# Одни на всех
p = 3001 # Простое число
q = 2    # Натуральное число

if q**(p-1)%p != 1: 
    print("Error")
    raise SystemExit

# Приватные ключи
# Натуральное числа

mLittel = [84503, 90236, 74923, 62398, 38920, 82983, 59280, 39009, 29099, 13289]
print("LITTEL: ")
print(mLittel)
print('\n') 

# Публичные ключи
mBig = []
for i in range(10):
   mBig.append((q**mLittel[i])%p)

print("BIG: ")   
print(mBig)
print('\n') 

print("BIG:  LITTEL: ")    

# Приватные ключи
# kA == kB
# Их используют для шифрования по любому другому синхронному алгоритму
keys = []
for i in range(10):
   for j in range(10):
      keys.append((mBig[j]**mLittel[i])%p)
      #print(mBig[j], ' ' ,mLittel[i], ' :', keys[-1])
      print(j, ' ' ,i, ' :', keys[-1])


print('\n')    
print(keys)
print('\n')   

print(keys[0])

for i in range(100):
   if (i<100):
    if(keys[i] == keys[i+1]):
        print(keys[i])

# Приватные ключи
# kA == kB
# Их используют для шифрования по любому другому синхронному алгоритму
#kA = B**a%p # Key
#kB = A**b%p # Key
#print(kA, kB)


