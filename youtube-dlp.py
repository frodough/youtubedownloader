import os
from yt_dlp import YoutubeDL

def clear_screen():
    os.system('cls||clear')

def get_user_input():
    print("======== YouTube Downloader ========\n")
    print("Press 1: Download a YouTube Video")
    print("Press 2: Download a YouTube Audio File\n")
    while True:
        answer = input("Please enter a selection: ")
        if answer in ['1', '2']:
            return answer
        print("Invalid entry: Enter only 1 or 2\n")

def validate_playlist():
    while True:
        playlist = input("Is this a playlist? (y/n): ")
        if playlist in ['y','n']:
            return playlist
        print("Invalid entry: Enter only (y/n)\n")

def download_video():
    clear_screen()
    print("======== YouTube Downloader Video ========\n")
    url = input("Enter the video url: ")
    playlist = validate_playlist()
    location = input("Enter the location to save the video: ")
    path = os.path.join(os.path.expanduser("~") + f"/{location}/")
    ydl_opts = {
        "outtmpl": f"{path}%(title)s.%(ext)s"
    }
    if playlist == 'y':
        ydl_opts["playlistreverse"] = True
    with YoutubeDL (ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download complete!")
        except Exception as e:
            print("Download failed: ", e)

def download_audio():
    clear_screen()
    print("======== YouTube Downloader Audio ========\n")
    url = input("Enter the video url: ")
    playlist = validate_playlist()
    location = input("Enter the location to save the mp3: ")
    path = os.path.join(os.path.expanduser("~") + f"/{location}/")
    ydl_opts = {
        "outtmpl": f"{path}%(title)s.%(ext)s",
        "format": "bestaudio/best",
        "extractaudio": True,
        "noplaylist": False,
        "playlistreverse": True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    if playlist == 'y':
        ydl_opts["playlistreverse"] = True
        ydl_opts["noplaylist"] = False
    else:
        ydl_opts["noplaylist"] = True
    with YoutubeDL (ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download complete!")
        except Exception as e:
            print("Download failed: ", e)

if __name__ == '__main__':
    clear_screen()
    answer = get_user_input()
    if answer == '1':
        download_video()        
    elif answer == '2':
        download_audio()
