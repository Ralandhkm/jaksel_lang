import Utama as interpreter
from datetime import date
import sys

tanggal = date.today().strftime("%B %d, %Y")

while True:
	teks = input('Kode > ')
	if teks.strip() == "": continue
	hasil, error = interpreter.esekusi("<stdin>", teks)

	if error: print(error.jadiString())
	elif hasil: 
		if len(hasil.isi) == 1:
			print(repr(hasil.isi[0]))
		else:
			print(repr(hasil))

# python konsol.py