#                          Tuple                List
#-----------------------------------------------------------------------------
#Ordered                   yes                  Yes
#Indexed                   yes                  Yes
#Mutable                   No                   Yes

def main():
    Data1 = [10,20,30,40]
    Data2 = (10,20,30,40)

    for i in Data1:
        print("Data1 ",i)
    for i in Data2:
        print("Data 2",i)

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])

if __name__== "__main__":
    main()