i = 1
sumOfSquares = 0

#Python While Loop
while sumOfSquares < 200:
    sumOfSquares = sumOfSquares + (i * i)
    print(sumOfSquares)
    i += 1

print(sumOfSquares)

print('---------------')

#Python Do-While Loop
while True:
    sumOfSquares = sumOfSquares + (i * i)
    print(sumOfSquares)
    i += 1
    if sumOfSquares > 200:
        break
   
print(sumOfSquares)