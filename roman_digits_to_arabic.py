from collections import deque

class RomanNumerals:

    def to_roman(val):
        result = ""

        n_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                  100: 'C', 90: 'XC', 50: 'L', 40:'XL',  10: 'X',
                  9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        while val > 0:

            for num, symb in n_dict.items():
                if val >= num:
                    val -= num
                    result += symb
                    break

        return result


    def from_roman(roman_num):

        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums_lst = deque([roman_dict[n] for n in roman_num])

        result = 0

        while nums_lst:

            first_num = nums_lst.popleft()

            if nums_lst:
                second_num = nums_lst[0]

                if second_num > first_num:
                    result += second_num - first_num
                    nums_lst.popleft()

                else:
                    result += first_num
            else:
                result += first_num

        return result

