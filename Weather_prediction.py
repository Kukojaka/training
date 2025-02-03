def weather_prediction(days, weather_today, final_weather, P):
    print(days, weather_today, final_weather)
    
    A = [P[weather_today]]
    B = P
    
    for n in range (1, days ):
        result = [[sum(a * b for a, b in zip(A_row, B_col)) 
                            for B_col in zip(*B)]
                                    for A_row in A]
        A = result

    r = A[0][final_weather]
    return(r)
