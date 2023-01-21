def longest(a, b):
    return "".join(sorted(set(a).union(b)))

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))