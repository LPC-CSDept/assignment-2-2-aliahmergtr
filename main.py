def main():
    """
    ##################################################
    # Complete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = float(input("enter a temperature in celsius: "))
    fahrenheit = ((9/5)*celcius)+32
    print(f'Fahrenheit: \t {fahrenheit:.2f}')

# my github link: https://github.com/LPC-CSDept/assignment-2-2-aliahmergtr

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
