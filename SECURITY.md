# Warning:

Pdftotext uses ImageMagick to parse PDFs in Windows and poppler-utils in Linux. While ImageMagick and poppler-utils are versatile tools, they have a history of some terrible security bugs. A malicious PDF could exploit a bug in ImageMagick or poppler-utils to take over your computer. If you're working with potentially malicious PDFs, it's safest to run them through Pdftotext in an isolated environment, such as a virtual machine.
