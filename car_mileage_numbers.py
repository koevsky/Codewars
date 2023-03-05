def is_interesting(number, awesome_phrases):

    def zeros_test(num):
        num = str(num)
        return num == num[0] + (len(num)-1) * "0"

    def same_number_test(num):
        return len(set(str(num))) == 1

    def incrementing_test(num):
        num = str(num)

        if num.endswith("90") and len(num) == len(set(num)):
            num = num[:len(num)-1]

        return all(int(x)+1 == int(y) for x, y in zip(num, num[1:]))

    def decrementing_test(num):
        num = str(num)
        return all(int(x) == int(y) + 1 for x, y in zip(num, num[1:]))

    def palindrome_test(num):
        num = str(num)
        return num == num[::-1]

    def awesome_phrases_test(num):
        return num in awesome_phrases

    for x in range(3):

        n = number + x
        if len(str(n)) >= 3:
            result = any([zeros_test(n), same_number_test(n), incrementing_test(n),
                      decrementing_test(n), palindrome_test(n), awesome_phrases_test(n)])

            if x == 0 and result:
                return 2

            elif x in [1, 2] and result:
                return 1

    else:
        return 0