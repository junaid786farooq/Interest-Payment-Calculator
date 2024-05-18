# Monthly interest payment loan calculator

def main():
    print("This is a monthly payment loan calculator.")

    # Input loan details
    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = float(input("Enter amount of years: "))
    
    # Calculate monthly interest rate and the number of months
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12

    # Calculate monthly payment using the formula for an annuity
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (- amount_of_months))

    # Display the result
    print(f"The monthly payment for this loan is: ${monthly_payment:.2f}" )

# Run the main function
if __name__ == "__main__":
    main()