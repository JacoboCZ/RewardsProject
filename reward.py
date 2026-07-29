import pyautogui
import time

time.sleep(2)  # Espera 2 segundos antes de iniciar la acción
pyautogui.click(925, 39)  # Simula un clic del mouse en la posición actual
texto = "ejemplo de búsqueda"

for letra in texto:
    pyautogui.write(letra)
    time.sleep(0.5)  # pequeña pausa entre teclas, simula escritura humana

pyautogui.press('enter')