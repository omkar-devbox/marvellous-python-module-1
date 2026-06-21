def calculation(No1,No2):
    Mult = No1 * No2
    Div  = No1 / No2
    return Mult,Div

def main():
    value1 = int(input("Enter First Number :"))
    value2 = int(input("Enter Second Number :"))
    
    Ret1,Ret2 = calculation(value1,value2)
    print("Multipliation :",Ret1)
    print("Division",Ret2)


if __name__ == "__main__":
    main()
else:
    print("Error")