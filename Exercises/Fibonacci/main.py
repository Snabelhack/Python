import fibbonacci as fib

# Main
fib = fib.fibonacci()

print("Skriv in ett heltal: ")
var = int(input())

seq = []

seq.append(fib(var) for var in range(var))

print(seq)

