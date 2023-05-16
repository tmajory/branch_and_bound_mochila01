def RelaxacaoLinearMochila01(lucros, pesos, capacidade):
 
    TOL = 1e-6
    n = len(lucros)
 
    b = 0 # capacidade ja utilizada
    sol = dict() # solucao parcial da relaxao linear
    vfobj = 0    # valor da funcao objetivo
    indices = list(range(n)) # indices de variaveis livres
        
    if b > capacidade:
        return (vfobj, sol, False)
    
    criterio = [(lucros[i]/pesos[i], i) for i in indices]
    criterio.sort(key=lambda x: x[0], reverse=True)
    
    for (f,i) in criterio:
        if b + pesos[i] <= capacidade:
            sol[i] = 1
            vfobj += lucros[i]
            b += pesos[i]
        elif capacidade > b + TOL:
            sol[i] = (capacidade-b)/pesos[i]
            vfobj += lucros[i]*sol[i]
            b = capacidade
            break
    
    return (vfobj, sol, True)
 
#---------------------------------------------------------------------
# Exemplo de problema da mochila 0-1
L = [45, 48, 35, 51, 21]
P = [5, 8, 3, 5, 3]
C = 12
 
(zRL, solRL, viavelRL) = RelaxacaoLinearMochila01(L, P, C)
 
print(zRL)