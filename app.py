import streamlit as st
import pickle
import pandas as pd

def recommend_youtube(youtube_name):
    yt_index = youtube[youtube['Youtuber'] == youtube_name].index[0]
    distances = similarity[yt_index]
    yt_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]

    recommended_yt = []
    for i in yt_list:
        Youtuber = youtube.iloc[i[0]].Youtuber
        recommended_yt.append(youtube.iloc[i[0]].Youtuber)
    return recommended_yt

yts_dict = pickle.load(open('yt_dict.pkl','rb'))
youtube = pd.DataFrame(yts_dict)

similarity = pickle.load(open('similarity_matrix.pkl','rb'))

st.title("YouTube Recommendation System")

selected_yt_name = st.selectbox(
'Enter a YouTube channel',
youtube['Youtuber'].values)


if st.button('Get Recommend'):
    names = recommend_youtube(selected_yt_name)
    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.success(names[0])
    with col2:
        st.success(names[1])
    with col3:
        st.success(names[2])
    with col1:
        st.success(names[3])
    with col2:
        st.success(names[4])
    with col3:
        st.success(names[5])
    with col1:
        st.success(names[6])
    with col2:
        st.success(names[7])
    with col3:
        st.success(names[8])

# Add custom text at the bottom using Markdown
st.markdown("---")
st.markdown("Copyright © Nadeem Akhtar. All Rights Reserved")



