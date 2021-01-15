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
