import streamlit as st
#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd
import scraper
import altair as alt


st.sidebar.image("img/twitter_logo.png", width=50)

st.sidebar.title("TWITTER SCRAPER")
st.sidebar.write(
    "Check what programming language or SQL flavor is trending on twitter by clicking on the buttons below")
language_button = st.sidebar.button('Programming Language')
sql_button = st.sidebar.button('SQL Flavor')


if language_button:
    #st.success('Fetching tweets....')
    with st.spinner('Fetching tweets...'):

        tweet_word_count = scraper.app('programming')
        # Reset index again on the new df
        tweet_word_count.reset_index(drop=True, inplace=True)

        # Display the table of words and their frequency
        st.write(tweet_word_count)

        # Create a barchart to visualize the searchwords and their frequency, Clear titles
        test_chart = alt.Chart(tweet_word_count).mark_bar().encode(
            y=alt.Y('Word:O', title=''),
            x=alt.X('Frequency:Q', title=''),
            opacity=alt.value(0.9),

            # Set customized color scheme
            color=alt.Color('Word', legend=None,
                            scale=alt.Scale(
                                domain=tweet_word_count.sort_values(
                                    ['Frequency'])['Word'].tolist(),
                                range=['#ff9c8a', '#ffec8a', '#c5ff8a', '#8affa7']))).configure_axis(grid=False)
        st.altair_chart(test_chart, use_container_width=True)
    st.success('Success!')


elif sql_button:
    #st.success('Fetching tweets....')
    with st.spinner('Fetching tweets...'):

        tweet_word_count = scraper.app('sql')
        # Reset index again on the new df
        tweet_word_count.reset_index(drop=True, inplace=True)

        # Display the table of words and their frequency
        st.write(tweet_word_count)

        # Create a barchart to visualize the searchwords and their frequency, Clear titles
        test_chart = alt.Chart(tweet_word_count).mark_bar().encode(
            y=alt.Y('Word:O', title=''),
            x=alt.X('Frequency:Q', title=''),
            opacity=alt.value(0.9),

            # Set customized color scheme
            color=alt.Color('Word', legend=None,
                            scale=alt.Scale(
                                domain=tweet_word_count.sort_values(
                                    ['Frequency'])['Word'].tolist(),
                                range=['#ff9c8a', '#ffec8a', '#c5ff8a', '#8affa7']))).configure_axis(grid=False)
        st.altair_chart(test_chart, use_container_width=True)
    st.success('Success!')
