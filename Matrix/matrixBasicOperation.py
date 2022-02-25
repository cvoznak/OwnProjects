print("Welcome to Matrix Basic Operation")
print()
print("If addiction or subtraction, both matrices must need have same number of rows and columns.")
print("(1) Matrix Addition: A + B = C")
print("(2) Matrix Subtraction: A - B = C")
cod = int(input("Which operation do you wish execute? (1 / 2)"))

m = int(input("How many rows are the matrices?"))
n = int(input("How many columns are the matrices?"))

#matrices creation, always column came first.
matrixA = [[0 for x in range(n)] for x in range(m)]
matrixB = [[0 for x in range(n)] for x in range(m)]
matrixC = [[0 for x in range(n)] for x in range(m)]

print("Please, type all elements of Matrix A:")
for i in range(0, m):
    for j in range(0, n):
        matrixA[i][j] = float(input(f"Element [{i},{j}]:"))

print("Please, type all elements of Matrix B:")
for i in range(0, m):
    for j in range(0, n):
        matrixB[i][j] = float(input(f"Element [{i},{j}]:"))


for i in range(0, m):
    for j in range(0, n):
        if cod == 1:
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
        elif cod == 2:
            matrixC[i][j] = matrixA[i][j] - matrixB[i][j]

#Next operation is only to determine best space to tabulate
qtyMax = 0 #Just to start max character determination
qtyDec = 0 #Just to start max character determination
for i in range(0, m):
    for j in range(0, n):
        listMatrixC = str(matrixC[i][j]).partition('.')
        qtyBeforePoint = len(listMatrixC[0])
        qtyAfterPoint = len(listMatrixC[2])
        qtyTotal = qtyBeforePoint + qtyAfterPoint + 1
        #Another way is make direct len before partiotion
        if qtyMax < qtyTotal:
            qtyMax = qtyTotal
        if qtyDec < qtyAfterPoint:
            qtyDec = qtyAfterPoint
if qtyDec > 4:#Limitation of 4 digits
    qtyDec = 4

print()
if cod == 1:
    print(f"Matrix Sum")
elif cod == 2:
    print(f"Matrix Subtract")
for i in range(0, m):
    for j in range(0, n):
        print(f"{matrixC[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    print()

print(f"Summary:")
for i in range(0, m):
    for j in range(0, n):
        print(f"{matrixA[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    if i == 0:
        if cod == 1:
            print("  + ", end="")
        elif cod == 2:
            print("  - ", end="")
    else:
        print("    ", end="")
    for j in range(0, n):
        print(f"{matrixB[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    if i == 0:
        print("  = ", end="")
    else:
        print("    ", end="")
    for j in range(0, n):
        print(f"{matrixC[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    print()