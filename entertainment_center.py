import media
import trailers

The_Martian = media.Movie("The Martian", "About",
                          "https://m.media-amazon.com/images/M/"
                          "MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@"
                          "._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")
# print(voz.storyline)
Idiots = media.Movie("3Idiots", "About Friends and Life",
                     "https://m.media-amazon.com/images/M/"
                     "MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2"
                     "ZGJmYzFhXkEyXk"
                     "FqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                     "https://www.youtube.com/watch?v=K0eDlFX9GMc")
The_Persuit_of_Happyness = media.Movie("The Persuit of Happyness",
                                       "About goals",
                                       "http://image.tmdb.org/t/p/original/"
                                       "hfsn5EdfNX6UTdNU0Nkelg2wqTp.jpg",
                                       "https://www.youtube.com/"
                                       "watch?v=DMOBlEcRuw8")
Banglore_Days = media.Movie("Banglore Days", "About Friendship",
                            "https://image3.mouthshut.com/images/MoviesMusic/"
                            "photo/Bangalore-Days-56621_3516.jpg",
                            "https://www.youtube.com/watch?v=Gdzif0Px_qY")
Hachi_A_Dogs_Tale = media.Movie("Hachi A Dogs Tale", "movie",
                                "http://www.affirmfilms.com/files/"
                                "POSTER-hachiadogstale-387x580.jpg",
                                "https://www.youtube.com/"
                                "watch?v=TIl2o1hm1F4")
# voz.show_trailer()

movies = [The_Martian, Idiots, The_Persuit_of_Happyness,
          Banglore_Days, Hachi_A_Dogs_Tale]
trailers.open_movies_page(movies)
# print(media.Movie.__doc__)
