def operator(a, b, operation):
    if operation == "+":
        return a + b 
    if operation == "-":
        return a - b 

    if operation == "×":
        return a * b 
    if operation == "÷":
        return a / b 
        
print(operator(45, 15, "+"))