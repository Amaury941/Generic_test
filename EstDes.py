### algoritmo para estatística descritiva ###
n_classes = 5
dados = [985, 801, 1349, 1562, 1600, 1606, 1510, 959, 822, 1321, 1263, 1162, 1406, 1421,1248, 1204, 1000, 683, 1650, 1927, 1543, 981, 986, 1416, 1985, 506, 431, 
            1167,1098, 1096, 1501, 1360, 1526, 1550, 1708, 1005, 1623, 1712, 1530, 1605, 1538, 1746, 1472, 1589, 1913, 1815, 2115, 2475, 2927, 1635, 1812, 1107, 
            1450, 1917, 1807, 1461, 1969, 2402, 1446, 1851, 2134, 1685, 1944, 2077, 605, 1872, 2133,1891, 623, 1977, 2132, 2417, 2046, 2056, 2192, 2744, 3239, 
            3117, 2471, 2077]
def amplitude_dados(dados):  return max(dados) - min(dados)

def amplitude_classe(amplitude_dados,n_classes): return round(amplitude_dados/n_classes)

def definir_limites(dados,n_classes,amplitude_classe):
    limites = {str(min(dados)):0}
    for i in range(n_classes):
        limites.update({int(list(limites)[i])+amplitude_classe:0})
    del limites[str(min(dados))]
    return limites

def fill (data,limites,n=0):
    if data < int(list(limites)[n]):
        limites[list(limites)[n]] += 1
        return limites
    if n+1<len(limites):
        fill (data,limites,n+1)

def fill_limits(limites,dados):
    for data in dados:
        fill(data,limites)

def string_frequencies(limites,dados):
    print ('frequências')
    x = [min(dados)]+list(limites)
    for n in range(1,len(x)):
        print ('%i-%i : %i'%(x[n-1],x[n]-1,limites[ (x[n]) ]))

def string_Relatives_frequencies(limites,dados):
    print ('frequências relativas')
    x = [min(dados)]+list(limites)
    for n in range(1,len(x)):
        print ('%i-%i : %.3f%s'%(x[n-1],x[n]-1,(limites[ (x[n]) ]/len(dados))*100,'%' ))



limites = definir_limites(dados,n_classes,amplitude_classe(amplitude_dados(dados),n_classes))

fill_limits(limites,dados)
print (limites)
string_frequencies(limites,dados)
string_Relatives_frequencies(limites,dados)