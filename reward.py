import csv
import random
import time
from pathlib import Path

import pyautogui

csv_path = Path(__file__).resolve().parent / "resources" / "most_streamed_spotify_2025.csv"


def escribir_palabra(palabra: str, delay: float = 0.3) -> None:
    """Escribe una palabra carácter por carácter con un pequeño retardo."""
    for letra in palabra:
        pyautogui.write(letra)
        time.sleep(delay)


try:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector, None)  # omite la fila de encabezado
        palabras = [fila[1] for fila in lector if len(fila) > 1 and fila[1].strip()]

    random.shuffle(palabras)

    time.sleep(2)  # Espera 2 segundos antes de iniciar la acción
    pyautogui.click(887, 40)  # Simula un clic del mouse en la posición actual

    max_searches = 35
    for i, palabra in enumerate(palabras[:max_searches], start=1):
        pyautogui.click(887, 40)  # vuelve a enfocar la ventana de texto antes de escribir

        escribir_palabra(palabra)

        pyautogui.click(887, 40)  # vuelve a enfocar la ventana de texto
        pyautogui.press('enter')  # presiona enter después de cada palabra
        time.sleep(random.uniform(3, 6))  # pequeña pausa entre palabras

        pyautogui.hotkey('alt', 'f4')  # cierra la ventana después de cada búsqueda
    time.sleep(2)  # espera 2 segundos antes de continuar con la siguiente fase
    
except KeyboardInterrupt:
    print("El programa ha sido interrumpido por el usuario.")
