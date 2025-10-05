def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        result = num1 / num2
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric."




# def safe_divide(numerator:int, denominator:int):
#     try:
#         divide = numerator/denominator
#         return divide
#     except ZeroDivisionError:
#         print("Error, cannot divide by zero")
#     except ValueError:
#         print("Incorrect value entered, try again")
#     else:
#         return divide
       

    
