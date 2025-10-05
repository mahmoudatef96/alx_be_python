def perform_operation(num1, num2, operation):
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
            elif num2 == 0:
                return(num1 / num2)