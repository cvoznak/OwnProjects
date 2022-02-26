print("Welcome to Product between two Matrix")
print()
print("In the case of product between two matrix, there is a restriction regarding number of rows and columns.\n"
      "If Matrix A is an m x n matrix, B matrix necessary need be n x p matrix, and m = p or not.")
print()
print("Matrix A")
m = int(input("How many rows is the Matrix A?"))
n = int(input("How many columns is the matrix A?"))
print()
print("Matrix B")
print(f"Matrix B has {n} rows")
p = int(input("How many columns is the Matrix B?"))

#matrices creation, always column came first.
matrixA = [[0 for x in range(n)] for x in range(m)]
matrixB = [[0 for x in range(p)] for x in range(n)]
matrixC = [[0 for x in range(p)]for x in range(m)]

print("Please, type all elements of Matrix A:")
for i in range(0, m):
    for j in range(0, n):
        matrixA[i][j] = float(input(f"Element [{i},{j}]:"))

print("Please, type all elements of Matrix B:")
for i in range(0, n):
    for j in range(0, p):
        matrixB[i][j] = float(input(f"Element [{i},{j}]:"))
print()
print(f"Matrix Multiplication")
for i in range(0, m):
    for k in range(0, p):
        for j in range(0, n):
            matrixC[i][k] += (matrixA[i][j] * matrixB[j][k])

#Next operation is only to determine best space to tabulate
qtyMax = 0 #Just to start max character determination
qtyDec = 0 #Just to start max character determination
for i in range(0, m):
    for j in range(0, p):
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
for i in range(0, m):
    for j in range(0, p):
        print(f"{matrixC[i][j]:{qtyMax + 2}.{qtyDec}f}", end="")
    print()

