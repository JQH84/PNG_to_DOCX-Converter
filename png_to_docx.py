from PIL import Image
from pathlib import Path
from PyPDF2 import PdfFileMerger
from pdf2docx import parse

path = input("Drag the folder into the terminal or type the path where the files exist ensure no space is at the en of the path you type:\n")
file_list = []
pdf_list = []


for i in range(10):
    file_list.append(f"/{i+1}.png")
    with Image.open(f"{path}/{file_list[i]}") as im:
         im.save(f'{path}/{i+1}.pdf',format='pdf')
    pdf_list.append(str.replace(file_list[i],'.png','.pdf'))
    
merger = PdfFileMerger()

for pdf in pdf_list:
    merger.append(path+pdf)
merger.write(f"{path}/result.pdf")
merger.close()
parse(path+'/result.pdf')