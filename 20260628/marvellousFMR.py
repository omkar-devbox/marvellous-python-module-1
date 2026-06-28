from functools import reduce

def FilterX(Task,Elements):
    Result = []

    for no in Elements:
        ret = Task(no) # CheckEven(no)
        if ret == True:
            Result.append(no)
    
    return Result

def MapX(Task,Elements):
    Result = []

    for no in Elements:
        ret = Task(no) # CheckEven(no)
        Result.append(ret)
    
    return Result


    
def ReduceX(Task,Elements):
    Sum = 0 
    for no in Elements:
        Sum = Task(Sum,no)
    return Sum
    

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
