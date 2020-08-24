import numpy as np

# Method 01
# assume annual interest of 10%
interest = 10
annual_rate = interest/100.0
monthly_rate = annual_rate/12
# assume payment over 10 years
years = 10
number_month = years * 12
# assume a loan value of 1000 rupees
loan_value = 1000000
monthly_payment = abs(np.pmt(monthly_rate, number_month, loan_value)) # this function is deprecated.
print("Monthly Payment will be : {}".format(monthly_payment))


# Method 02 - Will be supported in future also 
import numpy_financial as npf

print("Monthly Interest Payment: {}".format(abs(npf.pmt(monthly_rate, number_month, loan_value))))
