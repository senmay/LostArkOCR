import pytesseract
import winsound
import time
from PIL import Image, ImageOps, ImageGrab
import tkinter as tk

# Określ obszar przechwytywania
REGION = (1160, 51, 1182, 69)
config = "-c tessedit_char_whitelist=X0123456789 --psm 6"


def wyswietl_powiadomienie(text):
    # Graj dźwięk głośowy
    winsound.Beep(1000, 100)

    root = tk.Tk()
    root.geometry("300x80+1250+40")
    root.attributes('-topmost', True)  # Umieść okno na wierzchu
    root.attributes('-alpha', 0.5)     # Ustawiłem przezroczystość na 0.3, ale możesz wybrać niższą wartość
    root.overrideredirect(True)  # Usuwa obramówkę okna
    label = tk.Label(root, text=text, font=("Arial", 15), wraplength=350, bg='gray') # Ustawiłem tło labela na szaro dla lepszej widoczności
    label.pack(pady=5)
    root.after(5000, root.destroy)  # Zamknij okno po 5 sekundach
    root.mainloop()


try:
    while True:
        # Przechwytuj obraz z określonego obszaru
        screenshot = ImageGrab.grab(bbox=REGION)
        grayscale_image = screenshot.convert("L")
        threshold = 95
        binary_image = grayscale_image.point(lambda p: 255 if p > threshold else 0)
        text = pytesseract.image_to_string(binary_image, config=config).strip()

        if text in ["189", "190"]:
            wyswietl_powiadomienie("Transformacja cube")
        if text in ["175", "176", "177"]:
            wyswietl_powiadomienie("Zaraz pierwsza mechanika, stan dobrze, sprawdź cube")
        elif text in ["162", "163", "164"]:
            wyswietl_powiadomienie("Transformacja cuba na 160")
        elif text in ["139", "140", "141"]:
            wyswietl_powiadomienie("Transformacja cuba na 135")
        elif text in ["125", "126", "127", "128"]:
            wyswietl_powiadomienie("Zaraz mechanika, stan dobrze")
        elif text in ["98", "99", "100"]:
            wyswietl_powiadomienie("Stagger zaraz")
        elif text in ["91", "92", "93"]:
            wyswietl_powiadomienie("Transformacja cuba")
        elif text in ["69", "70"]:
            wyswietl_powiadomienie("Transformacja cuba na 65")
        elif text in ["62", "57", "58"]:
            wyswietl_powiadomienie("Mechanika zaraz")
        elif text in ["40", "42", "44", "45"]:
            wyswietl_powiadomienie("Transformacja cuba")
        elif text in ["21", "22", "23", "24"]:
            wyswietl_powiadomienie("Zaraz stagger")

        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nProgram zakończony.")
