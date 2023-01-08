import fibbonacci as fib

# Main
fib_of = fib.Fibonacci()
#Prompt user for input
print("Skriv in ett heltal: ")
var = int(input())

print([fib_of(n) for n in range(var)])