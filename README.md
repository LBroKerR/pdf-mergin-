# Recommeneded
install pyhton 3.12 from microsoft store
pip install PyPDF2


# PDF Kezelő Script pdf_merge.py

konzol megnyitása

cd C:\Users\dorin\Desktop\"pdf össze  vonása"

fájl futtatása python pdf_merge.py

két elérésiút megadása a parancsok szerintm, és végül a kezdő oldalszám megadása.

kimenet a mappában merge_outpu.pdf néven. 

Figyelem:

merge_outpu.pdf-re mindig rá fog ja menteni az új merge-t, ebből következik, hogy minden merge után legyen el mentve a fájl egy másik néven egy új helyre.

# PDF Kezelő Script pdf_editor.py

Ez a Python alapú program PDF fájlok manipulálására szolgál, lehetőséget biztosít oldalak törlésére, intervallumok kezelésére, valamint két PDF fájl összefűzésére egy megadott helyen. A program támogatja a parancssori flagek használatát, így rugalmasan kezelhető különböző műveletekre.

---

## Funkciók

- Egy adott oldal törlése.
- Oldalak törlése egy megadott intervallumban.
- Két PDF fájl összefűzése egy megadott pozícióban.
- Kombinált műveletek, például oldalak törlése és másik PDF beillesztése.
- Minden művelet fájl elérési úttal történik, így nincs szükség fix helyen lévő fájlokra.

---
--pdf-a=<elérési út>: Az első PDF fájl elérési útja (kötelező).
--pdf-b=<elérési út>: A második PDF fájl elérési útja (opcionális, ha beillesztés szükséges).

Opcionális flagek
--delete-page=N: Egy adott oldalt (N-edik) töröl az első PDF fájlból.
--delete-range=S-E: Egy oldaltartományt (S-től E-ig, zárt intervallum) töröl az első PDF fájlból.
--insert=N: A második PDF tartalmát az első PDF N-edik oldala után illeszti be.
--help: Megjeleníti a súgót és kilép.


## Használat

python script.py --pdf-a=/path/to/input.pdf --delete-page=3

python script.py --pdf-a=/path/to/input.pdf --delete-range=5-10

python script.py --pdf-a=/path/to/A.pdf --pdf-b=/path/to/B.pdf --insert=7

python script.py --pdf-a=/path/to/A.pdf --pdf-b=/path/to/B.pdf --delete-range=2-4 --insert=5

python script.py --help

### Szintaxis

```bash
python script.py [opciók]