import media
import fresh_tomatoes
"""	list_elem_name=media.Movie(name,poster link,youtube trailer link)"""
hitman_s_bodyguard=media.Movie(
	"Hitman's body guard",
	"https://upload.wikimedia.org/wikipedia/en/2/2d/HitmansBodyguard.jpg",
	"https://www.youtube.com/watch?v=9TEVn44hr8w")
american_assasin=media.Movie(
	"American assasin",
	"https://upload.wikimedia.org/wikipedia/en/5/5d/American_Assassin.jpg",
	"https://www.youtube.com/watch?v=n_NcS62Sx7I",)
battements_par_mn=media.Movie(
	"120 battements par minute",
	"https://upload.wikimedia.org/wikipedia/en/c/cd/120_battements_par_minute.jpg",
	"https://www.youtube.com/watch?v=q4Jgg4uUVqI"
	)
Blade_runner_2049=media.Movie(
	"Blade runner 2049",
	"https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png",
	"https://www.youtube.com/watch?v=aZ9Os8cP_gg")	
Movies=[hitman_s_bodyguard,american_assasin,battements_par_mn,Blade_runner_2049]
fresh_tomatoes.open_movies_page(Movies)