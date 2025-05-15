import random
import array as arr
class GeneticAlgorithm(object):
    
    def __init__(self):
        pass
    
    def generate(self, length):
        chr = ""
        for i in range(length):
            temp = str(random.randint(0, 1))
            chr += temp	
        return(str(chr))
    
    def select(self, population, fitnesses):
        population = ['101', '100', '010']
        fitnesses = [2, 3, 1]
        summ = 0
        propabilities = []
        for i in range (0, len(fitnesses) - 1):
            summ = summ + fitnesses[i]
        for i in range (0, len(fitnesses)):
            propabilities.append(fitnesses[i]/ summ)
        print(propabilities)
        
        random.choice(list())
        return None

    def mutate(self, chromosome, p_m):          
        p = int(random.randint(0, 1000)) 
        new_chr = chromosome
        if p <= (p_m*1000) :
            k = int(random.randint(0, len(chromosome)-1))
            print('k = ', k)
            print('k element = ', chromosome[k])
            chr = chromosome        
            if chromosome[k] == '0' :
                new_chr = chr[:k] + '1' + chr[k+1:]
                print(new_chr)
            else :
                new_chr = chr[:k] + '0' + chr[k+1:]
                print(new_chr)             
        return(str(new_chr))     
    
    def crossover(self, chromosomes, p_c):
        p = int(random.randint(0, 100)) 
        new_chr = chromosomes
        chr = chromosomes[0]
        chr_2 = chromosomes[1]
        print(chr, chr_2)
        if p <= (p_c*100) :
            k = int(random.randint(0, len(chromosomes[0])-1))
            print('k = ', k)
            print('k element 1st chromosome= ', chromosomes[0][k])        
            new_chr = chr[:k] + chr_2[k:]
        print(new_chr)             
        return(str(new_chr)) 
    
    def run(self, fitness, length, p_c, p_m, iterations):
        return None
    
    pop = []
    for i in range(0, 4):
        pop.append(generate(1, 10))
    print(pop)
    
    
    crossover(1, ['11111111', '00000000'], 1)
            
        
