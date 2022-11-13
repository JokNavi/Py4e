import sqlite3
import xml.etree.ElementTree as ET


def find_value(root, find_value):
    return [tag.text for tag in root.findall(find_value)]


def print_tag(root):
    return [(i, root[i].tag) for i in range(len(root))]


def program():
    conn = sqlite3.connect(r'TestData/Database/trackdb.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Artist;')
    cur.execute('DROP TABLE IF EXISTS Genre;')
    cur.execute('DROP TABLE IF EXISTS Album;')
    cur.execute('DROP TABLE IF EXISTS Track;')
    cur.execute(
        'CREATE TABLE Artist ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);')
    cur.execute(
        'CREATE TABLE Genre ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE );')
    cur.execute(
        'CREATE TABLE Album ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE );')
    cur.execute('CREATE TABLE Track ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER );')

    tree = ET.parse(r'TestData/Library.xml')
    root = tree.getroot()
    root = root[0][17]


    find_value(root[1], "key")


def test():
    conn = sqlite3.connect(r'TestData/Database/trackdb.sqlite')
    cur = conn.cursor()

    cur.execute('''
            SELECT
                Track.title,
                Artist.name,
                Album.title,
                Genre.name 
            FROM
                Track 
            JOIN
                Genre 
            JOIN
                Album 
            JOIN
                Artist 
                ON Track.genre_id = Genre.ID 
                AND Track.album_id = Album.id 
                AND Album.artist_id = Artist.id 
            ORDER BY
                Artist.name LIMIT 3
            ''')

    conn.close()


program()
