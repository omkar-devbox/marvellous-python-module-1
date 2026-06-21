def Area(Redius,PI):
    Ans = PI * Redius * Redius
    return Ans


def main():
    Rect = Area(PI=3.14,Redius=10.5)
    print("Area Of Circle is :",Rect)



if __name__ == "__main__":
    main()
else:
    print("Error")