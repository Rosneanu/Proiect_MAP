import matplotlib.pyplot as plt # Bibliotecă pentru crearea de grafice. Este folosită pentru a reprezenta vizual temperaturile orare.
import numpy as np # Bibliotecă pentru calcul numeric eficient. Este utilizată pentru a crea un vector de ore.
import requests # Bibliotecă folosită pentru a trimite cereri HTTP către un API (interfață de programare a aplicațiilor).
from tkinter import messagebox # Bibliotecă pentru afișarea de mesaje grafice (popup), utilizată pentru a afișa mesaje grafice, de exemplu, notificări în cazul unei erori

# Coordonatele pentru Bacau România, sunt reprezentate de (latitudine și longitudine) si sunt salvate în variabile
latitude = 46.56718
longitude = 26.91384

# URL-ul API-ului Open-Meteo pentru prognoza meteo, url conține adresa API-ului Open-Meteo pentru prognoza meteo. Tilizeaza f-string pentru a înlocui variabilele latitude și longitude în URL.
# latitude și longitude: Coordonatele locației
# hourly=temperature_2m: Solicită temperaturile orare la 2 metri deasupra solului
# start=2024-11-24 și end=2024-11-25: Specifică intervalul de timp pentru prognoză
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days=1"

# Solicitarea datelor de la API
try:
    response = requests.get(url) # Trimite o cerere GET la API-ul Open-Meteo pentru a obține datele
except:
    messagebox.showinfo("Nu am reușit să accesez API-ul. ") # Dacă cererea nu poate fi trimisă, de exemplu, din cauza unei probleme de conexiune, este afișat un mesaj popup

if response.status_code == 200: # verifică dacă cererea a fost procesată cu succes (200 înseamnă "OK").
    data = response.json() # extrage datele din răspunsul API sub formă de obiect JSON.
    # Extrage temperaturile orare
    temperatures = data['hourly']['temperature_2m'] # Datele JSON conțin un dicționar cu mai multe informații, iar acest cod extrage temperaturile orare din câmpul hourly -> temperature_2m
    # Generează un vector de timp pentru orele din zi
    hours = np.arange(0, len(temperatures))  #creează un vector cu valori de la 0 până la len(temperatures) (numărul de ore pentru care există date)
    
    # Trasează datele
    plt.plot(hours, temperatures, marker='o') # creează graficul, cu orele pe axa X și temperaturile pe axa Y. Marker-ul 'o' reprezintă punctele de pe grafic
    plt.title('Temperatura orară în Bacau pentru 24 noiembrie 2024') # setează titlul graficului
    plt.xlabel('Prognoza pe ore') # etichetează axele
    plt.ylabel('Temperatura (°C)') # etichetează axele
    plt.grid(True) # adaugă o grilă pe fundal pentru a face graficul mai ușor de citit
    plt.show() # afișează graficul
