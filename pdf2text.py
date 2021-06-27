# PDFtoTEXT
# Copyright (c) 2021 ANISH M < aneesh25861@gmail.com >

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

''' This program converts all PDF files in current working directory to text Files.'''

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
      
     #Return to current working Directory.
     os.chdir('..')
