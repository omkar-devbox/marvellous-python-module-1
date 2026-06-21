# Accept : multiple Parameter
# Return : multiple value
def marvellous(value1,value2):
    print("Inside Marvellous :",value1,value2)
    return 21,51

def main():
    ret1,ret2 = marvellous(11,20)
    print("Return values are :",ret1,ret2)

if __name__ == "__main__":
    main()
else:
    print("Error")