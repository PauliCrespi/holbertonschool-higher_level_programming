-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title AS title FROM tv_shows WHERE tv_shows.id NOT IN (SELECT tv_shows.id FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id AND tv_genres.name = "Comedy") ORDER BY title ASC;
