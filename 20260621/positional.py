def Area(Redius,PI):
    Ans = PI * Redius * Redius
    return Ans


def main():
    Rect = Area(10.5,3.14)
    print("Area Of Circle is :",Rect)

    Rect = Area(13.6,7.12)
    print("Area Of Circle is :",Rect)


if __name__ == "__main__":
    main()
else:
    print("Error")