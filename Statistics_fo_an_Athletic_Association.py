def stat(strg):
    
    # ''
    if strg == '':
        return("")
    
    #from hhmmss to sec
    arr = strg.split(', ')
    arrall = []
    for n in range(0, len(arr)):
        l = str(arr[n]).split('|')
        arrall.append(int(l[0])*60*60+ int(l[1])*60+ int(l[2]))
    # sorting list using nested loops
    for i in range(0, len(arrall)):
        for j in range(i+1, len(arrall)):
            if arrall[i] >= arrall[j]:
                # temporary variable
                temp = arrall[i]
                arrall[i] = arrall[j]
                arrall[j] = temp
                
    # range, average
    sec_range = arrall[len(arrall)-1]-arrall[0]
    sec_average = sum(arrall)//len(arrall)
    #median
    if (len(arrall)%2) == 1:
        sec_median = arrall[len(arrall)//2]
    else:
        sec_median = ( arrall[len(arrall)//2-1]+arrall[len(arrall)//2] )//2
    
    #from sec to hhmmss
    r = [sec_range//3600, sec_range%3600//60, sec_range%3600%60]
    a = [sec_average//3600, sec_average%3600//60, sec_average%3600%60]
    m = [sec_median//3600, sec_median%3600//60, sec_median%3600%60]
    
    # from 'x|x|xx' to '0x|0x|xx'
    for i in range(0, 3):
        if r[i]//10==0:
            r[i] = '0'+ str(r[i])
        if a[i]//10==0:
            a[i] = '0'+ str(a[i])
        if m[i]//10==0:
            m[i] = '0'+ str(m[i])
    #merge
    range_r = str(r[0]) + '|'+ str(r[1])+ '|'+ str(r[2])
    average_r = str(a[0])+ '|'+ str(a[1])+ '|'+ str(a[2])
    median_r = str(m[0])+ '|'+ str(m[1])+ '|'+ str(m[2])
    
    #result
    result = 'Range: '+ range_r+ ' '+ 'Average: '+ average_r+ ' '+ 'Median: '+ median_r
    return(str(result))
