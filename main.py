try:
    import yt_dlp

    def download_video(url):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    link = input("Enter video URL: ")
    download_video(link)
except Exception:
    print(Exception)
    input("Press any key to exit...")