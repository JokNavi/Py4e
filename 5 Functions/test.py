def computepay(h, r):
    if h > 40:
        over_hours = h - 40
        return (40 * r) + over_hours * (1.5 * r)
    else:
        return h * r

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)