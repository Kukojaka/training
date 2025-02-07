from preloaded import LOVE_LANGUAGES

def love_language(partner, weeks):
    
    l = ['words', 'acts' , 'time', 'touch', 'gifts']
    
    for n in range (0, 49):
        k = n%5
        print(k)
        
        print(l[k])
        print(partner.response(l[k]), weeks)
    return "words"
