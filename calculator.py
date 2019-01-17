class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """
        try:
            return firstOperand + secondOperand
        except:
            raise TypeError("Please enter two numbers")

    def subtract(self, firstOperand, secondOperand):
        """Subtracts two numbers

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        try:
            return firstOperand - secondOperand
        except:
            raise TypeError("Please enter two numbers")

    def multiply(self, firstOperand, secondOperand):
        """Multiplies two numbers

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        if isinstance(firstOperand, int) and isinstance(secondOperand, int):
            return firstOperand * secondOperand

        else:
            raise TypeError("Please enter two numbers")

    def divide(self, firstOperand, secondOperand):
        """Divides two numbers

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        if isinstance(firstOperand, int) and isinstance(secondOperand, int) and secondOperand != 0:
            return firstOperand / secondOperand
        elif secondOperand == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            raise TypeError("Please enter two numbers")
