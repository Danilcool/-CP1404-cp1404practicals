"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_user_input = int(input("How many months? "))

    for month in range(1, months_user_input + 1):
        income = float(input(f"Enter income for month {month} "))
        incomes.append(income)

    generate_income_report(months_user_input, incomes)

def generate_income_report(months, incomes):
    """
    Generates an income report for the specified number of months
    and corresponding incomes.
    """
    report = []
    total = 0

    # Generate report for each month
    for i in range(months):
        month = i + 1
        income = incomes[i]
        total += income
        report.append(f"Month {month:2} - Income: ${income:,.2f} Total: ${total:,.2f}")

    # Print report
    header = "Income Report\n-------------"
    print(f"\n{header}\n" + "\n".join(report))


main()