import csv
import os
import random
import subprocess
import time
from pathlib import Path

import pyautogui

csv_path = Path(__file__).resolve().parent / "resources" / "most_streamed_spotify_2025.csv"


def escribir_palabra(palabra: str, delay: float = 0.3) -> None:
    """Escribe una palabra carácter por carácter con un pequeño retardo."""
    for letra in palabra:
        pyautogui.write(letra)
        time.sleep(delay)


def abrir_edge(url: str = "microsoft-edge:") -> None:
    """Abre Microsoft Edge sin usar coordenadas de pantalla específicas."""
    try:
        os.startfile(url)
    except OSError:
        subprocess.Popen(["cmd", "/c", "start", url], shell=False)
    time.sleep(2)
    pyautogui.hotkey("alt", "d") # Selecciona la barra de búsqueda
    time.sleep(0.5)

coordenadas_busquedas = [
    (1755, 549),  # Coordenadas de la primera búsqueda
    (1745, 734),  # Coordenadas de la segunda búsqueda
    (1737, 856),  # Coordenadas de la tercera búsqueda
]

try:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector, None)  # omite la fila de encabezado
        palabras = [fila[1] for fila in lector if len(fila) > 1 and fila[1].strip()]

    random.shuffle(palabras)

    max_searches = 35
    for i, palabra in enumerate(palabras[:max_searches], start=1):
        abrir_edge()
        escribir_palabra(palabra)

        pyautogui.press('enter')  # presiona enter después de cada palabra
        time.sleep(random.uniform(3, 6))  # pequeña pausa entre palabras

        pyautogui.hotkey('alt', 'f4')  # cierra la ventana después de cada búsqueda
    
    #   Aquí comienza la segunda fase del script

    abrir_edge()
    escribir_palabra("busqueda")  # escribe la palabra "rewards"
    pyautogui.press('enter')  # presiona enter después de escribir "rewards"
    time.sleep(2)  # espera 2 segundos antes de presionar enter 
       
    for coordenada in coordenadas_busquedas:
        pyautogui.doubleClick(1775, 140)  # Abre rewards
        time.sleep(2)  # espera 2 segundos antes de entrar a la sección de rewards
        pyautogui.click(1696, 951)  # abre la racha de conjunto diario
        time.sleep(1)  # espera 1 segundo antes de hacer la primer búsqueda
        pyautogui.click(*coordenada)  #Hace las búsquedas
        time.sleep(2)  # espera 2 segundos antes de repetir el ciclo
    
except KeyboardInterrupt:
    print("El programa ha sido interrumpido por el usuario.")