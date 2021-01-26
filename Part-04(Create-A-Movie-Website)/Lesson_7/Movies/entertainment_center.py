import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=v-PjgYDrg70")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

home = media.Movie("Home", "story",
                    "https://www.newdvdreleasedates.com/images/posters/large/home-2015-02.jpg",
                    "https://www.youtube.com/watch?v=MyqZf8LiWvM")

school_of_rock = media.Movie("school_of_rock", "storyline",
                            "https://fanart.tv/fanart/movies/1584/movieposter/school-of-rock-53f7a862c918b.jpg",
                            "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille", "storyline",
                          "https://johnrieber.files.wordpress.com/2013/06/ratatouille-poster.jpg",
                          "https://www.youtube.com/watch?v=bKedSHDpkvI")

midnight_in_paris = media.Movie("Midnight_in_paris", "storyline",
                                "https://images-na.ssl-images-amazon.com/images/I/7169gq7PgdL._AC_SL1060_.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger_Games", "storyline",
                           "https://s2982.pcdn.co/wp-content/uploads/2015/11/hunger-games-catching-fire-movie-poster.jpg",
                           "https://www.youtube.com/watch?v=FovFG3N_RSU")

movies = [toy_story, avatar, home, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
