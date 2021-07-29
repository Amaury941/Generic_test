''' algoritmo para distribuições de probabilidades Discretas  '''

def fatorial(num,fatorial=1):
	if num == 0: num = 1
	for n in range (num):
		fatorial = fatorial * (n+1)
	return fatorial

def probabilidade_binomial (n,p,q,x):
	return (fatorial(n)/(fatorial(n-x)*fatorial(x)))*(p**x)*(q**(n-x))

x = 2    # valor a ser buscado
n = 3    #frequência das ocorrências

#distribuição de bernoulli
p = 0.75 #probabilidade de sucesso
q = 1-p  #probabilidade de falha
s2 = p*q # variância VAR(X)
x_ = p # Média E(x)

print(probabilidade_binomial(n,p,q,x))


#### Ex uma urna tem 30 bolas brancas e 20 verdes
# retira-se uma bola. Seja X o número de bolas verdes
# calcule E(X) e VAR(X)
# total de bolas = 50
# bolas brancas = 30/50
# bolas verdes = 20/50
# x_ = p = E(x) = 20/50 = 2/5 = 0.4
# s2 = p*q = VAR(x) = x_*30/50 = 60/250 = 0.24