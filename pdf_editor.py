from PyPDF2 import PdfReader, PdfWriter
import os
import sys

def print_help_and_exit():
    help_text = """
    PDF Kezelő Script - Flagek és Használat

    Használat:
      python script.py [opciók]

    Fájlok:
      - Az első PDF megadása kötelező (--pdf-a=<elérési út>).
      - A második PDF opcionális, ha beillesztés szükséges (--pdf-b=<elérési út>).

    Lehetőségek (flagek):
      --help                  - Megjeleníti ezt a súgót és kilép.
      --pdf-a=<elérési út>    - Az első PDF elérési útja.
      --pdf-b=<elérési út>    - A második PDF elérési útja (beillesztéshez szükséges).
      --delete-page=N         - Egy adott (N-edik) oldalt töröl.
      --delete-range=S-E      - Egy intervallum (S-től E-ig, zárt) oldalait törli.
      --insert=N              - Ha két PDF van megadva, a második fájlt az N-edik oldalra illeszti be. pl: N=2 akkor pdf-b első oldala pdf-a 2. oldalán kezdődik.

    Példák:
      1. Egy adott oldal törlése:
         python script.py --pdf-a=input.pdf --delete-page=3
      2. Oldalak törlése 5 és 10 között:
         python script.py --pdf-a=input.pdf --delete-range=5-10
      3. Két PDF összefűzése a 7. oldal helyén:
         python script.py --pdf-a=A.pdf --pdf-b=B.pdf --insert=7
      4. Kombinált művelet (törlés + beillesztés):
         python script.py --pdf-a=A.pdf --pdf-b=B.pdf --delete-range=2-4 --insert=5
    """
    print(help_text)
    exit(0)

# Ellenőrizzük, hogy a help flag aktív-e
if "--help" in sys.argv:
    print_help_and_exit()

# Parancssori argumentumok feldolgozása
args = sys.argv[1:]

# Alapértelmezett értékek
pdf_a_path = None
pdf_b_path = None
delete_page = None
delete_range = None
insert_at = None

# Argumentumok értelmezése
for arg in args:
    if arg.startswith("--pdf-a="):
        pdf_a_path = arg.split("=")[1]
    elif arg.startswith("--pdf-b="):
        pdf_b_path = arg.split("=")[1]
    elif arg.startswith("--delete-page="):
        try:
            delete_page = int(arg.split("=")[1]) - 1
        except ValueError:
            print("Hiba: A --delete-page flaghez érvényes oldalszámot kell megadni!")
            exit(1)
    elif arg.startswith("--delete-range="):
        try:
            range_parts = arg.split("=")[1].split("-")
            delete_range = (int(range_parts[0]) - 1, int(range_parts[1]) - 1)
        except ValueError:
            print("Hiba: A --delete-range flaghez érvényes intervallumot kell megadni (pl. 3-5)!")
            exit(1)
    elif arg.startswith("--insert="):
        try:
            insert_at = int(arg.split("=")[1]) - 1
        except ValueError:
            print("Hiba: A --insert flaghez érvényes oldalszámot kell megadni!")
            exit(1)

# Ellenőrizzük a fájlok meglétét
if not pdf_a_path or not os.path.exists(pdf_a_path):
    print("Hiba: Az első PDF fájlt (--pdf-a=<elérési út>) meg kell adni, és léteznie kell!")
    exit(1)
if pdf_b_path and not os.path.exists(pdf_b_path):
    print("Hiba: A második PDF fájl (--pdf-b=<elérési út>) nem található!")
    exit(1)

# PDF olvasók
reader_a = PdfReader(pdf_a_path)
reader_b = PdfReader(pdf_b_path) if pdf_b_path else None

# PDF író
writer = PdfWriter()

# Oldalak feldolgozása
for page_num in range(len(reader_a.pages)):
    # Törölt oldalak kihagyása
    if delete_page is not None and page_num == delete_page:
        print(f"A(z) {delete_page + 1}. oldal törlésre került.")
        continue
    if delete_range is not None and delete_range[0] <= page_num <= delete_range[1]:
        print(f"A(z) {page_num + 1}. oldal törlésre került.")
        continue
    # Beillesztés az adott helyre
    if insert_at is not None and page_num == insert_at and reader_b:
        print(f"B.pdf tartalma beillesztésre került a(z) {insert_at + 1}. oldal után.")
        for b_page in reader_b.pages:
            writer.add_page(b_page)
    # A.pdf oldalak hozzáadása
    writer.add_page(reader_a.pages[page_num])

# Ha az insert flag az A.pdf végére szól, kezeljük külön
if insert_at is not None and insert_at >= len(reader_a.pages) and reader_b:
    print(f"B.pdf tartalma beillesztésre került az A.pdf végére.")
    for b_page in reader_b.pages:
        writer.add_page(b_page)

# Kimeneti fájl mentése
output_filename = 'processed_output.pdf'
with open(output_filename, 'wb') as output_pdf:
    writer.write(output_pdf)

print(f"A feldolgozott PDF sikeresen elmentve: {output_filename}")