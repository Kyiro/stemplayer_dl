from random import random
import requests, logging, os 
from merger import merge

API_URL = "https://api.stemplayer.com/"
BASE_FOLDER = "Dump"
MERGE_SONGS = True

# https://github.com/krystalgamer/stem-player-emulator/blob/master/stem_emulator.user.js#L310
# broken
def random_serial() -> str:
    res = 0
    i = 0
    
    while (i < 24):
        res += int(random() * 10)
        i += 1
    
    return str(res)

def download_stems(data, album, track):
    logging.debug("      download_stems: initialized")
    
    os.makedirs(f'{os.getcwd()}/{BASE_FOLDER}/{album}/{track}')
    
    for url in data:
        match (url):
            case "1":
                r = requests.get(data[url]).content
                with open(f'{BASE_FOLDER}/{album}/{track}/instrumental.mp3', 'wb') as f:
                    f.write(r)
                pass
            case "2":
                r = requests.get(data[url]).content
                with open(f'{BASE_FOLDER}/{album}/{track}/vocals.mp3', 'wb') as f:
                    f.write(r)
                pass
            case "3":
                r = requests.get(data[url]).content
                with open(f'{BASE_FOLDER}/{album}/{track}/drums.mp3', 'wb') as f:
                    f.write(r)
                pass
            case "4":
                r = requests.get(data[url]).content
                with open(f'{BASE_FOLDER}/{album}/{track}/bass.mp3', 'wb') as f:
                    f.write(r)
            case _:
                logging.info("      download_stems: Unsupported stem?")
    
    logging.debug("      download_stems: finished")
    
    #if (MERGE_SONGS):
    #    merge(album, track)
    
    return

def get_albums():
    logging.info('request: Getting list of albums from the Kano API')
    
    r = requests.get(API_URL + "content/albums").json()['data']
    return r

def get_track(track_id, version=1, codec="mp3"):
    logging.debug('      request: Getting track by id {} with codec {}'.format(track_id, codec))
    
    url = API_URL + f'content/stems?track_id={track_id}&version={version}&codec={codec}&device_id=002800273330510139323636'
    r = requests.get(url).json()['data']
    
    return r