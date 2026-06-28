from marvellousLib import FilterX,MapX,ReduceX
    

CheckEven = lambda no : no%2 == 0

Increment = lambda  no : no + 1

Addition = lambda no,no2: no + no2 
  

def main():
    data= [13,12,8,10,11,20]
    print("Input Data is :",data)

    FData = list(FilterX(CheckEven,data))
    print("Data After Filter :",FData)

    MData = list(MapX(Increment,FData))
    print("Data After Map :",MData)

    RData = ReduceX(Addition,MData)
    print("Data After reduce :",RData)

if __name__ == "__main__":
    main()
