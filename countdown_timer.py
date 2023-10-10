import time
import winsound
import keyboard

def countdown_timer(seconds):
    print(f"Oczekiwanie na rozpoczęcie... (naciśnij '0' na klawiaturze numerycznej aby zacząć)")
    keyboard.wait('num_0')  # czeka na naciśnięcie klawisza "0" na klawiaturze numerycznej
    while True:
        print(f"Oczekiwanie przez {seconds} sekund...")
        time.sleep(seconds)
        winsound.Beep(440, 1000)  # 440 Hz przez 1 sekundę

if __name__ == "__main__":
    countdown_timer(55)
