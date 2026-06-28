CheckEven = lambda no: no%2 == 0

Increment = lambda no: no + 1
  

def main():
    data= [13,12,8,10,11,20]
    print("Input Data is :",data)

    FData = list(filter(CheckEven,data))
    print("Data After Filter :",FData)

    FData = list(map(Increment,data))
    print("Data After Map :",FData)
    
if __name__ == "__main__":
    main()