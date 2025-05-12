def split_into_installments(total, round_to, parts=3):
    base = total // parts
    base = round(base / round_to) * round_to

    installments = [base] * parts
    current_sum = sum(installments)
    difference = total - current_sum
    installments[-1] += difference
    return installments


total_fee = 79000
installments = split_into_installments(total_fee, 500)

print("Installment breakdown:")
for i, amount in enumerate(installments, 1):
    print(f"Installment {i}: tk {amount}")

print(f"Total: {installments[0]} + {installments[2]} + {installments[2]} = {sum(installments)} tk")

