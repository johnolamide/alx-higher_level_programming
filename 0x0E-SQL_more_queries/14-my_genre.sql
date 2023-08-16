-- list genres
USE hbtn_0d_tvshows;
SELECT genre.name FROM genre
INNER JOIN tv_show_genres ON genre.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genre.name ASC;
