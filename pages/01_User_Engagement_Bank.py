#..............................UI design of User Engagement Page Bank.....................................

import streamlit as st # for data visualization in the web application
import pandas as pd # for dataframe manipulation
import plotly.express as px # for data visualization
from googleapiclient.discovery import build # for data extraction via API
import seaborn as sns # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)

#Importing Images to user interface (UI)

url0 = "https://raw.githubusercontent.com/udara135/SMA/main/images/all%20%20logo.png"
url1 = "https://raw.githubusercontent.com/udara135/SMA/main/images/Facebook%20logo.png"
url2 = "https://raw.githubusercontent.com/udara135/SMA/main/images/YouTube%20logo.png"
url3 = "https://raw.githubusercontent.com/udara135/SMA/main/images/Instagram%20%20logo.png"
url00 = "https://raw.githubusercontent.com/udara135/SMA/main/images/analysis.png"

response0 = requests.get(url0)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response00 = requests.get(url00)

img0 = Image.open(BytesIO(response0.content))
img1 = Image.open(BytesIO(response1.content))
img2 = Image.open(BytesIO(response2.content))
img3 = Image.open(BytesIO(response3.content))
img00 = Image.open(BytesIO(response00.content))

st.image(img0)
st.image(img2)

st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)


st.sidebar.image(img00)

#.......Extraction of DFCC bank Facebook page user engagement data..................

import pandas as pd 
import plotly.express as px 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np

from facebook_scraper import get_posts
x= []

for post in get_posts('dfccbankplc',pages =5,extra_infor=True,options={"comments":True,"reaction_count":True}):
    x.append(post)

df_dfccb = pd.DataFrame.from_dict(x)

df_dfccb

df_dfccb[['post_id','likes','shares','comments']]

from facebook_scraper import get_posts
y= []

for post in get_posts('HNBPLC',pages =5,options={"comments":True,"reaction_count":True}):
    y.append(post)

df_hnbp = pd.DataFrame.from_dict(y)

df_hnbp

df_hnbp[['post_id','likes','shares','comments']]


from facebook_scraper import get_posts
z= []

for post in get_posts('ndbbankplc',pages =5,options={"comments":True,"reaction_count":True}):
    z.append(post)

df_ndb = pd.DataFrame.from_dict(z)

df_ndb

df_ndb[['post_id','likes','shares','comments']]

from facebook_scraper import get_posts
q= []

for post in get_posts('pabcbank',pages =5,options={"comments":True,"reaction_count":True}):
    q.append(post)

df_pabcb = pd.DataFrame.from_dict(z)

df_pabcb

df_pabcb[['post_id','likes','shares','comments']]

user_engagement_peer = { 'Product' : ['DFCC Bank','HNB','NDB','PABC'],
                    'Likes': [df_dfccb['likes'].sum(),df_hnbp['likes'].sum(),df_ndb['likes'].sum(),df_pabcb['likes'].sum()],
                    'Shares' : [df_dfccb['shares'].sum(),df_hnbp['shares'].sum(),df_ndb['shares'].sum(),df_pabcb['shares'].sum()],
                    'Comments': [df_dfccb['comments'].sum(),df_hnbp['comments'].sum(),df_ndb['comments'].sum(),df_pabcb['comments'].sum()]
}

df = pd.DataFrame(user_engagement_peer)
df

import seaborn as sns

sns.set(rc={'figure.figsize':(10,8)})
ch_comp1= sns.barplot(x='Product', y='Likes', data=df)


sns.set(rc={'figure.figsize':(10,8)})
ch_comp2= sns.barplot(x='Product', y='Comments', data=df)

sns.set(rc={'figure.figsize':(10,8)})
ch_comp3= sns.barplot(x='Product', y='Shares', data=df)

sns.set(rc={'figure.figsize':(20,16)})
ch_dfcc_likes= sns.barplot(x='post_id', y='likes', data=df_dfccb[['post_id','likes','shares','comments']])

sns.set(rc={'figure.figsize':(20,16)})
ch_dfcc_shares= sns.barplot(x='post_id', y='shares', data=df_dfccb[['post_id','likes','shares','comments']])

sns.set(rc={'figure.figsize':(20,16)})
ch_dfcc_comments= sns.barplot(x='post_id', y='comments', data=df_dfccb[['post_id','likes','shares','comments']])

df

'''
Conclusion :
both NDB,PABC and HNB are the leading banks with more user engagement than DFCCbank
so need to be focus on to get much more user engagement compired to peer banks.


'''
#.......Extraction of DFCC bank YouTube channel user engagement data..................

from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

api_key = 'AIzaSyA-tcJYcndj45jHH9H4xhkDztVilROirpE'
#channel_id = 'UCbWZ43RBxXhF6oikhpDrSlw' # RuBeauty 

channel_ids = ['UCarLZ8E9DG0d6n46avsQK0Q', # DFCC Bank
               'UCbLAqE6pV7z2Qdg6Re5gfOw', # NDB Bank 
               'UCtObq4iV1jZqEf7cclLLzzA', # Commercial Bank of Ceylon PLC
               'UCFC-ntuwXAvbkvCovsbZbtw' # Hatton National Bank PLC
              
              ] 

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return all_data

channel_statistics = get_channel_stats(youtube, channel_ids)
channel_data = pd.DataFrame(channel_statistics)
channel_data

channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])
channel_data.dtypes

sns.set(rc={'figure.figsize':(10,8)})
ax = sns.barplot(x='Channel_name', y='Subscribers', data=channel_data)

ax = sns.barplot(x='Channel_name', y='Views', data=channel_data)

ax = sns.barplot(x='Channel_name', y='Total_videos', data=channel_data)

channel_data

playlist_id = channel_data.loc[channel_data['Channel_name']=='DFCC Bank PLC', 'playlist_id'].iloc[0]


def get_video_ids(youtube, playlist_id):
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids


video_ids = get_video_ids(youtube, playlist_id)

video_ids


def get_video_details(youtube, video_ids):
    all_video_stats = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                    part='snippet,statistics',
                    id=','.join(video_ids[i:i+50]))
        response = request.execute()
        
        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                               Published_date = video['snippet']['publishedAt'],
                               Views = video['statistics']['viewCount'],
                               Likes = video['statistics']['likeCount'],
                               Comments = video['statistics']['commentCount']
                               )
            all_video_stats.append(video_stats)
    
    return all_video_stats



video_details = get_video_details(youtube, video_ids)

video_data = pd.DataFrame(video_details)

video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Likes'] = pd.to_numeric(video_data['Likes'])
#video_data['Dislikes'] = pd.to_numeric(video_data['Dislikes'])
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data

top10_videos = video_data.sort_values(by='Views', ascending=False).head(10)

top10_videos

ax1 = sns.barplot(x='Views', y='Title', data=top10_videos)

video_data

video_data['Month'] = pd.to_datetime(video_data['Published_date']).dt.strftime('%b')

video_data

videos_per_month = video_data.groupby('Month', as_index=False).size()

videos_per_month


sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories=sort_order, ordered=True)

videos_per_month = videos_per_month.sort_index()

ax2 = sns.barplot(x='Month', y='size', data=videos_per_month)

video_data.to_csv('Video_Details(DFCC Bank).csv')