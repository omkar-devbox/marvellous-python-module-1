def Summetion(Data):
    sum = 0
    for i in Data:
        sum = sum + i
    return sum

    


def main():
    size= 0
    Arr = list()
    print("Enter the number of Elememnt :")
    Size = int(input())
    print("Enter the Elements :")
    for i in range(Size):
        no = int(input())
        Arr.append(no)
    ret = Summetion(Arr)
    
    print("Summetion is ",ret)
    

if __name__ == "__main__":
    main()