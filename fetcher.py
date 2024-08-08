import pandas as pd
import streamlit
from urlextract import URLExtract
extract=URLExtract()
import emoji
import matplotlib.pyplot as plt
from collections import Counter
def fetch(user_name,df):
    if(user_name!='Overall'):
        df = df[df['user'] == user_name]
    words=[]
    for message in df['message']: # number of words
      words.extend(message.split())
    num_messages=df.shape[0] # number of messages
    num_media=df[df['message']=='<Media omitted>\n'].shape[0]
    urls=[]
    for message in df['message']:  # number of words
        urls.extend(extract.find_urls(message))
    return num_messages,len(words),num_media,len(urls)
def most_active_users(df):
    x=df['user'].value_counts().head()
    return x
def least_active_users(df):
    x=df['user'].value_counts().tail()
    return x

def mostcommon(selected_user,df,stop_words,stop_words2):
    df = df[df['user'] != 'Group Notification'];
    df = df[df['message'] != '<Media omitted>\n'];
    if(selected_user!='Overall'):
        df=df[df['user']==selected_user];
    lis=[];
    words=[]
    mesagingwords=['added','deleted','edited>','left','<this','y','message']
    for message in df['message']:
     for word in message.lower().split():
         if word not in stop_words and word not in stop_words2 and word not in mesagingwords and word.isalpha():
             words.append(word);
    return pd.DataFrame(Counter(words).most_common(20));

# def particularword(selected_word, df):
#     # Initialize an empty dictionary
#     my_dict = {}
#
#     # Iterate over the rows of the dataframe
#     for index, message in df['message'].iteritems():
#         # Check if the selected word is in the message
#         if selected_word.lower() in message.lower().split():
#             # Add the message and its index to the dictionary
#             my_dict[message] = index
#
#     return my_dict

def emojicollector(df,selected_user):
  if(selected_user!='Overall'):
     df=df[df['user']==selected_user]
  emojis = [];
  for messages in df['message']:
      emojis.extend([c for c in messages if emoji.is_emoji(c)])
  df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
  return df


def graph(df,selected_user):
    if(selected_user!='Overall'):
        df=df[df['user']==selected_user]
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
       time.append(str(timeline['month'][i])+'-'+str(timeline['year'][i]));
    timeline['time']=time;
    return timeline

def graph2(df,selected_user):
    if(selected_user!='Overall'):
        df=df[df['user']==selected_user]
    timeline = df.groupby(['only_date']).count()['message'].reset_index()
    return timeline
def week_activity_map(df,selected_user):
    if (selected_user != 'Overall'):
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts();


def month_activity_map(df,selected_user):
    if (selected_user != 'Overall'):
        df = df[df['user'] == selected_user]
    return df['month'].value_counts();




