import csv
import os
from googleapiclient.discovery import build
import pandas as pd
# API Key generated from the Youtube API console
api_key = "AIzaSyBdKfpBe2PNbh6ySg7E3G_gNnq9g9diCAs"
# Establishing connection with the YouTube API key
youtube  = build('youtube','v3',developerKey=api_key)
# Setting up the directory location e.g. C:/Users/prateek/Desktop
os.chdir('F:\Project')

# Part 1 of the code
# This function helps us to fetch the Youtube channel playlist data
# Part 1 of the code
# This function helps us to fetch the Youtube channel playlist data
def youtube_playlist_data(id):
    token = None
    # Using the API's list function to retrive the channel data
    y_data = youtube.channels().list(id=id,part='contentDetails').execute()
    print(y_data)
    # Retrieving the "uploads" playlist Id from the channel
    youtube_playlist_id = y_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    video_data = []
    # The while loop which continues until the items are present in the playlist
    # while 1:
    #     y_playlist_data = youtube.playlistItems().list(playlistId = youtube_playlist_id, part = 'snippet', maxResults = 50, pageToken = token).execute()  #Retrieving the playlist items snippet with a max result of 50 in each iteration
    #     video_data = video_data + y_playlist_data['items']
    #     # Update the token so as to get the next data
    #     token = y_playlist_data.get('nextPageToken')
    #     # If there is no token break the loop
    #     if token is None:
    #         break
    # # Return the final collected data
    # return video_data

# Part 2 of the code
# Here we pass the channel id of which the data needs to be retrieved
y_video_data = youtube_playlist_data('UCkw4JCwteGrDHIsyIIKo4tQ')
# Initializing the title variable
title = []
# Initializing the description variable
description = []
# Initializing the thumbnail_default variable
thumbnail_default = []
# Initializing the thumbnail_standard variable
thumbnail_standard = []
# iterating through videos data one by one
for data in y_video_data:
    # Retrieving and appending the video title
     title.append(data['snippet']['title'])
    # Retrieving and appending the description
     description.append(data['snippet']['description'])
    # Check whether the thumbnail attribute is present
     if 'thumbnails' in data['snippet'].keys():
        if 'default' in data['snippet']['thumbnails'].keys():
            # If thumbnail default present append the data
            thumbnail_default.append(data['snippet']['thumbnails']['default']['url'])
        else:
            # If thumbnail default not present append 'Null'
            thumbnail_default.append('Null')
        if 'standard' in data['snippet']['thumbnails'].keys():
            # If thumbnail standard present append the data
            thumbnail_standard.append(data['snippet']['thumbnails']['standard']['url'])
        else:
            # If thumbnail standard not present append 'Null'
            thumbnail_standard.append('Null')
     else:
         thumbnail_default.append('Null')
         thumbnail_standard.append('Null')
final_data = {'video_title': title, 'Description':description, 'thumbnail_default': thumbnail_default, 'thumbnail_standard':thumbnail_standard} # Merge the data to form the final dataset

# Part 3 of the code
#Creating pandas data frame
file = pd.DataFrame(final_data)
# Save into csv format in the desired location
file.to_csv('Edureka.csv', encoding='utf-8', index=False)
