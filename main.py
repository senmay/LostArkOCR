import pytesseract
import time
import cv2
from PIL import ImageGrab

# Określ obszar przechwytywania
#REGION = (1219, 70, 1264, 94)
REGION = (1239,65,1297,86)

# Konfiguracja dla Tesseract (bez białej listy)
config = "-c tessedit_char_whitelist=X0123456789 --psm 6"


def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Zwiększenie kontrastu przez wyrównanie histogramu
    image = cv2.equalizeHist(image)

    # Adaptacyjne progowanie
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return image

try:
    while True:
        # Przechwytuj obraz z określonego obszaru
        screenshot = ImageGrab.grab(bbox=REGION)

        # Konwersja na skalę szarości
        grayscale_image = screenshot.convert("L")
        grayscale_image.save("processed_screenshot.png")

        # Użyj OCR do rozpoznania tekstu z obrazu w skali szarości
        text = pytesseract.image_to_string(grayscale_image, config=config)
        print(text)

        # Odczekaj pewien czas przed kolejnym przechwytywaniem (np. 2 sekundy)
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\nProgram zakończony.")


