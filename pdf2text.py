# PDFtoTEXT
# Copyright (C) 2018-2021 M.Anish <aneesh25861@gmail.com>
# Copyright (C) 2020-2021 Kavyan
# Copyright (C) 2020-2021 Pranav
# Copyright (C) 2020-2021 Hariram
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
