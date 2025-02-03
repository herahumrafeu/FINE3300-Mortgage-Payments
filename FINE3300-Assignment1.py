print("Mortgage Calculator\n")

#answering first part of the assignment
def mortgage_payments(principal, rate, amortization):
    #changing quoted rate provided into decimal form
    rate /= 100

    #payments for different periods (no need to mention accelerated ones as they can just be calulated by dividing the monthly payment by 2 or 4)
    monthly_n = amortization * 12
    semi_monthly_n = amortization * 24
    bi_weekly_n = amortization * 26
    weekly_n = amortization * 52
   

    #rates for different periods (no need to mention accelerated ones as they can just be calulated by dividing the monthly payment by 2 or 4)
    monthly_r = (1 + rate / 2) ** (2 / 12) - 1
    semi_monthly_r = (1 + rate / 2) ** (2 / 24) - 1
    bi_weekly_r = (1 + rate / 2) ** (2 / 26) - 1
    weekly_r = (1 + rate / 2) ** (2 / 52) - 1

    #defining the payment formula and calculating the payments for different periods
    def payments (n, r):
        return principal * (r / (1 - (1 + r) ** -n))
    monthly_payment = payments(monthly_n, monthly_r)
    semi_monthly_payment = payments(semi_monthly_n, semi_monthly_r)
    bi_weekly_payment = payments(bi_weekly_n, bi_weekly_r)
    weekly_payment = payments(weekly_n, weekly_r)
   
    #calculating the accelerated payments
    accelerated_bi_weekly_payment = monthly_payment / 2
    accelerated_weekly_payment = monthly_payment / 4
    
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(accelerated_bi_weekly_payment, 2),
        round(accelerated_weekly_payment, 2),
    )


#asking the user to input the principal, rate and amortization period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted interest rate: "))
amortization = int(input("Enter the amortization period: "))

#payment calculations
payments = mortgage_payments(principal, rate, amortization)

#printing the results for the user
print(f"Monthly Payment: ${payments[0]:.2f}")
print(f"Semi-monthly Payment: ${payments[1]:.2f}")
print(f"Bi-weekly Payment: ${payments[2]:.2f}")
print(f"Weekly Payment: ${payments[3]:.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:.2f}")