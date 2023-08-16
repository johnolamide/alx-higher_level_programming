-- list all shows
USE hbtn_0d_tvshows;
SELECT tv_shows.title, genre.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN genre ON tv_show_genres.genre_id = genre.id
ORDER BY tv_shows.title ASC, genre.name ASC;
