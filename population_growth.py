def nb_year(p0, percent, aug, p):
    total_years = 0
    while p0 < p:
        p0 += int(p0 * percent/100 + aug)
        total_years += 1

    return total_years

print(nb_year(1500000, 2.5, 10000, 2000000))
