import os
import mimetypes

def get_video_info(path : str) -> dict:
    '''returns True if the file exists
    ici indique que path doit être un string et que la fonction retourne un dico'''
    found, _ = mimetypes.guess_type(path)
    if found != None:
        if found.split('/') == 'video':
            print('Onpeut continuer')
        else:
            print("Il ne s'agit pas d'un fichier vidéo")