from expense_report import expense_report

for val1 in expense_report:
    for val2 in expense_report:
        for val3 in expense_report:
            if val1 + val2 + val3 == 2020:
                print(val1 * val2 * val3)
