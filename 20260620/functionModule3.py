from Marvellous import Addition
def main():
    print("Enter first Number :")
    value1 =int(input())
    print("Enter Second Number :")
    value2 = int(input())
    
    ret= Addition(value1 , value2)
    print("Addition is :",ret)

    ret = Substraction(value1,value2) #Error
    print("Substraction :" ,ret)


if __name__ == "__main__":
    main()