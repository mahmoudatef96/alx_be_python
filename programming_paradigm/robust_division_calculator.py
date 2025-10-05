def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        try:                
            result = num / den
        except ZeroDivisionError:
            return("Error: Cannot divide by zero.")
        return(f"The result of the division is {result}")
    except ValueError:
        return("Error: Please enter numeric values only.")
   
    