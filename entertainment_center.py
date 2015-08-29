import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story of toys coming to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#avatar.show_trailer()

spirited_away = media.Movie("Spirited Away",
                            "A child who discovers a secret spirit world",
                            "http://vignette2.wikia.nocookie.net/studioghibli/images/6/61/Spirited_away.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

ponyo = media.Movie("Ponyo On The Cliff By The Sea",
                    "A goldfish who became a child and befriends a boy",
                    "https://upload.wikimedia.org/wikipedia/en/b/b3/Ponyo.jpg",
                    "https://www.youtube.com/watch?v=MXI7x6ExPuc")
                    
matrix = media.Movie("The Matrix",
                     "A hacker discovers the world is a computer simulation",
                     "http://ecx.images-amazon.com/images/I/91HQ3kSAxhL._SL1500_.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")
movies = [toy_story, avatar, spirited_away, ponyo, matrix]

fresh_tomatoes.open_movies_page(movies)
