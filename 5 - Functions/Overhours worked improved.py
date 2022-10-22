#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
def computepay(hours, rate):
    if hours > 40.0:
        over_hours = hours - 40.0
        return (40 * rate) + over_hours * (1.5 * rate)
    else:
        return hours * rate
    
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = computepay(hours, rate)
    print('Pay: ' + str(pay))
except:
    print('Error, please enter numeric input')

