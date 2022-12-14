import pandas as pd


def create_tweet_dataframe(tweet_list):
    df = pd.DataFrame(tweet_list, columns=['text'])
    return df


def clean_dataframe(tweet_df):
    tweet_df['text'] = tweet_df['text'].str.lower(
    ).str.replace('[!,.":()#/-]', '', regex=True)
    return tweet_df


def get_tweet_word_count(tweet_df):
    word_count = tweet_df.text.str.split(
        expand=True).stack().value_counts().reset_index()

    # Add column names to the DataFrame
    word_count.columns = ['Word', 'Frequency']
    return word_count


def drop_words(word_list, tweet_word_count):
    # Delete words in dataframe that does not exist in word_list
    for index, row in tweet_word_count.iterrows():
        if row['Word'] not in word_list:
            tweet_word_count.drop(index, inplace=True)
    return tweet_word_count
