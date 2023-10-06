import os

# Ścieżka do katalogu z obrazami .tif
directory_path = 'J:/programowanie/ocrpy/traindata/'

# Utwórz plik listy
with open(os.path.join(directory_path, "list.txt"), 'w') as list_file:
    # Przeszukaj katalog w poszukiwaniu plików .tif
    for filename in os.listdir(directory_path):
        if filename.endswith(".tif"):
            # Pobierz nazwę pliku bez rozszerzenia
            base_name = os.path.splitext(filename)[0]
            # Zapisz nazwę pliku do list.txt
            list_file.write(base_name + '\n')

print("Zakończono tworzenie listy.")
