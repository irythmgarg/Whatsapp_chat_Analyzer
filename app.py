import proprocessor
import streamlit as st
import fetcher
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
import emoji
st.markdown(
    '<p style="padding:0px;margin-left:0px;text-align: left;font-size:30px;">Welcome&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;नमस्ते</p>',
    unsafe_allow_html=True
)

st.sidebar.title("Whattsapp Chat Analyzer")
uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8");
    df=proprocessor.preprocess(data);
    user_name=df['user'].unique().tolist()
    user_name.remove("Group Notification")
    user_name.sort()
    user_name.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("show analysis with respect to ", user_name)
    if st.sidebar.button("show Analysis"):
        st.title("Top Statistics")
        col1, col2, col3,col4 = st.tabs(["Messages", "Words", "Media","Links"])
        num_messages,words,num_media,links=fetcher.fetch(selected_user, df);
        with col1:
            st.header("Total Messages")
            st.title(num_messages);
        with col2:
            st.header("Number of Words")
            st.title(words);
        with col3:
            st.header("Number of Media file shared")
            st.title(num_media);
        with col4:
            st.header("Number of links shared")
            st.title(links);

        if(selected_user=='Overall'):
           col1,col2=st.columns(2)
           x = fetcher.most_active_users(df)
           with col1:
             st.markdown("<p style='font-size:20px;'>Most Active Users",unsafe_allow_html=True)
             st.dataframe(x);
           with col2:
             fig,ax=plt.subplots()
             ax.bar(x.index,x.values)
             plt.xticks(rotation='vertical')
             st.pyplot(fig)
             p = pd.DataFrame(x)

           col1, col2 = st.columns(2)
           x = fetcher.least_active_users(df)
           with col1:
               st.markdown("<p style='font-size:20px;'>least Active Users", unsafe_allow_html=True)
               st.dataframe(x);
           with col2:
               fig, ax = plt.subplots()
               ax.bar(x.index, x.values)
               plt.xticks(rotation='vertical')
               st.pyplot(fig)
               p = pd.DataFrame(x)

        f=open('stop_hinglish.txt','r');
        stop_words=f.read();
        f2 = open('stopwords.txt', 'r');
        stop_words2 = f2.read();


        col1,col2 = st.columns(2)
        with col1:
           st.markdown("<p style='font-size:20px;'>Most frequently used words", unsafe_allow_html=True)
           st.write(fetcher.mostcommon(selected_user, df, stop_words,stop_words2))
        with col2:
            st.markdown("<p style='font-size:20px;'>Used Emojis With their Frequency", unsafe_allow_html=True)
            emojis = fetcher.emojicollector(df, selected_user)
            st.dataframe(emojis)


        timeline=fetcher.graph(df,selected_user)
        fig,ax2=plt.subplots()
        st.title('Monthly Timeline')
        ax2.plot(timeline['time'], timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        timeline2 = fetcher.graph2(df, selected_user)
        fig, ax3 = plt.subplots()
        st.title('Daily Timeline')

        plt.xticks(rotation='vertical')
        ax3.plot(timeline2['only_date'], timeline2['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        col1,col2=st.columns(2);
        with col1:
            week_activity=fetcher.week_activity_map(df,selected_user)
            fig, ax2 = plt.subplots()
            st.title('Day Wise')
            plt.figure(figsize=(10,10));
            ax2.bar(week_activity.index,week_activity.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            month_activity = fetcher.month_activity_map(df, selected_user)
            fig, ax2 = plt.subplots()
            plt.figure(figsize=(20, 20));
            st.title('Monthly')
            ax2.bar(month_activity.index, month_activity.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)


        # title = st.sidebar.text_input("Enter some text 👇", placeholder="Enter Here.")
        # if title:
        #     my_dict = fetcher.particularword(title, df)
        #     if my_dict:  # Check if there are any results
        #         newdf = pd.DataFrame(list(my_dict.items()), columns=['Message', 'Index'])
        #         st.write(newdf)
        #     else:
        #         st.write("No messages found containing the text.")
        # else:
        #     st.sidebar.write("Please enter some text to see results.")
else:
    st.markdown(
        '<p style="font-size:30px;">Upload a Whattsapp chat to analyse</p>',
        unsafe_allow_html=True
    )















