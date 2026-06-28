from functools import reduce

def CheckEven(no):
    return no%2 == 0

def Increment(no):
    return no + 1

def Addition(no , no2):
    return no + no2 
  

def main():
    data= [13,12,8,10,11,20]
    print("Input Data is :",data)

    FData = list(filter(CheckEven,data))
    print("Data After Filter :",FData)

    MData = list(map(Increment,data))
    print("Data After Map :",MData)

    RData = reduce(Addition,FData)
    print("Data After reduce :",RData)
if __name__ == "__main__":
    main()