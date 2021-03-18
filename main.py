import csv
import os
import pandas as pd
from googleapiclient.discovery import build

api_key = "AIzaSyBdKfpBe2PNbh6ySg7E3G_gNnq9g9diCAs"

youtube = build('youtube', 'v3', developerKey = api_key)
os.chdir('F:\Project')

def youtube_playlist_data(id):
    token = None
    #using api's list function to retrieve the channel data
    y_data = youtube.channels().list(id=id, part='contentDetails').execute()
    #retrieving the 'uploads' playlist Id from the channel
    youtube_playlist_id = y_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    video_data  = []

    while 1:
        y_playlist_data = youtube.playlistItems().list(playlistId=youtube_playlist_id, part='snippet', maxResults=50, pagetoken = token).execute()
        video_data = video_data + y_playlist_data['items']
        token = y_playlist_data.get('nextPageToken')

        if token is None:
            break;
        return video_data


y_video_data = youtube_playlist_data('UCQYMhOMi_Cdj1CEAU-fv80A')
#initializing the variables
title = []
description = []
thumbnail_default = []
thumbnail_standard = []
for data in y_video_data:
    title.append(data['snippet']['title'])
    description.append(data['snippet']['description'])
    if 'thumbnails' in data['snippet'].keys():
        if 'default' in data['snippet']['thumbnails'].keys():
            thumbnail_default.append(data['snippet']['thumbnails']['default']['url'])
        else:
            thumbnail_default.append('Null')
        if 'standard' in data['snippet']['thumbnails'].keys():
            thumbnail_standard.append(data['snippet']['thumbnails']['standard']['url'])
        else:
            thumbnail_standard.append('NUll')

    else:
        thumbnail_default.append('NUll')
        thumbnail_standard.append('Null')


final_data = {'video_title':title, 'Description':description, 'thumbnail_default':thumbnail_default, 'thumbnail_standard':thumbnail_standard}

file = pd.DataFrame(final_data)
file.to_csv('ChannelData.csv', encoding='utf-8', index=False)



#This file is changed to show the working of the git commands


def function(a):
    return a*a
