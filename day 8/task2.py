import math  
while 1:  
    print ("1) Add")  
    print ("2) Subtract")
    print ("3) Divide")
    print ("4) Multiply")
    print ("0) Exit")

    try:  # This is a try statement used to handle errors
        answer = input("Option: ")  
        if answer == 1:  
            first = float(input("First Number: "))  
            second = float(input("Second Number: "))  
            final = first + second 
            print ("Answer:", float(final)) 
            print()
        elif answer == 2:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first - second
            print ("Answer:", float(final)) 
            print()
        elif answer == 3:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first / second
            print ("Answer:", float(final))
            print()
        elif answer == 4:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first * second
            print ("Answer:", float(final))
            print()
        elif answer == 0: 
            break
        else:  
            print ("\nPlease select a valid option number\n")
    except NameError: 
        
        print ("\nNameError: Please Use Numbers Only\n")
        
    except SyntaxError:  # SyntaxError means we typed letters or special characters i.e !@#$%^&*( or if we tried to run python code
        
        print ("\nSyntaxError: Please Use Numbers Only\n")
        
    except TypeError:  # TypeError is if we entered letters and special characters or tried to run python code
        
        print ("\nTypeError: Please Use Numbers Only\n")
        
    except AttributeError:  # AttributeError handles rare occurances in the code where numbers not on the list are handled outside of the if statement
        
        print ("\nAttributeError: Please Use Numbers Only\n")
        