def CheckEven(no):
    if (no % 2 == 0):
        print("Its Even Number")
    else:
        print("Its Odd Number")

def main():
    value = int(input("Enter Number :"))
    CheckEven(value)


if __name__ == "__main__":
    main()