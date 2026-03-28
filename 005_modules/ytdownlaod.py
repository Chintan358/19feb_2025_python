from pytube import YouTube

# Paste your YouTube video URL here
url = input("Enter YouTube URL: ")

try:
    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get highest resolution stream
    video = yt.streams.get_highest_resolution()

    print("Downloading...")
    video.download()

    print("Download completed!")

except Exception as e:
    print("Error:", e)