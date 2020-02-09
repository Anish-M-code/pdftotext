
import os

#Loop to get names of all PDF files in current working Directory.
for i in os.listdir():
  if i[-3:].lower()=='pdf':
     
     #create an output folder.
     os.mkdir(i+'_output')
     
     #Move PDF file to output folder.
     os.system('mv '+i+' '+i+'_output')
     
     #Change directory to output folder.
     os.chdir(i+'_output')
     
     #Convert PDF file to PNG images using pdftocairo tool in poppler-utils.
     os.system('pdftocairo '+i+' '+'-png')

#Loop to get names of all PNG image files in current working directory.
for i in os.listdir():
  if i[-3:].lower()=='png':
  
     #Pass the image to Tesseract ocr to recover text from images.
     os.system('tesseract '+i+' '+i[:-3])
     
     #Delete the image generated during Conversion of PDF to Text files.
     os.remove(i)
