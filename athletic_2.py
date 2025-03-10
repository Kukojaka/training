from statistics import mean, median
def stat(strg):
    if not strg: return ''
    s = [sum(x * y for x,y in zip([3600, 60, 1], map(int, i.split('|')))) for i in strg.split(', ')]
    f = lambda x: f'{int(x//3600):02}|{int(x%3600//60):02}|{int(x%60):02}'
    return f'Range: {f(max(s) - min(s))} Average: {f(mean(s))} Median: {f(median(s))}'
