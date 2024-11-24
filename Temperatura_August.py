import matplotlib.pyplot as plt # acest modul este utilizat pentru crearea graficelor 2D
import numpy as np              # este o bibliotecă pentru manipularea datelor numerice (ex. matrici, funcții matematice)


# Importăm versiunea matplotlib
import matplotlib # importă biblioteca principală matplotlib
print("Matplotlib version:", matplotlib.__version__) # afișează versiunea instalată a acesteia, astfel încât să știm ce versiune folosim

# Simularea datelor de temperatură zilnică
zile = np.arange(1, 20) # creează un șir de numere întregi de la 1 la 19 (inclusiv). Acestea reprezintă zilele lunii august
temperatura = np.random.normal(loc=25, scale=5, size=len(zile)) # Generează un șir de temperaturi folosind o distribuție normală (Gauss),
                                                                # loc=25: media temperaturilor este 25°C, 
                                                                # #scale=5: deviația standard este 5°C (valorile fluctuează în jurul mediei),
                                                                # size=len(zile): lungimea vectorului de temperaturi este egală cu numărul de zile (19)

# Trasează datele
plt.plot(zile, temperatura, marker='o') # creează un grafic linie folosind valorile din zile pentru axa X și valorile din temperatura pentru axa Y
                                        # marker='o': fiecare punct este reprezentat cu un marker de tip cerc (o)
plt.title('Temperatura pe ore') # adaugă titlul graficului
plt.xlabel('Zile') # etichetează axa X cu "Zi"
plt.ylabel('Temperatura (°C)') # etichetează axa Y cu "Temperatura (°C)"
plt.grid(True) # activează grila pe grafic pentru o mai bună lizibilitate

# Show the plot
plt.show()

