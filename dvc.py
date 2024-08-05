def calculate(weekday, weekend, max_points=300):
    total_days = 0
    points = 0

    while True:
        for j in [5, 2]:
            if j == 5:
                day = weekday
            else:
                day = weekend
            for i in range(j):
                total_days += 1
                points += day
                if points + day > max_points:
                    return total_days, points


def calculate2(weekday, weekend, max_points=300):
    total_days = 0
    points = 0

    days = ([weekday] * 5 + [weekend] * 2) * 10

    i = 0
    for day in days:
        total_days += 1
        points += day
        if points + days[i + 1] > 300:
            return total_days, points
        i += 1


print(calculate(8, 10))
