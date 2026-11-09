n = int(input())

if n <= 0:
    print("Невалиден брой")
else:
    multiples_of_three = 0
    positive_sum = 0
    positive_count = 0

    for _ in range(n):
        number = int(input())

        if number % 3 == 0:
            multiples_of_three += 1

        if number > 0:
            positive_sum += number
            positive_count += 1

    print(f"Кратни на 3: {multiples_of_three}")

    if positive_count == 0:
        print("Няма положителни")
    else:
        average = positive_sum / positive_count
        print(f"Средна стойност на положителните елементи: {average:.2f}")
