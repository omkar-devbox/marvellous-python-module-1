#                          Tuple                List
#-----------------------------------------------------------------------------
#Ordered                   yes                  Yes
#Indexed                   yes                  Yes
#Mutable                   No                   Yes
#Hetrogeneous              Yes                  Yes
#----------------------------------------------------------------------------

def main():
    Data1 = [10,3.14,True,"Pune"]  # List
    Data2 = (10,3.14,True,"Pune")  # Tuple

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