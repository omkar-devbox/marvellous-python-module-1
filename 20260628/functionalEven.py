CheckEven = lambda no: (no % 2 == 0)

def main():
    value = int(input("Enter Number :"))
    ret = CheckEven(value)
    print(ret)
    if (ret == True):
        print("its Even Number")
    else:
        print("its Odd Number")


if __name__ == "__main__":
    main()