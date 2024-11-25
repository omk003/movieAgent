import json
dict = {'movie_name': 'Bhool Bhulaiyaa 3', 'movie_type': 'Horror, Comedy', 'cinemas': [{'cinema_name': 'INOX Reliance Mall, Garkheda, Aurangabad', 'showtimes': [{'showtime': '22:00', 'screen': 'SCREEN 5', 'seats': {'seat_type': 'Club', 'available_seats': 107, 'total_seats': 112, 'price': 240}}, {'showtime': '22:00', 'screen': 'SCREEN 5', 'seats': {'seat_type': 'Executive', 'available_seats': 36, 'total_seats': 36, 'price': 220}}, {'showtime': '22:00', 'screen': 'SCREEN 5', 'seats': {'seat_type': 'Royale Recliners', 'available_seats': 10, 'total_seats': 10, 'price': 430}}, {'showtime': '22:00', 'screen': 'SCREEN 5', 'seats': {'seat_type': 'Royale', 'available_seats': 73, 'total_seats': 82, 'price': 260}}]}, {'cinema_name': 'INOX Prozone Mall, Chilkalthana, Aurangabad', 'showtimes': [{'showtime': '21:30', 'screen': 'SCREEN 1', 'seats': {'seat_type': 'CLUB', 'available_seats': 159, 'total_seats': 165, 'price': 220}}, {'showtime': '21:30', 'screen': 'SCREEN 1', 'seats': {'seat_type': 'EXECUTIVE', 'available_seats': 56, 'total_seats': 56, 'price': 200}}, {'showtime': '21:30', 'screen': 'SCREEN 1', 'seats': {'seat_type': 'ROYALE RECLINERS', 'available_seats': 28, 'total_seats': 30, 'price': 430}}, {'showtime': '21:30', 'screen': 'SCREEN 1', 'seats': {'seat_type': 'ROYALE', 'available_seats': 45, 'total_seats': 50, 'price': 240}}]}]}
with open("./test/save_movie.json", "w") as outfile: 
    json.dump(dict, outfile)