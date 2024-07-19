def bank(X, Y):
    for _ in range(Y):
        X += X * 0.10
    return X


initial_amount = 1000000  
years = 5             

final_amount = bank(initial_amount, years)

print(f"Сумма на счету пользователя спустя {years} лет: {final_amount:.2f} рублей")