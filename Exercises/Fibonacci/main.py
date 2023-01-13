import fibbonacci as fib
import numpy as np
import seaborn as sns
import pandas as pd

# Main
fib_of = fib.Fibonacci()
#Prompt user for input
print("Skriv in ett heltal: ")
var = int(input())

print([fib_of(n) for n in range(var)])