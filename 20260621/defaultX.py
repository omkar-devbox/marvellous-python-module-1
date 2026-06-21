def Area(PI=3.14,Redius): #Error Deful Argument Always last(last la define karne)
    Ans = PI * Redius * Redius
    return Ans


def main():
    Rect = Area(Redius=10.5)
    print("Area Of Circle is :",Rect)

    Rect = Area(PI=7.12,Redius=10.5)
    print("Area Of Circle is :",Rect)



if __name__ == "__main__":
    main()
else:
    print("Error")