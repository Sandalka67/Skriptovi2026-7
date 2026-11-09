first_number = int(input())

if first_number == 0:
    print("Няма данни")
else:
    minimum = first_number
    negative_count = 0
    increase_count = 0
    number_count = 0
    previous_number = None
    number = first_number

    while number != 0:
        number_count += 1
        if number < minimum:
            minimum = number
        if number < 0:
            negative_count += 1
        if previous_number is not None and number > previous_number:
            increase_count += 1

        previous_number = number
        number = int(input())

    negative_percentage = round(negative_count * 100 / number_coun

    print(f"Най-малко число: {minimum}")
    print(f"Брой нараствания: {increase_count}")
    print(f"Процент отрицателни числа: {negative_percentage}%")

    