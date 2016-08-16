import fresh_tomatoes
import media

# Instance creation for all six movies
sound_of_music = media.Movie("Sound of music",
                             "A story of a nun who is a governess",
                             "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=mMSP7rwtigU")
parent_trap = media.Movie("Parent trap", "Twins who are separated",
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/Parenttrapposter.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=32WeiH4TrIY")

v_for_vendetta = media.Movie("V for vendetta",
                             "A single man trying to break a regime of hate",
                             "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=IHVzzxrPt1c")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

legally_blonde = media.Movie("Legally blonde",
                             "A stereotyped girl who gets into Harvard law and"
                             " breaks stereotypes",
                             "https://upload.wikimedia.org/wikipedia/en/a/ac/Legally_blonde.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=E8I-Qzmbqnc")

# List creation with all instances
movies = [sound_of_music, parent_trap, v_for_vendetta, ratatouille,
          midnight_in_paris, legally_blonde]

# Function call to open movie website
fresh_tomatoes.open_movies_page(movies)
