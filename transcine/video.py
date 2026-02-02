import os
import mimetypes
from pymediainfo import MediaInfo

def get_video_info(path : str) -> dict:
    '''returns info about a video file
    ici indique que path doit être un string et que la fonction retourne un dico'''
    info = MediaInfo.parse(path)
    for track in info.tracks:
        if track.track_type == "Video":

            return {
                "width" : track.width,
                "height" : track.height,
                "duration_ms" : track.duration,
                "frame_rate" : float(track.frame_rate),
                "duration_s" : track.duration / 1000
            }