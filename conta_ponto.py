from equipes import equipes

dic1 = {}

bateria_atual = 1
CPreal = 0
CPprevisto = 0
PVreal = 0
PVprevisto = 0

for eqp in range(1, len(equipes)+1):
    equipe = []
    if eqp != 34:
        for bat in range(1,8):
            equipe.append(equipes[eqp][bat])
            equipe.sort()
        try:
            BCF = 20*(1-(5*(equipe[-1]-equipe[-2])/equipe[-1])**2)
        except:
            BCF = 0
        dic1[eqp] = sum(equipe) + (BCF if BCF>0 else 0) - equipes[eqp]["penalidade"] + equipes[eqp]["bonificacao"]




podio = dict(reversed(sorted(dic1.items(), key=lambda item: item[1])))

print(podio)

