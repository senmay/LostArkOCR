import pytesseract
import time
from PIL import Image, ImageOps, ImageGrab

# Określ obszar przechwytywania
REGION = (1160,51,1182,69)
#REGION = (1219, 70, 1264, 94)

# Konfiguracja dla Tesseract (bez białej listy)
config = "-c tessedit_char_whitelist=X0123456789 --psm 6"

ostatnia_poprawna_wartosc = None

try:
    while True:
        # Przechwytuj obraz z określonego obszaru
        screenshot = ImageGrab.grab(bbox=REGION)

        # Konwersja na skalę szarości
        grayscale_image = screenshot.convert("L")
        grayscale_image.save("grayscale_screenshot.png")


        # Binaryzacja z progiem 50%
        threshold = 95
        binary_image = grayscale_image.point(lambda p: 255 if p > threshold else 0)

        binary_image.save("binary_screenshot.png")

        # Użyj OCR do rozpoznania tekstu z obrazu w skali szarości
        text = pytesseract.image_to_string(binary_image, config=config).strip()
        print(text)

        # Odczekaj pewien czas przed kolejnym przechwytywaniem (np. 0.3 sekundy)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nProgram zakończony.")


