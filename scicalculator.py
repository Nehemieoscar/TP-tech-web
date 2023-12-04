def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:  
        return "Divizyon pa zero pa posib."
    else:
        return a / b

def exponent(a, b):
    return a ** b

def factorial(n):
    if n < 0:  
        return "Faktoryèl pa definis pou non-negatif."
    elif n == 0 or n == 1:  
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

def square(n):
    if n < 0:  
        return "Rasin kare pa definis pou non-negatif."
    else:
        return n ** 0.5
