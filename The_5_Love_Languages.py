from preloaded import LOVE_LANGUAGES

def love_language(partner, weeks):
    
    l = ['words', 'acts' , 'time', 'touch', 'gifts']
    s = [0, 0, 0, 0, 0]
    
    for n in range (0, weeks*7 - (weeks*7%5)) :
        k = n%5
        
        if partner.response(l[k]) == 'positive':
            s[k] = s[k] + 1
            
    print(s)
    print(l[s.index(max(s))])
        
    return l[s.index(max(s))]
