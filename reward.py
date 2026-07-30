import random
import pyautogui
import time

time.sleep(2)  # Espera 2 segundos antes de iniciar la acción
pyautogui.click(887, 40)  # Simula un clic del mouse en la posición actual

palabras = [
    "este", "programa", "escribe", "treinta", "palabras", "en", "una", "lista",
    "para", "simular", "escritura", "humana", "en", "una", "ventana", "de", "texto",
    "cada", "elemento", "se", "envia", "con", "un", "pequeno", "retardo",
    "y", "al", "final", "presiona", "enter"
]

for palabra in palabras:
    pyautogui.click(887, 40)  # vuelve a enfocar la ventana de texto antes de escribir

    for letra in palabra:
        pyautogui.write(letra)
        time.sleep(0.3)  # pausa entre cada letra

    pyautogui.click(887, 40)  # vuelve a enfocar la ventana de texto
    pyautogui.press('enter')  # presiona enter después de cada palabra
    time.sleep(random.uniform(0.5, 10))  # pequeña pausa entre palabras

    pyautogui.hotkey('alt', 'f4')  # cierra la ventana después de cada búsqueda
