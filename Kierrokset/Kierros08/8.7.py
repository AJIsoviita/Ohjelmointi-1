tiedosto = open("esimerkkitiedostot.zip", "r")
import os, shutil, re
from zipfile import ZipFile
tiedosto = r"esimerkkitiedostot.zip"
kulli = r"kulli.zip"

def fix_filenames(tiedosto):
    with ZipFile(tiedosto, 'r') as my_zip:
        mp3 = [name for name in my_zip.namelist() \
               if os.path.splitext(name)[1].lower()== '.mp3']
        my_zip.extractall(kulli, mp3)
    for i in kulli:
        print(i)
    print('x')