import argparse
import os
import pytesseract

# The main class containing the 3 stage processing of the PDF
class Scanner:
	def __init__(self,tractList,pdf_dir,out_dir):
		

	def coarseScan(self):
		


# The main driver class
def main():
	print("Detect Tracts with Tesseract OCR - Coarse Scan Proof of Concept")
	print("#############################################################")

	tractList=["Section-Township-Range", "metes & bounds", "lots/blocks"]
	
	if args.pdf_dir and args.out_dir:
		pass
	else:
		print("Syntax: python -m deed_ocr --pdf_dir ./input_pdfs --out_dir ./out")


if __name__ == '__main__':
	main()