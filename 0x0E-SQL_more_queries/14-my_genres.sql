-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name AS name FROM tv_show_genres INNER JOIN tv_shows ON tv_shows.title = "Dexter";
