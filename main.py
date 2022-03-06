from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
from moviepy.editor import *
from tkinter import *
from urllib.error import HTTPError

def download(name, isUrl):
    # Get youtube results if not an url
    if not isUrl:
        print(f"Looking for '{name}' ...") 
        vid = VideosSearch(name, limit=1)
        url = vid.result()['result'][0]['link']
        print(f"Found '{vid.result()['result'][0]['title']}' !")

    # Download it
    print('Downloading ...')
    try:
        yt = YouTube(name if isUrl else url)
        t = yt.streams.filter(only_audio=True)
        res = t[0].download('downloadedMusic')
        print("Downloaded !\n")
        return res

    # http errors
    except HTTPError as e:
        # update available
        if e.code == 410:
            print('New update available. Downloading...')
            os.system('python -m pip install --upgrade pytube')
            print("\n\nProgram just upgraded. Please run it again to make it work !")
            input('Press Enter to exit the program...')
            exit(0)
    # other errors
    except Exception as e:
        print(f"Error: {e}\n")
        return ''

def main():
    # file operations
    file = open('./list.txt', 'r')
    content = file.readlines()

    # main loop
    for i in content:
        name = download(i, True if 'http' in i else False)
    print('Finished !')
    input('Press Enter to exit the program...')

main()
