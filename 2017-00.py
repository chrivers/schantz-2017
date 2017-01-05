#!/usr/bin/python3

initial_year    = 2016
initial_reserve = 0.0

small_payment = 10000.0
large_payment = 20000.0
large_payment_start = 2030

small_customer_fee = 1000.0
small_customer_limit = 200000.0

interest_pal_fee = 0.1530
interest_rate = 0.01

payment_fee = 0.1100

def calc_year(year):
    if year == initial_year:
        return initial_reserve
    else:
        Rn_last = calc_year(year - 1)
        if year >= large_payment_start:
            I = large_payment
        else:
            I = small_payment
        Opct = I * payment_fee
        if Rn_last > small_customer_limit:
            Oabs = 0
        else:
            Oabs = small_customer_fee
        r = interest_rate * (Rn_last + I - Opct - Oabs)
        PAL = interest_pal_fee * r
        res = Rn_last + I - Opct - Oabs + r - PAL
#        print("Rn_last(%.2f) + I(%.2f) - Opct(%.2f) - Oabs(%.2f) + r(%.2f) - PAL(%.2f)" % (Rn_last, I, Opct, Oabs, r, PAL))
        return res

for year in range(2016, 3000):
    amount = calc_year(year)
    print("%d\t%.6f" % (year, amount))
    if amount > 1000000.0:
        break
