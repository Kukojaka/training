def sweet_date(w1, r1, w2, r2, time_period):
    sweet_dates = 0

    for day in range(time_period):
        john_resting = day % (w1 + r1) >= w1
        anne_resting = day % (w2 + r2) >= w2

        if john_resting and anne_resting:
            sweet_dates += 1

    return sweet_dates
