import os

# Ścieżka do katalogu z obrazami .tif
directory_path = 'J:/programowanie/ocrpy/traindata/'

# Przeszukaj katalog w poszukiwaniu plików .tif
for filename in os.listdir(directory_path):
    if filename.endswith(".tif"):
        # Pobierz nazwę pliku bez rozszerzenia
        base_name = os.path.splitext(filename)[0]

        # Utwórz nazwę dla pliku .txt
        txt_filename = base_name + '.txt'

        # Zapisz nazwę pliku (bez rozszerzenia) do pliku .txt
        with open(os.path.join(directory_path, txt_filename), 'w') as txt_file:
            txt_file.write(base_name)

print("Zakończono tworzenie plików tekstowych.")
