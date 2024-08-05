import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import streamlit as st
import Preprocessing
from stats import fetch_stat,fetch_busy,create_wc,get_common_words,most_busy_days,most_busy_months,get_emojis
st.sidebar.title("Whatsapp Chat Analyzer")

# Uploading a file

upload_file=st.file_uploader("Choose a whatsapp chat file")
# Uploading a file
if upload_file is not None:
    # Working on a uploaded file
    bytes_data = upload_file.getvalue()
    
    bytes=bytes_data.decode("utf-8")
    #getting data as dataframe
    df=Preprocessing.preprocess(bytes)

    #Displaying the dataframe

    #st.dataframe(df)

    #fetching the unique users

    users=df['User'].unique().tolist()
    
    # removing the notifications becuase I need only users

    users.remove('Group Notification')
    
    # sorting the users
    users.sort()
    # inserting the overall label
    users.insert(0, "Overall")
    # creating a sidebar for selecting user
    selected_user = st.sidebar.selectbox(
        "Show analysis with respect to", users)

    st.title("Whats App Chat Analysis for " + selected_user)

    if st.sidebar.button('Show analysis '):
        num_message, num_words, media_omitted, links = fetch_stat(
            selected_user, df)
    # showing the number of output
    
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_message)

        with col2:
            st.header("Total No.of Words")
            st.title(num_words)

        with col3:
            st.header("Media Shared")
            st.title(media_omitted)

        with col4:
            st.header("Total Links Shared")
            st.title(links)
        # Finding the busiest user
        if selected_user=='Overall':
            st.title('Most busy Users')
            busy_users,newdf=fetch_busy(df)
            # ploting the user
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            # bar plot
            with col1:
                ax.bar(busy_users.index,busy_users.values,color='green')
                st.pyplot(fig)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(newdf)
            
        # Creating a WordCloud
        if selected_user!='Overall':
            st.title('Word Cloud of a particular user')
            w_img=create_wc(df,selected_user)
            fig,ax=plt.subplots()
            ax.imshow(w_img)
            st.pyplot(fig)
        # Get common words
        most_common=get_common_words(selected_user,df)
        fig,ax=plt.subplots()
        ax.barh(most_common[0],most_common[1])
        plt.xticks(rotation='vertical')
        plt.title('Common words')
        st.pyplot(fig)

         #Get emojis
        st.title('Emoji ANna')
        emoji_df=get_emojis(selected_user,df)
        emoji_df.columns=['Emoji','Count']
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            Emoji_count=list(emoji_df['Count'])
            perlist=[(i/sum(Emoji_count)*100) for i in Emoji_count]
            emoji_df['PercentageList']=np.array(perlist)
            st.dataframe(emoji_df)
        
        # Most busy days and Months
        col1,col2=st.columns(2)
        with col1:
         st.title('Busy Days')
         busy_days=most_busy_days(selected_user,df)
         fig,ax=plt.subplots()
         ax.bar(busy_days.index,busy_days.values)
         st.pyplot(fig)
        with col2:
         st.title('Busy Months')
         busy_months=most_busy_months(selected_user,df)
         fig,ax=plt.subplots()
         ax.bar(busy_months.index,busy_months.values)
         st.pyplot(fig)

         
            
            



