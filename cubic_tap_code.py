letters_dict = {"A": [1, 1, 1], "B": [2, 1, 1], "C": [3, 1, 1],
                "D": [1, 2, 1], "E": [2, 2, 1], "F": [3, 2, 1],
                "G": [1, 3, 1], "H": [2, 3, 1], "I": [3, 3, 1],

                "J": [1, 1, 2], "K": [2, 1, 2], "L": [3, 1, 2],
                "M": [1, 2, 2], "N": [2, 2, 2], "O": [3, 2, 2],
                "P": [1, 3, 2], "Q": [2, 3, 2], "R": [3, 3, 2],

                "S": [1, 1, 3], "T": [2, 1, 3], "U": [3, 1, 3],
                "V": [1, 2, 3], "W": [2, 2, 3], "X": [3, 2, 3],
                "Y": [1, 3, 3], "Z": [2, 3, 3], " ": [3, 3, 3]}


def encode(text):

    final_res = []

    for l in text:

        part_1, part_2, part_3 = letters_dict[l][0] * ".", letters_dict[l][1] * ".", letters_dict[l][2] * "."
        encoded = f"{part_1} {part_2} {part_3}"
        final_res.append(encoded)

    return " ".join(final_res)

def decode(dots):

    dots = dots.split()

    final_res = ""

    nums = []

    for d in dots:
        nums.append(d)

        if len(nums) == 3:
            nums[0], nums[1], nums[2] = len(nums[0]), len(nums[1]), len(nums[2])

            letter = list(letters_dict.keys())[list(letters_dict.values()).index(nums)]
            final_res += letter
            nums.clear()

    return final_res


print(encode("N"))

print(encode("TEST"))

print(decode(".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. ."))