import webbrowser

# Definition of class Movie


class Movie():
    # Information about the class
    """Definition of class Movie. Used to create different movie instances

       Attributes:
       title(str) : Title of the movie
       storyline(str) : Storyline of the movie
       poster_image_url(str) : Url for the movie poster
       trailer_youtube_url(str) : Url for the movie trailer

       Methods:
       __init__ : Constructor to initialize class instance
       show_trailer(self) : Method to open browser with movie trailer link"""

    # Constructor initializes movie instance with values for instance variables
    def __init__(self, title, story, poster, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    # Instance method to open supplied youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer)
