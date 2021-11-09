i = 1
sumOfSquares = 0

#Python While
while sumOfSquares < 200:
    x = (i * i)
    sumOfSquares = sumOfSquares + x
    i += 1

print(sumOfSquares)

print('---------------')

#Python Do-While
while True:
    x = (i * i)
    sumOfSquares = sumOfSquares + x
    i += 1
    if sumOfSquares > 200:
        break
   
print(sumOfSquares)