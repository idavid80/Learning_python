import sys

def PrimeraLetraMayísculas:
    for line in sys.stdin:
        print(line.strip().capitalize())

# cat archivo.txt | ./pipe.py

# cat ./pipe.py < archivo.txt