from PyPDF2 import PdfReader, PdfWriter
import os

# Felhasználói bemenetek
pdf_a_path = input("Add meg a pdf útvonalát amibe bele szertnél fűzni (pl. /path/to/A.pdf): ")
pdf_b_path = input("Add meg a belefűzni kívánt pdf teljes elérési útját (pl. /path/to/B.pdf): ")

# Ellenőrizhetjük, hogy a fájlok léteznek-e
if not os.path.exists(pdf_a_path):
    print(f"Hiba: Az A.pdf fájl nem található a következő úton: {pdf_a_path}")
    exit(1)

if not os.path.exists(pdf_b_path):
    print(f"Hiba: A B.pdf fájl nem található a következő úton: {pdf_b_path}")
    exit(1)

# PDF olvasók létrehozása
reader_a = PdfReader(pdf_a_path)
reader_b = PdfReader(pdf_b_path)

# Felhasználó kéri, hogy hol kezdődjön a B.pdf
try:
    page_start = int(input("Add meg, hányadik oldaltól szeretnéd, hogy kezdődjön a B.pdf: ")) - 1
except ValueError:
    print("Hiba: Érvénytelen oldalszám.")
    exit(1)

# Ellenőrizzük, hogy az oldalszám érvényes-e
if page_start < 0 or page_start >= len(reader_a.pages):
    print(f"Hiba: A megadott oldalszám ({page_start+1}) érvénytelen az A.pdf-ben!")
    exit(1)

# PDF Writer létrehozása
writer = PdfWriter()

# Az A.pdf oldalaiból hozzáadjuk az első részt (A oldalait a kiválasztott oldal előtt)
for page_num in range(page_start):
    writer.add_page(reader_a.pages[page_num])

# Az egész B.pdf hozzáadása
for page_num in range(len(reader_b.pages)):
    writer.add_page(reader_b.pages[page_num])

# Az A.pdf maradék oldalait hozzáadjuk
for page_num in range(page_start, len(reader_a.pages)):
    writer.add_page(reader_a.pages[page_num])

# Kimeneti fájl létrehozása
output_filename = 'merged_output.pdf'
with open(output_filename, 'wb') as output_pdf:
    writer.write(output_pdf)

print(f"Az összefűzött PDF sikeresen elkészült és elmentésre került: {output_filename}")