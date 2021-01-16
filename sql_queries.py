# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (
songplay_id SERIAL PRIMARY KEY,
start_time time NOT NULL,
user_id int NOT NULL,
level varchar,
song_id varchar,
artist_id varchar,
session_id int,
location varchar,
user_agent varchar)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id int PRIMARY KEY,
first_name varchar NOT NULL,
last_name varchar,
gender varchar,
level varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song (
song_id varchar PRIMARY KEY,
title varchar NOT NULL,
artist_id varchar NOT NULL,
year int,
duration numeric)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (
artist_id varchar PRIMARY KEY,
artist_name varchar NOT NULL,
artist_location varchar,
latitude numeric,
longitude numeric)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time time PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s,%s,%s,%s,%s, %s,%s,%s)
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level
""")

song_table_insert = (""" INSERT INTO song (song_id, title, artist_id, year, duration) VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = (""" INSERT INTO artist (artist_id, artist_name, artist_location,  latitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = (""" SELECT s.song_id, a.artist_id FROM song s JOIN artist a ON s.artist_id = a.artist_id
WHERE s.title = %s and a.artist_name = %s and s.duration = %s """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

