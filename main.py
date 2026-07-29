import pyautogui
import time
import mouse

print("Monitoring mouse position every 2 seconds.")
print("Press and hold the left mouse button to stop.")

while True:
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")

    if mouse.is_pressed("left"):
        print("Left click detected. Stopping.")
        break

    time.sleep(2)