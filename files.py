import webbrowser

class MovieTrailers():
    def __init__(self,movie_title,movie_storyline,movie_posters_url,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.posters_image_url=movie_posters_url
        self.trailer_youtube_url=trailer_youtube
    def show_movie_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
