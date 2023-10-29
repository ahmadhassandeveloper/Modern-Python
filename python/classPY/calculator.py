import numpy as np
import pandas as pd
import matplotlib 

#Addition
add1 = int(input("First Number: "))
add2 = int(input("Second Number: "))
print(add1 + add2)

#Subtraction
sub1 = int(input("First Number: "))
sub2 = int(input("Second Number: "))
sub = sub1 - sub2

print(f'Subtraction Result = {sub}')

np1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np1.ndim)

np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np3 = np.dot(np1, np2)
print(np3)

df = pd.read_csv("pd.csv")
a = df["year"]
b = df["value"]
c = pd.concat([a, b])
print(c)

# # Yield Function
# from collections.abc import Iterator

# def my_generator()-> Iterator[int]:
# function statements
