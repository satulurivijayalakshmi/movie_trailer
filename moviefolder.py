import files
import fresh_tomatoes
bighero6=files.MovieTrailers("BigHero6","Robotics","https://encrypted-tbn0.gstatic.com/images?"
                       "q=tbn:ANd9GcTBrcW-BhmwYvxxDiAjYAbKmrUdiPvQdt8b1iT4p9lflb83SbWU",
                       "https://www.youtube.com/watch?v=rD5OA6sQ97M")
uturn=files.MovieTrailers("UTurn","Thriller","https://data1.ibtimes.co.in/cache-img-0-450/en/"
                          "full/698906/1536778560_samantha-akkineni-u-turn.jpg",
                          "/www.youtube.com/watch?v=HG7Lv384yTU")
theri=files.MovieTrailers("Theri","A Family Drama","https://encrypted-tbn0.gstatic.com/images?"
                          "q=tbn:ANd9GcRtGLs3Ft_0nw16gyIvnKu20_unodE7n4f0ZbzRIaJi3_L-JXG3",
                          "https://www.youtube.com/watch?v=ZK4uGLpkAKk")
threeidiots=files.MovieTrailers("3 idiots","All Is Well","https://encrypted-tbn0.gstatic.com/"
                             "images?q=tbn:ANd9GcSaWWmDamf0VAWT3fbLXhICyUGyG8A62WCDMZpIc-lmE141L_GX",
                             "https://www.youtube.com/watch?v=xvszmNXdM4w")
dangal=files.MovieTrailers("Dangal","Inspirational","https://content-images.p-cdn.com/images/public/amz/2/"
                           "3/2/8/FAK1481827168232_1080W_1080H.jpg",
                           "https://www.youtube.com/watch?v=x_7YlGv9u1g")
bangloredays=files.MovieTrailers("BangloreDays","Entertainer","https://i.ytimg.com/vi/Gdzif0Px_qY/0.jpg",
                                 "www.youtube.com/watch?v=uVpHL5g4buY")
                           
movies=[bighero6,uturn,theri,threeidiots,dangal,bangloredays]
fresh_tomatoes.open_movies_page(movies)
