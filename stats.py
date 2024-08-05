# importing the libraries
import emoji.unicode_codes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urlextract import URLExtract
from collections import Counter
from wordcloud import WordCloud

import emoji
extract=URLExtract()

def fetch_stat(selected_user,df):
    if selected_user !='overall':
        df=df[df['User']==selected_user]
        #extracting messges
        num_messages=df.shape[0]
        #extracting words
        words=[]
        for word in df['Message']:
            words.extend(word.split())
        # extracting links 
        links=[]
        for word in df['Message']:
            links.extend(extract.find_urls(word))
        # extracting the media

        media_omitted=df[df['Message']=='<Media omitted>']
        # return the output
    return num_messages, len(words), media_omitted.shape[0], len(links)
    


def fetch_busy(df):
    #getting the busy user
    df=df[df['User']!='Group Notification']
    # Taking the counts
    count=df['User'].value_counts().head()
    # Taking the Dataframe of Ratio of busy
    newdf=pd.DataFrame((df['User'].value_counts()/df.shape[0])*100)
    newdf.columns=['Presence_perc']
    # returning the counts newdf
    return count, newdf

# function of making a word cloud
def create_wc(df,selected_user):
    if selected_user !='overall':
        df=df[df['User']==selected_user]
        wc=WordCloud(width=400,height=400,background_color='white')
        w_img=wc.generate(df['Message'].str.cat(sep=' '))
        return w_img

# Function of finding most common words

def get_common_words(selected_user,df):
    if selected_user !='overall':
        df=df[df['User']==selected_user]
        stopwords_file=open('stop_hinglish.txt','r')
        stop_words=stopwords_file.read()
        stop_words=stop_words.split('\n')
        temp=df[(df['User']!='Group Notification') | (df['User']!='<Media omitted>')]
        words=[]

        for message in temp['Message']:
            for word in message.lower().split():
                if word not in stop_words:
                    words.append(word)
        most_common_words=pd.DataFrame(Counter(words).most_common(20))
        return most_common_words


# Emoji Function

import pandas as pd
import emoji  # Assuming you have installed the emoji library

def get_emojis(selected_user, df):
    if selected_user != 'overall':
        user_df = df[df['User'] == selected_user]

        emojis = []
        for message in user_df['Message']:
            emojis.extend(c for c in message if c in emoji.EMOJI_DATA)

        emoji_df = pd.DataFrame(Counter(emojis).most_common())
        emoji_df.columns = ['Emoji', 'Count']

        # Optional: Normalize emoji counts
        # emoji_df['Count'] = emoji_df['Count'] / len(user_df)

        return emoji_df


# Most Busy Months

def most_busy_months(selected_user,df):
    if selected_user !='overall':
        df=df[df['User']==selected_user]
        return df['Month'].value_counts()
    

# Most busy Days

def most_busy_days(selected_user,df):
    if selected_user !='overall':
        df=df[df['User']==selected_user]
        return df['Day_name'].value_counts()

            

