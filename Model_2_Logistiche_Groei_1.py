"""
-- Model 2 --

Program      : Exponential growth with R-value
Author       : Lucas & Lorenzo
Created      : March 2, 2022
"""

import matplotlib.pyplot as plt

N = 1000                   # De bevolkingsgrootte
I_init = 1                 # Het aantal besmette personen op t = 0
S_init = N - I_init        # Het aantal vatbare personen op t = 0

t_init = 0
t_end = 100                # De simulatie loopt tot 100 dagen na het begin
Dt = 1/1000                # Tijdstap van 1/1000 dag
nsteps = int(round((t_end-t_init)/Dt)) # Totaal aantal tijdstappen

Rwaarde = 1.93             # Het reproductiegetal; aantal mensen dat iemand gemiddeld besmet
Tb = 7

t_lst = [t_init] + [0] * nsteps
I_lst = [I_init] + [0] * nsteps
S_lst = [S_init] + [0] * nsteps

for i in range(1, nsteps+1):        # Eulers methode
    t = t_lst[i-1]
    I = I_lst[i-1]
    S = S_lst[i-1]

    dIdt = Rwaarde/Tb * I*(1-I/N)    # De verandering in het aantal besmette mensen
    dSdt = -Rwaarde/Tb * I*(1-I/N)   # De verandering in het aantal vatbare mensen
    
    t_lst[i] = t + Dt
    I_lst[i] = I + dIdt * Dt
    S_lst[i] = S + dSdt * Dt
    
# Het maken van een grafiek:
f = plt.figure(dpi=150)
plt.plot(t_lst, I_lst)
plt.plot(t_lst, S_lst, ":")
plt.grid(True)
plt.legend(["Geïnfecteerd", "Vatbaar"])
plt.xlabel('Tijd (dagen)')
plt.ylabel('Aantal mensen')
plt.title('Verloop van COVID-19-besmettingen')
plt.show()