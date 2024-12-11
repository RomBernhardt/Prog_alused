import tkinter as tk
from tkinter import messagebox
import random


def soovita_toidud(kalorid):
    """Soovitab toidud, et täita kalorivajadus. Lõpetab, kui kalorivajadus on täidetud."""
    kogus = 0
    valitud_toidud = []
    
    toidud = {
        "Leib": 250,
        "Sai": 290,
        "Piim (2,5%)": 50,
        "Kohv (must, ilma suhkruta)": 2,
        "Must tee (ilma suhkruta)": 1,
        "Juust": 350,
        "Vorst": 300,
        "Või": 720,
        "Muna": 155,
        "Suhkur": 400,
        "Müsli": 370,
        "Kartul": 85,
        "Makaronid (keedetud)": 110,
        "Värske kurk": 15,
        "Värske tomat": 20,
        "Marineeritud kurk": 30,
        "Marineeritud kapsas": 20,
        "Šokolaad": 530,
        "Riis": 130,
        "Tatar": 340,
        "Seamaks": 135,
        "Rõskkoor": 200,
        "Praetud muna": 200,
        "Viinerid": 270,
        "Peekon": 500,
        "Uba tomatikastmes": 90,
        "Jäätis": 200
    }
    
    toidud = list(toidud.items()) 
    
    while kogus < kalorid and toidud:
        toit, kcal = random.choice(toidud)
        if kogus + kcal <= kalorid:
            valitud_toidud.append((toit, kcal))
            kogus += kcal
        toidud = [t for t in toidud if t[0] != toit]

    return valitud_toidud


def arvuta_bmr(sugu, kaal, pikkus, vanus):
    """Arvutab baasainevahetuse (BMR) vastavalt Harris-Benedicti valemile."""
    if sugu == "mees":
        bmr = 88.36 + (13.4 * kaal) + (4.8 * pikkus) - (5.7 * vanus)
    elif sugu == "naine":
        bmr = 447.6 + (9.2 * kaal) + (3.1 * pikkus) - (4.3 * vanus)
    else:
        raise ValueError("Sugu peab olema 'mees' või 'naine'.")
    return bmr

def arvuta_energia_vajadus(bmr, aktiivsus, eesmargiks):
    """Arvutab päevase energiavajaduse vastavalt aktiivsusele ja eesmärgile."""
    aktiivsuse_korrutaja = {
        "istuv": 1.2,
        "väike": 1.375,
        "mõõdukas": 1.55,
        "kõrge": 1.725,
        "väga kõrge": 1.9
    }
    
    energia_vajadus = bmr * aktiivsuse_korrutaja.get(aktiivsus, 1.2)
    
    if eesmargiks == "kaalu langetamine":
        energia_vajadus -= 500
    elif eesmargiks == "kaalu tõstmine":
        energia_vajadus += 500
    return energia_vajadus

def makrotoitained(energia_vajadus):
    """Arvutab makrotoitainete jaotuse kalorites (valgud, rasvad, süsivesikud)."""
    valgud = energia_vajadus * 0.15 / 4
    rasvad = energia_vajadus * 0.25 / 9
    sysivesikud = energia_vajadus * 0.60 / 4
    return (valgud, rasvad, sysivesikud)


def kalkuleeri():
    """Kalkuleerib kõik sisestatud andmete põhjal ja kuvab tulemuse."""
    try:
        sugu = sugu_var.get().strip().lower()
        kaal = float(kaal_var.get())
        pikkus = float(pikkus_var.get())
        vanus = int(vanus_var.get())
        aktiivsus = aktiivsus_var.get().strip().lower()
        eesmargiks = eesmargiks_var.get().strip().lower()

        bmr = arvuta_bmr(sugu, kaal, pikkus, vanus)
        energia_vajadus = arvuta_energia_vajadus(bmr, aktiivsus, eesmargiks)
        
        valgud, rasvad, sysivesikud = makrotoitained(energia_vajadus)
        
        result_text = f"Teie päevane energiavajadus on {energia_vajadus:.2f} kcal.\n"
        result_text += f"Makrotoitainete jaotus:\n"
        result_text += f"- Valkude kogus: {valgud:.2f} g\n"
        result_text += f"- Rasvade kogus: {rasvad:.2f} g\n"
        result_text += f"- Süsivesikute kogus: {sysivesikud:.2f} g\n"

        toidud = soovita_toidud(energia_vajadus)
        result_text += "\nSoovitatud toidud:\n"
        for toit, kcal in toidud:
            result_text += f"{toit}: {kcal} kcal\n"

        result_label.config(text=result_text)
        
    except ValueError as e:
        messagebox.showerror("Sisendi viga", f"Viga sisendis: {e}")

root = tk.Tk()
root.title("Kalorite Kalkulaator")

sugu_var = tk.StringVar()
kaal_var = tk.StringVar()
pikkus_var = tk.StringVar()
vanus_var = tk.StringVar()
aktiivsus_var = tk.StringVar()
eesmargiks_var = tk.StringVar()

tk.Label(root, text="Sugu (mees/naine):").pack()
tk.Entry(root, textvariable=sugu_var).pack()

tk.Label(root, text="Kaal (kg):").pack()
tk.Entry(root, textvariable=kaal_var).pack()

tk.Label(root, text="Pikkus (cm):").pack()
tk.Entry(root, textvariable=pikkus_var).pack()

tk.Label(root, text="Vanus (aastates):").pack()
tk.Entry(root, textvariable=vanus_var).pack()

tk.Label(root, text="Aktiivsuse tase (istuv, väike, mõõdukas, kõrge, väga kõrge):").pack()
tk.Entry(root, textvariable=aktiivsus_var).pack()

tk.Label(root, text="Eesmärk (kaalu langetamine/kaalu tõstmine/kehakaalu hoidmine):").pack()
tk.Entry(root, textvariable=eesmargiks_var).pack()

tk.Button(root, text="Kalkuleeri", command=kalkuleeri).pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

root.mainloop()
