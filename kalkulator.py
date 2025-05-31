def add(x, y):
    return x + y

def subtract(x, y):

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("nie dzielimy przez zero")
    return x / y

if __name__ == "__main__":
    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    
    choice = input("Wprowadź numer operacji (1-4): ")
    num1 = float(input("Wprowadź pierwszą liczbę: "))
    num2 = float(input("Wprowadź drugą liczbę: "))
    
    if choice == '1':
        print(f"Wynik: {add(num1, num2)}")
    elif choice == '2':
        print(f"Wynik: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Wynik: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"Wynik: {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Nieprawidłowy wybór.")
