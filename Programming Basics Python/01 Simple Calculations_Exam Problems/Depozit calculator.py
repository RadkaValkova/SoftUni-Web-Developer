depozit_sum = float(input())
depozit_months = int(input())
lihven_procent = float(input())

final_sum = depozit_sum + depozit_months*((depozit_sum*(lihven_procent/100))/12)
print(final_sum)