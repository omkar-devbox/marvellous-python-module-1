
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