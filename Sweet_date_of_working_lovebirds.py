def sweet_date(w1, r1, w2, r2, time_period):
  
    arr1 = []
    arr2 = []
  
    for i in range(0, w1):
        arr1.append('work')
    for i in range(0, r1):
        arr1.append('rest')
        
    for i in range(0, w2):
        arr2.append('work')
    for i in range(0, r2):
        arr2.append('rest')
    
    arr_new1 = []
    arr_new2 = []
    for i in range(0, time_period):
        arr_new1.append(arr1[i%len(arr1)])
        arr_new2.append(arr2[i%len(arr2)])

    n = 0
    for i in range(0, len(arr_new1)):
        if arr_new1[i] == arr_new2[i] == 'rest':
            n = n+1
    return(n)
