# author @ SAKSHI PATEL
# This file parses the JSON data from the news API and
# transfers it into three different CSV files according to
# further need of creating the application

import json
import csv

# Opening JSON file and loading the data into the variable data
with open('/Users/sakshipatel/PycharmProjects/news/newsarticle.json') as json_file:
    Data = json.load(json_file)
News_data = Data['results']

# Open a file for writing news data
Data_file = open('news.csv', 'w')
# Create the csv writer object
Csv_writer = csv.writer(Data_file)

# Counter variables used for writing headers to the CSV file
Count = 0
Count1 = 0
Count2 = 0
for news in News_data:
    if Count == 0:
        # Writing headers of news CSV file
        Header = news.keys()
        Csv_writer.writerow(Header)
        Count += 1
    # Writing data of news CSV file
    Csv_writer.writerow(news.values())

    Media_data = (news.get('media'))
    # Open a file for writing media data
    Media_file = open('media.csv', 'a')
    Csv_media = csv.writer(Media_file)
    for media in Media_data:
        if Count1 == 0:
            # Writing headers of media CSV file
            Header2 = media.keys()
            Csv_media.writerow(Header2)
            Count1 += 1
        # Writing data of media CSV file
        Csv_media.writerow(media.values())

    # Open a file for writing media_info data
    Media_info_file = open('media_info.csv', 'a')
    Csv_media_info = csv.writer(Media_info_file)
    for i in Media_data[0]['media-metadata']:
        if Count2 == 0:
            # Writing headers of media_info CSV file
            Csv_media_info.writerow(i.keys())
            Count2 += 1
        # Writing data of media_info CSV file
        Csv_media_info.writerow(i.values())

    # Closing the files
    Media_file.close()
    Media_info_file.close()

Data_file.close()
