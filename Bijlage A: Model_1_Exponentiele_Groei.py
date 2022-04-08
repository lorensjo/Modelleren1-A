"""
-- Simpel Model van COVID-19 volgens exponentiele groei -- 

Program      : Exponential growth with R-value
Author       : Lucas & Lorenzo
Created      : March 2, 2022
"""
import math
import matplotlib.pyplot as plt

# Voor dit model definiëren we allereerst de initiële waarden en constanten
I_init = 10                      # Het aantal geïnfecteerden op tijdstip t = 0
t_init = 0                       # Het model begint op t = 0
t_end = 100                      # Het model rekent tot t = t_end
Dt_s =  [1, 1/10, 1/100]         # Dt is de tijdstap waarmee het model rekent. 
                                 #Hoe kleiner Dt, hoe preciezer het model. 

R = 1.93                         # Het reproductiegetal
Tb = 7                           # Periode van ziekte

def NumeriekeMethode(I_init, t_init, t_end, Dt, R, Tb): 
    nsteps = int(round((t_end-t_init)/Dt))  # Het totaal aantal tijdstapjes van lengte
                                            # Dt dat het model moet nemen
                                            
    # Hier worden voor t en I lijsten aangemaakt om de waardes bij te houden. 
    # De initiele waarden worden er alvast in gezet.
    t_lst = [t_init] + [0] * nsteps
    I_lst = [I_init] + [0] * nsteps    # Waardes van het numeriek model
    
    # Nu gaat het model nsteps-1 stapjes maken zodat bij ieder tijdstip de waarde
    # van I op wordt berekend en aan de lijst wordt toegevoegd
    for i in range(1, nsteps+1):
        # Hier worden de waarden van t en I op het vorige tijdstip opgehaald
        t = t_lst[i-1]
        I = I_lst[i-1]
        
        dIdt = R/Tb * I       # Dit is de differentiaalvergelijking
        
        # Hier worden de nieuwe waarden van t en I op het huidige tijdstip toegevoegd
        t_lst[i] = t + Dt
        I_lst[i] = I + dIdt * Dt
    return I_lst, t_lst

def AnalytischeMethode(I_init, t_init, t_end, R, Tb):
    Dt = 1/1000
    nsteps = int(round((t_end-t_init)/Dt))  # Het totaal aantal tijdstapjes van lengte
                                            # Dt dat het model moet nemen
    A_lst = [I_init] + [0] * nsteps    # Waardes van het analytische model
    t_lst = [t_init] + [0] * nsteps
    for j in range(1, nsteps+1):
        t = t_lst[j-1]
        
        A_lst[j] = I_init * (math.e)**(R/Tb * t)
        t_lst[j] = t + Dt
    return A_lst, t_lst


A_lst, t_lstA = AnalytischeMethode(I_init, t_init, t_end, R, Tb)
I1_lst, t_lst1 = NumeriekeMethode(I_init, t_init, t_end, Dt_s[0], R, Tb)
I2_lst, t_lst2 = NumeriekeMethode(I_init, t_init, t_end, Dt_s[1], R, Tb)
I3_lst, t_lst3 = NumeriekeMethode(I_init, t_init, t_end, Dt_s[2], R, Tb)


f = plt.figure(dpi=150)  # Dit is om de resolutie van de grafiek te verhogen
f.set_figwidth(10)
f.set_figheight(10)

plt.plot(t_lstA, A_lst, color="r")
plt.plot(t_lst1, I1_lst, '--')
plt.plot(t_lst2, I2_lst, ':')
plt.plot(t_lst3, I3_lst, '-.')

plt.grid(True)
plt.title("Vergelijking Analytisch en Numeriek Model")
plt.xlabel("Tijd (dagen)")
plt.ylabel("Aantal besmettingen")
plt.legend(["Analytisch", "Numeriek Dt = 1", "Numeriek Dt = 1/10", "Numeriek Dt = 1/100", "Numeriek Dt = 1/1000"])
plt.yscale('log') 

plt.show() 
    
    
