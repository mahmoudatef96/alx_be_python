def perform_operation(num1: float, num2: float, operation: str):
    """ this functioim oerform some operations"""
    match operation : 
        case "add":
            return(num1 + num2)
        case "subtract":
            return(num1 - num2)
        case "multiply":
            return(num1 * num2)
        case "divide":
            if num2 == 0:
                print("can't divide on zero")
                return(None)
            else:
                return(num1 / num2)