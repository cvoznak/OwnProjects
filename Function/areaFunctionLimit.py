import numpy as np
from matplotlib import pyplot as plt

#Determine polynomials degree
from matplotlib import pyplot

n = int(input("Function degree: "))
#Create an empty list
coeff = []
#Add values to this list, a value per degree, will be the coefficients of polynomial function
for i in range(0, n + 1):
    coeff.append(float(input(f"Type coefficient of x^{n-i}:")))

#Uses numpy to create a polynomial function p
p = np.poly1d(coeff)
print("Polynominal function:")
print(p)

#Determine limits to study
xStart = float(input("x(start) = "))
xStop = float(input("x(stop) = "))

#Area under the fuction according integral
area = np.polyint(p)
print("Integral of Polynominal function")
print(area)
areatotal = area(xStop) - area(xStart)
print(f"Area below polynominal function between {xStart} and {xStop} is {areatotal:.4f}")

print("Approximate the area under the curve using rectangles")
#Number of rectangles / divisions to calculate area
precision = int(input("How many rectangles / divisions must need be applied? "))
#delta x, limits to calculate area
fullPeriod = xStop - xStart
n = fullPeriod / precision
areaPrecision = 0
for i in range(0, precision):
    areaPrecision += p(xStart + n / 2 + i * n) * n
print(f"Area below polynominal function between {xStart} and {xStop} is {areaPrecision:.4f}")
print(f"Absolute deviation = {abs(areatotal - areaPrecision):.4f} and Error percentage = {(abs(areatotal - areaPrecision) * 100 / areatotal):.2}%")
#Plot
#Define array to plot function
x = np.arange(xStart, xStop)
#Applies array in function
y = p(x)
#Plot function according array
plt.plot(x, y)
#Shows plotted function
plt.show()


