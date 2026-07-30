import csv
import random
import time
from pathlib import Path

import pyautogui

csv_path = Path(__file__).resolve().parent / "recourses" / "most_streamed_spotify_2025.csv"

with csv_path.open("r", encoding="utf-8-sig", newline="") as archivo_csv:
    lector = csv.reader(archivo_csv)
    next(lector, None)  # omite la fila de encabezado
    palabras = [fila[1] for fila in lector if len(fila) > 1 and fila[1].strip()]

random.shuffle(palabras)

time.sleep(2)  # Espera 2 segundos antes de iniciar la acción
pyautogui.click(887, 40)  # Simula un clic del mouse en la posición actual

for palabra in palabras:
    pyautogui.click(887, 40)  # vuelve a enfocar la ventana de texto antes de escribir

    for letra in palabra:
        pyautogui.write(letra)
        time.sleep(0.3)  # pausa entre cada letra

    pyautogui.click(887, 40)  # vuelve a enfocar la ventana de texto
    pyautogui.press('enter')  # presiona enter después de cada palabra
    time.sleep(random.uniform(3, 10))  # pequeña pausa entre palabras

    pyautogui.hotkey('alt', 'f4')  # cierra la ventana después de cada búsqueda
