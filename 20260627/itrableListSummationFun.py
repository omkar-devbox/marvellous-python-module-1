def Summation(Data):
    Sum1 = 0
    for no in Data:
        Sum1 = Sum1 + no
    return Sum1


def main():
    # pass
    Marks = [78,90,56,98,77]

    ret = Summation(Marks)
    print("Return sum :",ret)


    

if __name__ == "__main__":
    main()