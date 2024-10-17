# dynamic

def fibd(n,memory={}):
    if n==1:
        return 1
    elif n==0:
        return 0
    
    if n not in memory:
        memory[n] = fibd(n-1)+fibd(n-2)
    return memory[n]
print(fibd(5))
    

        
        

# recursive 
def fibr(n):
    
    if n <1 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-1)+fibr(n - 2)

