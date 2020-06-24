#COS-205_assignment1_MC.py
#   This is a program will return the future value of a principle sum of money
#   given the inputs of principle amount, yearly interest rate, number of compounding periods per year
#   and number of years.
#by: Mike Crowley

def main():
    print("This program will calculate the future value of your investment")
    print("based on the originating amount in dollars, yearly interest rate,")
    print("compounding periods per year, and total years.")
    print(" ")

    principle = eval(input("Please enter the principle amount of your investment without a monetary indicator: "))
    interest_rate = eval(input("Please enter the yearly interest rate expected of your investment as a decimal value: "))
    compounding_periods = eval(input("Please enter the number of compounding periods per year: "))
    investment_duration = eval(input("Please enter the total duration of your investment in years: "))

    for i in range(investment_duration):
        principle = principle * (1 + interest_rate/compounding_periods)**compounding_periods

    print(" ")
    print("The value of your initial investment in", investment_duration, "years will be: $", round(principle, 2))

main()