# Primary Key : a way for us to refer to a particular row, and it's unique number
#               ending point of the arrow
# Logical Key : unique thing that we might use to look up this row from the outside world
# Foreign Key : starting point of the arrow

# CREATE TABLE Track(
#     id INTERGER NOT NULL PRIMARY AUTOINCREMENT UNIQUE,
#     title TEXT,
#     album_id INTEGER,
#     genre_id INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# )

# SELECT Track.title, Genre.name from Track join Genre
# on Track.genre_id = Genre.id

# It can get complex
# select Track.title, Artist.name, Album.title, Genre.name from Track
# join Genre join album join Artist on Track.genre_id = Genre.id and Track.album.id = Album.id
# and Album.artist_id = Artist.id