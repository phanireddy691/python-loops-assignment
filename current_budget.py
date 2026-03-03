current_budget = 100.00

def reset_budget():
    current_budget = 500.00
    print(f"Budget reset to {current_budget}")

reset_budget()
print(f"Main program sees: {current_budget}")