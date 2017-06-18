import webbrowser as wb

class Movie:
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    def show_trailer(self):
        ffpath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        wb.register('chrome', None, wb.BackgroundBrowser(ffpath), 1)
        chrome = wb.get('chrome')
        chrome.open(self.trailer_youtube)