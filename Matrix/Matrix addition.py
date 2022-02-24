print("Welcome to Matrix addition")
print()
print("Just one rule to remember, both matrices must need have same number of rows and columns.")
m = int(input("How many rows are the matrices?"))
n = int(input("How many columns are the matrices?"))

#matrices creation, always column came first.
matrixA = [[0 for x in range(n)] for x in range(m)]
matrixB = [[0 for x in range(n)] for x in range(m)]
matrixSum = [[0 for x in range(n)]for x in range(m)]

print("Please, type all elements of 1st Matrix:")
for i in range(0, m):
    for j in range(0, n):
        matrixA[i][j] = float(input(f"Element [{i},{j}]:"))

print("Please, type all elements of 2nd Matrix:")
for i in range(0, m):
    for j in range(0, n):
        matrixB[i][j] = float(input(f"Element [{i},{j}]:"))
print()
print(f"Matrix Sum")
for i in range(0, m):
    for j in range(0, n):
        matrixSum[i][j] = matrixA[i][j] + matrixB[i][j]
#Next operation is only to determine best space to tabulate
qtyMax = 0 #Just to start max character determination
qtyDec = 0 #Just to start max character determination
for i in range(0, m):
    for j in range(0, n):
        listMatrixSum = str(matrixSum[i][j]).partition('.')
        qtyBeforePoint = len(listMatrixSum[0])
        qtyAfterPoint = len(listMatrixSum[2])
        qtyTotal = qtyBeforePoint + qtyAfterPoint + 1
        #Another way is make direct len before partiotion
        if qtyMax < qtyTotal:
            qtyMax = qtyTotal
        if qtyDec < qtyAfterPoint:
            qtyDec = qtyAfterPoint
if qtyDec > 4:#Limitation of 4 digits
    qtyDec = 4
for i in range(0, m):
    for j in range(0, n):
        print(f"{matrixSum[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    print()

print(f"Summary:")
for i in range(0, m):
    for j in range(0, n):
        print(f"{matrixA[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    if i == 0:
        print(" + ", end="")
    else:
        print("   ", end="")
    for j in range(0, n):
        print(f"{matrixB[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    if i == 0:
        print(" = ", end="")
    else:
        print("   ", end="")
    for j in range(0, n):
        print(f"{matrixSum[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    print()