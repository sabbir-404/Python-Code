def split_into_installments(total, parts=3, round_to=100):
    base = total // parts
    base = round(base / round_to) * round_to

    installments = [base] * parts
    current_sum = sum(installments)
    difference = total - current_sum

    # Adjust the last installment to match the total exactly
    installments[-1] += difference

    return installments

# Example usage
total_fee = 55000
installments = split_into_installments(total_fee)

print("Installment breakdown:")
for i, amount in enumerate(installments, 1):
    print(f"Installment {i}: tk {amount}")

print(f"Total: tk {sum(installments)}")
