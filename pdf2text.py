import os
import subprocess
import platform
import sys
from time import sleep

pkg = ''
tesseract = 'tesseract'

# Detect if platform is using apt, dnf, pacman, or xbps package manager.
try:
    subprocess.run(['apt', '-v'], capture_output=True).stdout
    pkg = 'apt'
except Exception:
    try:
        subprocess.run(['dnf', '--version'], capture_output=True).stdout
        pkg = 'dnf'
    except Exception:
        try:
            subprocess.run(['pacman', '--version'], capture_output=True).stdout
            pkg = 'pacman'
        except Exception:
            try:
                subprocess.run(['xbps-query', '-V'], capture_output=True).stdout
                pkg = 'xbps'
            except:
                print('Platform not supported!')
                sleep(5)
                sys.exit(1)

# Check for Windows platform
if platform.system().lower() == 'windows':
    print('Platform not supported!')
    sleep(5)
    sys.exit(1)

if pkg == 'xbps':
    tesseract = 'tesseract-ocr'

# Function to install Tesseract language packs
def install_language_pack(language):
    print(f'Trying to install Tesseract language pack for {language}...')
    if pkg == 'apt':
        subprocess.run(['sudo', 'apt', 'install', f'tesseract-ocr-{language}']).stdout
    elif pkg == 'dnf':
        subprocess.run(['sudo', 'dnf', 'install', f'tesseract-langpack-{language}']).stdout
    elif pkg == 'pacman':
        subprocess.run(['sudo', 'pacman', '-S', f'tesseract-data-{language}']).stdout
    elif pkg == 'xbps':
        subprocess.run(['sudo', 'xbps-install', f'tesseract-ocr-{language}']).stdout

# Function to check if the requested language is supported
def check_language_supported(language):
    supported_langs = subprocess.run([tesseract, '--list-langs'], capture_output=True, text=True).stdout.splitlines()
    if language in supported_langs:
        print(f'{language} is supported by Tesseract.')
        return True
    else:
        print(f'{language} is not supported by Tesseract. Please check if the correct language pack is installed.')
        return False

# Install tesseract if not installed
try:
    subprocess.run([tesseract, '-v'], capture_output=True)
except Exception:
    print('Tesseract Not Found!\nTrying to Install it...')
    if pkg == 'apt':
        subprocess.run(['sudo', 'apt', 'update']).stdout
        subprocess.run(['sudo', 'apt', 'install', 'tesseract-ocr']).stdout
    elif pkg == 'dnf':
        subprocess.run(['sudo', 'dnf', 'install', 'tesseract']).stdout
    elif pkg == 'pacman':
        subprocess.run(['sudo', 'pacman', '-S', 'tesseract']).stdout
    elif pkg == 'xbps':
        subprocess.run(['sudo', 'xbps-install', tesseract]).stdout

# Install pdftocairo if not installed
try:
    subprocess.run(['pdftocairo', '-v'], capture_output=True)
except Exception:
    print('pdftocairo Not Found!\nTrying to Install it...')
    if pkg == 'apt':
        subprocess.run(['sudo', 'apt', 'update']).stdout
        subprocess.run(['sudo', 'apt', 'install', 'poppler-utils']).stdout
    elif pkg == 'dnf':
        subprocess.run(['sudo', 'dnf', 'install', 'poppler-utils']).stdout
    elif pkg == 'pacman':
        subprocess.run(['sudo', 'pacman', '-S', 'poppler']).stdout
    elif pkg == 'xbps':
        subprocess.run(['sudo', 'xbps-install', 'poppler-utils']).stdout

# Get the optional language argument
languages = 'eng'  # Default language is English

if len(sys.argv) > 1:
    languages = sys.argv[1]  # User can pass a comma-separated list of languages (e.g., 'eng+fra+spa')

    # Split the languages and install/check each required language pack
    lang_list = languages.split('+')
    for lang in lang_list:
        if not check_language_supported(lang):
            install_language_pack(lang)
            if not check_language_supported(lang):
                print(f'Failed to install {lang}. Please install manually or check the package name.')
                sys.exit(1)

# Loop to get names of all PDF files in current working Directory.
for pdf_file in os.listdir():
    if pdf_file.endswith('.pdf'):

        print(f'\nProcessing {pdf_file}')
        # create an output folder.
        output_folder = pdf_file + '_output'
        os.mkdir(output_folder)

        # Move PDF file to output folder.
        subprocess.run(['mv', pdf_file, output_folder])

        # Change directory to output folder.
        os.chdir(output_folder)

        # Convert PDF file to PNG images using pdftocairo tool in poppler-utils.
        print(f'\nConverting {pdf_file} into PNGs...')
        subprocess.run(['pdftocairo', pdf_file, '-png'])

        # Loop to get names of all PNG image files in current working directory.
        for image_file in os.listdir():
            if image_file.endswith('.png'):
                print(f'Extracting Text from {image_file}')
                # Pass the image to Tesseract OCR to recover text from images with specified languages.
                subprocess.run([tesseract, image_file, image_file[:-4], '-l', languages], capture_output=True)

                # Delete the image generated during Conversion of PDF to Text files.
                os.remove(image_file)

        # Return to current working directory.
        os.chdir('..')
        print('Cleaning up PNGs...')

print('\nDone!')
