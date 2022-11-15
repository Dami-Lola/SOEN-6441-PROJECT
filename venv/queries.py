# author @ SAKSHI PATEL
# This file is used to fire a couple of queries to show the
# data from the API to user into the console

import csv
import sqlite3

# Creating connection to the database
Con = sqlite3.connect('news.db')
Cur = Con.cursor()

# Displaying all titles in the news db
print("Display all titles in the news db")
Cur.execute("select title from main")
result = Cur.fetchall()
for i in result:
    print(i[0])
print()

# Displaying all the sections in the news data
print("Display all the sections in the news data ")
Cur.execute("select section from main")
result = Cur.fetchall()
unique_list = []
for x in result:
    if x not in unique_list:
        unique_list.append(x)
for i in unique_list:
    print(i[0])
print()

# Displaying all the media copyrights
print("Display all the media copyrights")
Cur.execute("select copyright from media md inner join main on md.main_id = main.id")
result = Cur.fetchall()
for i in result:
    print(i[0])
print()

# Displaying title and abstract of news article on 2022-11-02
day = input("Give a date to get the title and abstract of news article on a particular day:")
print("Display title and abstract of news article on "+day)
Cur.execute("Select title, abstract from main where published_date = '"+day+"'")
result = Cur.fetchall()
for i in result:
    print("MOVIE TITLED " + i[0] + " HAS ABSTRACT " + i[1])
print()

# Displaying titles and subsections where section is Arts of all the news in the news data
section = input("Give a section name to get the titles and subsections for the same:")
print("Display titles and subsections where section is "+section+" of all the news in the news data")
Cur.execute("select title, subsection from main where  section = '"+section+"'")
result = Cur.fetchall()
for i in result:
    print(i[0])
print()

# Displaying byline and abstract of Opinion section articles
section = input("Give a section name to get the byline and abstract for the same:")
print("Display byline and abstract of "+section+" section articles ")
Cur.execute("select byline, abstract from main where section = '"+section+"';")
result = Cur.fetchall()
for i in result:
    print(i[0] + " HAS ABSTRACT " + i[1])
print()



# Displaying all the media urls for T Magazine section articles
section = input("Give a section name to display all media for section articles:")
print("Display all the media urls for "+section+" section articles ")
Cur.execute("select media_info.url as url from media md left join media_info on media_id = md.id inner join main on "
            "md.main_id = main.id  where section = '"+section+"'")
result = Cur.fetchall()
for i in result:
    print(i[0])
print()

# Displaying Adx keywords for articles in section Well
section = input("Give a section name to display Adx keywords for articles:")
print("Display Adx keywords for articles in section "+section)
Cur.execute("select keyword from adx_keywords adx inner join main on main.id = adx.main_id where section = '"+section+"'")
result = Cur.fetchall()
for i in result:
    print(i[0])
print()
