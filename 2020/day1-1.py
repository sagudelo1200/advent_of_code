from expense_report import expense_report

for r in expense_report:
    search_value = 2020 - r
    if search_value in expense_report:
        print(r * search_value)
