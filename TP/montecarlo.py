import numpy as np
import matplotlib.pyplot as plt

# C_thio+- 1%
# Vtot +- 1mL
# V0 +- 0,02 mL
# VE +- 0,04 mL




Vtot = 1
V0 = 0.010
VE = 0.0119
C_thio = 0.05


dVtot = 0.001
dV0 = 0.00002
dVE = 0.00004

# 1% de C_thio = +- 0.0005 mol/L
dC_thio = 0.0005


M_Cu = 63.55
resultats = []



valeur_ref = {"Vtot" : Vtot, "V0" : V0, "VE" : VE, "C_thio": C_thio }
valeur_inc = {"Vtot" : dVtot, "V0" : dV0, "VE" : dVE, "C_thio": dC_thio }
valeur_sim = {"Vtot" : Vtot, "V0" : V0, "VE" : VE, "C_thio": C_thio }


def titrage():

    for val in valeur_ref:
        ref = valeur_ref[val]
        inc = valeur_inc[val]
        sim = np.random.uniform(ref-inc, ref+inc)

        #print(f'{val} is {sim}'print)
        valeur_sim[val] = sim

    #valeur sim est rempli, on peut calculer m_Cu
    Vtot = valeur_sim['Vtot']
    V0 = valeur_sim['V0']
    VE = valeur_sim['VE']
    C_thio = valeur_sim['C_thio']
    
    #print(valeur_sim)
    m_Cu = Vtot*C_thio *VE * M_Cu / V0

    return m_Cu


def simulation(N):
    for i in range(N):
        m = titrage()
        resultats.append(m)    
       

    plt.hist(resultats)
    plt.show()
    moyenne = np.mean(resultats)
    ecartType= np.std(resultats)

    res = [moyenne, ecartType]

    return res

def main():
    #print(titrage())
    print(simulation(30))
    
# sim 3 : [3.7931249389294877, 0.028771527598080722]
# sim 30: [3.778433698519907, 0.023376185389182305]
# Entry point of the script.
if __name__ == "__main__":
    main()
