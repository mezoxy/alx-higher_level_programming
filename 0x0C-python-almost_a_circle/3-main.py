#!/usr/bin/python3
""" Doc """


from models.square import Square


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
