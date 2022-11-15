# author @ SAKSHI PATEL
# This file is used to convert the No-SQL data from the
# csv files created in jsonParser.py into SQL format to use
# it throughout the application

import csv
import sqlite3

# Creating connection to the database
Con = sqlite3.connect('news.db')
Cur = Con.cursor()

# Creation of tables by using the execute method for applying SQL queries to the database
Cur.execute("CREATE TABLE main (uri, url,id,asset_id,source,published_date,updated,section,subsection,nytdsection,"
            "byline,type,title,abstract,eta_id);")
Cur.execute("CREATE TABLE media (id, media_id, type, subtype ,caption ,copyright,approved_for_syndication,"
            "media_metadata);")
Cur.execute("CREATE TABLE adx_keywords (id, main_id,keyword,type);")
Cur.execute("CREATE TABLE media_info (id, media_id ,url ,format,height,width);")

# Opening the CSV file to transfer data to the database
with open('/Users/sakshipatel/PycharmProjects/news/venv/news.csv', 'r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    Dr = csv.DictReader(fin)
    To_main = [
        (i['uri'], i['url'], i['id'], i['asset_id'], i['source'], i['published_date'], i['updated'], i['section'],
         i['subsection'], i['nytdsection'], i['byline'], i['type'], i['title'], i['abstract'], i['eta_id']) for i
        in Dr]

# Inserting multiple rows to the table by using executemany method of sqlite3
Cur.executemany("INSERT INTO main (uri, url,id,asset_id,source,published_date,updated,section,subsection,nytdsection,"
                "byline,type,title,abstract,eta_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", To_main)

# Opening the CSV file to transfer data to the database
with open('/Users/sakshipatel/PycharmProjects/news/venv/news.csv', 'r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    Dr = csv.DictReader(fin)
    Count = 0
    To_adx = [((i['adx_keywords']), i['id'], i['des_facet'], i['org_facet'], i['per_facet'], i['geo_facet']) for i in
              Dr]
    for id_fk in To_adx:
        listadx = id_fk[0].split(";")
        for j in listadx:
            Count += 1
            if j in id_fk[2]:
                Type = 'des_facet'
            if j in id_fk[3]:
                Type = 'org_facet'
            if j in id_fk[4]:
                Type = 'per_facet'
            if j in id_fk[5]:
                Type = 'geo_facet'
            Cur.execute("INSERT INTO adx_keywords (id, main_id,keyword,type) VALUES (?,?,?,?);",
                        (Count, id_fk[1], j, Type))

# Opening the CSV file to transfer data to the database
with open('/Users/sakshipatel/PycharmProjects/news/venv/media.csv', 'r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    Dr_media = csv.DictReader(fin)
    To_media = [
        (i['type'], i['subtype'], i['caption'], i['copyright'], i['approved_for_syndication'], i['media-metadata']) for
        i in Dr_media]

# Inserting multiple rows to the table by using executemany method of sqlite3
Cur.executemany("INSERT INTO media (type, subtype ,caption ,copyright,approved_for_syndication,media_metadata) "
                "VALUES (?,?,?,?,?,?);", To_media)

# Opening the CSV file to transfer data to the database
with open('/Users/sakshipatel/PycharmProjects/news/venv/media_info.csv', 'r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    Dr_media_info = csv.DictReader(fin)
    To_media_info = [(i['url'], i['format'], i['height'], i['width']) for i in Dr_media_info]
    Count_info = 0
    Count_media = 1
    for i in To_media_info:
        Count_info += 1
        Cur.execute("INSERT INTO media_info (id, media_id ,url ,format,height,width) VALUES (?,?,?,?,?,?);",
                    (Count_info, Count_media, i[0], i[1], i[2], i[3]))
        if Count_info % 3 == 0:
            Count_media += 1
Con.commit()
Con.close()
