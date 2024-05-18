# Monthly Interest Payment Loan Calculator

This is a Python program that calculates the monthly payment for a loan based on the loan amount, annual interest rate, and the number of years. The program uses the formula for an annuity to compute the monthly payments.

## Features

- Calculates monthly loan payments.
- Takes user inputs for loan amount, annual interest rate, and loan duration in years.
- Displays the monthly payment amount.

## How to Use

1. **Run the Program:**
   - Execute the script in a Python environment.

2. **Input Instructions:**
   - The program will prompt you to enter the loan amount (principal).
   - Enter the annual interest rate (APR) as a percentage (e.g., 5 for 5%).
   - Enter the loan duration in years.

3. **Output:**
   - The program will calculate and display the monthly payment amount.

## Example

This is a monthly payment loan calculator.<br>
Enter the loan amount: 10000<br>
Enter the annual interest rate: 5<br>
Enter amount of years: 5<br>
The monthly payment for this loan is: $188.71

## Formula Used

The program calculates the monthly payment using the formula for an annuity:

\[ \text{Monthly Payment} = \frac{P \times r}{1 - (1 + r)^{-n}} \]

Where:
- \( P \) is the loan amount (principal).
- \( r \) is the monthly interest rate (annual interest rate divided by 12 and then by 100).
- \( n \) is the number of monthly payments (years multiplied by 12).

## Requirements

- Python 3.x

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
