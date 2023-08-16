-- lists all genres
USE hbtn_0d_tvshows;
SELECT genre.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genre
LEFT JOIN tv_show_genres ON genre.id = tv_show_genres.genre_id
GROUP BY genre.id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;
