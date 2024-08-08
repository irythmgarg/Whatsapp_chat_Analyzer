import re
import pandas as pd
def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, data);  # split data with pattern
    messages = messages[1:];  # remove first element
    dates = re.findall(pattern, data);  # find all dates pattern
    len(messages), len(dates)
    # number of messages in the chat
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})  # converting into dataFrame
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ');
    user = [];
    messages = [];
    for message in df['user_message']:
        split_message = re.split('([\w\W]+?):\s', message)
        if split_message[1:]:
            user.append(split_message[1])
            messages.append(split_message[2])
        else:
            user.append('Group Notification')
            messages.append(split_message[0])
    df['user'] = user
    df['message'] = messages
    df.rename(columns={'message_date': 'date'}, inplace=True)  # renaming the column
    df.drop(columns=['user_message'], inplace=True)  # drop the user_message column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['only_date'] = df['date'].dt.date
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['day_name'] = df['date'].dt.day_name();
    df['minute'] = df['date'].dt.minute
    return df
