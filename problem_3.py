def is_leap(year):
    leap = False
    if year<1900 and pow(10,5)<year:
        return leap
    if year%400 == 0:
        leap = True
        return leap
    if year%100==0:
        leap = False
    elif year%4==0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))