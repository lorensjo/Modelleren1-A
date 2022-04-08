"""
-- Model 4 Deïmmunisate--

Program      : SIRD-model met deïmmunisatie
Author       : Lucas & Lorenzo
Created      : April 6, 2022
"""
import matplotlib.pyplot as plt

#N = 1000                   # De bevolkingsgrootte
I_init = 1                 # Het aantal besmette personen op t = 0
S_init = 999               # Het aantal vatbare personen op t = 0
R_init = 0   
D_init = 0   

ρ = 1/7
δ = 0.23/100
σ = 1/183

t_init = 0
t_end = 365*2              # De simulatie loopt tot 100 dagen na het begin
Dt = 1/1000                # Tijdstap van 1/1000 dag
nsteps = int(round((t_end-t_init)/Dt)) # Totaal aantal tijdstappen

Rw = 1.93            # Het reproductiegetal; aantal mensen dat iemand gemiddeld besmet


t_lst = [t_init] + [0] * nsteps
I_lst = [I_init] + [0] * nsteps
S_lst = [S_init] + [0] * nsteps
R_lst = [R_init] + [0] * nsteps
D_lst = [D_init] + [0] * nsteps

for i in range(1, nsteps+1):        # Eulers methode  
    t = t_lst[i-1]
    I = I_lst[i-1]
    S = S_lst[i-1]
    R = R_lst[i-1]
    D = D_lst[i-1]
    N = S + I + R  # levende bevolking

    dIdt =  Rw/7 * I*S/N - ρ * I    # De verandering in het aantal besmette mensen
    dSdt = -Rw/7 * I*S/N + σ* R     # De verandering in het aantal vatbare mensen
    dRdt = ρ * I * (1-δ)     - σ * R
    DDdt = δ * ρ * I
    
    t_lst[i] = t + Dt
    I_lst[i] = I + dIdt * Dt
    S_lst[i] = S + dSdt * Dt
    R_lst[i] = R + dRdt * Dt
    D_lst[i] = D + DDdt * Dt

# Het maken van een grafiek:
f = plt.figure(dpi=150)
plt.plot(t_lst, S_lst, "--") 
plt.plot(t_lst, I_lst)
plt.plot(t_lst, R_lst, ":")
plt.plot(t_lst, D_lst, "-.")

plt.grid(True)
plt.legend(["Vatbaar (S)", "Geïnfecteerd (I)", "Immuun (R)", "Overleden (D)"])
plt.xlabel('Tijd (dagen)')
plt.ylabel('Aantal mensen')
plt.title('Verloop van COVID-19-besmettingen')
plt.show()
