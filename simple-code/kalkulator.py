command = ""

while command != "exit":
    command = input("Perintah : ")
    
    if command == "exit":
        break
    
    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Perintah tidak dikenali")
        continue
    
    a = int(input("Masukan angka pertama : "))
    b = int(input("Masukan angka kedua : "))
    
    if command == "+":
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b
        
    print(f"Hasilnya : {result}\n")
    

    
print("Program telah selesai")