import Marvellous as MI
def main():
    print("Enter first Number :")
    value1 =int(input())
    print("Enter Second Number :")
    value2 = int(input())
    
    ret= MI.Addition(value1 , value2)
    print("Addition is :",ret)


if __name__ == "__main__":
    main()