from youtube_dl import YoutubeDL

# Type and run the samples below, one by one
# Result: https://www.dropbox.com/s/cm5m6zitnuwdqbk/Screenshot%202017-12-08%2005.32.02.png?dl=0

# Sample 1: Download a single youtube video
dl = YoutubeDL()
#Natural - image dragon
dl.download(['https://www.youtube.com/watch?v=0I647GU3Jsc']) # Remember to put your video in a list, eventhough one video is downloaded



# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=0mwL7DCMcpI'])



# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=3GeaYy6zlXU'])



# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['Mercy'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['In My Feelings'])