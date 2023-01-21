def square_digits(num):
    return int("".join(str(int(x)**2) for x in list(str(num))))

num = int(input())

print(square_digits(num))