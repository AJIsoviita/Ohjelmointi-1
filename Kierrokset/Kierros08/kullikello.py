import os


def fix_filenames(koko_tiedosto):
    sisältö = os.listdir(koko_tiedosto)
    for tiedosto in sisältö:
        if tiedosto.endswith(".mp3"):
            chars = list(tiedosto)
            try:
                int(chars[0])

                a = tiedosto.strip(".mp3")
                jako = a.split("-")
                artisti = jako[1]
                kappale = jako[2]
                uusi_nimi = kappale + "-" + artisti + ".mp3"
                os.rename(os.path.join(koko_tiedosto, tiedosto),
                          os.path.join(koko_tiedosto, uusi_nimi))
            except:
                pass