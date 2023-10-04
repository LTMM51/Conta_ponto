from equipes import equipes

dic1 = {}

relatorio = 185
bateria_atual = 2
CPreal = 15
CPprevisto = 9.1
PVreal = 5.5
PVprevisto = 5.3
t = 60

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
        
Pcp = 12.5 * CPreal

FPV = max(0.8, 1.1 -15 * ((PVprevisto - PVreal)/PVprevisto)**2)

FPR = min(1, 0.5+ 0.9*relatorio/185)

Pvoo = FPV * FPR * Pcp

Pac = max(0, 30 - 830 * (abs((CPprevisto-CPreal)/CPprevisto))**1.75)

Brc = (min(20, 40-t/3) if t<120 else 0)

pontos = Brc + Pac + Pvoo  + CPreal

rodadas_nois = [pontos]

if bateria_atual >1:
    for bate in range(1,bateria_atual):
        rodadas_nois.append(equipes[34][bate])
        rodadas_nois.sort()
try:
    BCFnosso = 20*(1-(5*(rodadas_nois[-1]-rodadas_nois[-2])/rodadas_nois[-1])**2)
    BCFnosso = (BCFnosso if BCFnosso>0 else 0)
    print(rodadas_nois[-1])
    print(rodadas_nois[-2])
    print(BCFnosso)
except:
    BCFnosso = 0

pontos+=BCFnosso

dic1[34] = sum(rodadas_nois) - equipes[34]["penalidade"] + equipes[34]["bonificacao"]

podio = dict(reversed(sorted(dic1.items(), key=lambda item: item[1])))

times = []

for time in podio.keys():
    times.append(time)

print(f'Posição no podio com CP de {CPreal} é de: {times.index(34)+1}')
print(podio[34])

