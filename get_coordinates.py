import pyautogui
import time

try:
    while True:
        # Pobierz bieżące współrzędne kursora myszy
        x, y = pyautogui.position()
        print(f'X: {x}, Y: {y}')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram zakończony.")
