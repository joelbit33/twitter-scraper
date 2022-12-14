# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating global list to append tweet data


# Setting a max amount of tweets to fetch as global var
max_tweets = 25


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


def fetch_programming_lang():

    tweet_list = []

    # Scrape and append tweets to list about programming languages
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#programming').get_items()):
        if i >= max_tweets:  # number of tweets to scrape
            break

        # Add the tweet to the list
        tweet_list.append([tweet.content])

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#code').get_items()):
        if i >= max_tweets:  # number of tweets to scrape
            break

        # Add the tweet to the list
        tweet_list.append([tweet.content])

    # Create a DataFrame from the list of tweets
    tweet_df = create_tweet_dataframe(tweet_list)

    # Replace punctuations with blanks and lowercase strings
    tweet_df = clean_dataframe(tweet_df)

    # Convert tweet_df into a dataframe containing keywords used in tweets and their frequencies
    tweet_word_count = get_tweet_word_count(tweet_df)

    # Programming languages, hardcoded for now
    prog_lang = ['python', 'javascript', 'java', 'c++']

    tweet_word_count = drop_words(prog_lang, tweet_word_count)

    return tweet_word_count
