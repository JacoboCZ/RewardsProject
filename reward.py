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

coordenadas_busquedas = [
    (1704, 616),  # Coordenadas de la primera búsqueda
    (1690, 816),  # Coordenadas de la segunda búsqueda
    (1700, 931),  # Coordenadas de la tercera búsqueda
]

try:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector, None)  # omite la fila de encabezado
        palabras = [fila[1] for fila in lector if len(fila) > 1 and fila[1].strip()]

    random.shuffle(palabras)

    time.sleep(1)  # Espera 1 segundo antes de iniciar la acción
    pyautogui.click(1073, 1055)  # Abre edge de la barra de tareas
    time.sleep(2)  # Espera 2 segundos para que Edge se abra

    max_searches = 35
    for i, palabra in enumerate(palabras[:max_searches], start=1):
        pyautogui.click(289, 59)  # vuelve a enfocar la ventana de texto antes de escribir

        escribir_palabra(palabra)

        pyautogui.click(289, 59)  # vuelve a enfocar la ventana de texto
        pyautogui.press('enter')  # presiona enter después de cada palabra
        time.sleep(random.uniform(3, 6))  # pequeña pausa entre palabras

        pyautogui.hotkey('alt', 'f4')  # cierra la ventana después de cada búsqueda
    
    #   Aquí comienza la segunda fase del script

    time.sleep(2)  # espera 2 segundos antes de continuar con la siguiente fase
    pyautogui.click(1073, 1055)  # Abre edge de la barra de tareas nuevamente
    time.sleep(1)  # Espera 1 segundo para que Edge se abra
    for coordenada in coordenadas_busquedas:
        pyautogui.doubleClick(1775, 151)  # Abre rewards
        time.sleep(2)  # espera 2 segundos antes de entrar a la sección de rewards
        pyautogui.click(1880, 635)  # pone el foco en rewards
        time.sleep(1)  # espera 1 segundo antes de hacer scroll
        pyautogui.scroll(-900)  # desplaza hacia arriba para ver la siguiente sección
        time.sleep(1)  # espera 1 segundo antes de hacer la primer búsqueda
        pyautogui.click(*coordenada)  #Hace las búsquedas
        time.sleep(2)  # espera 2 segundos antes de repetir el ciclo
    
except KeyboardInterrupt:
    print("El programa ha sido interrumpido por el usuario.")