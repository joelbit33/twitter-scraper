# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating global list to append tweet data


# Setting a max amount of tweets to fetch as global var
max_tweets = 25


def fetch_programming_lang():
    tweet_list = []
    # Using TwitterSearchScraper to scrape data and append tweets to list about programming languages
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#programming').get_items()):
        if i > max_tweets:  # number of tweets you want to scrape
            break
        # declare the attributes to be returned
        tweet_list.append(
            [tweet.rawContent])

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#code').get_items()):
        if i > max_tweets:  # number of tweets you want to scrape
            break
        # declare the attributes to be returned
        tweet_list.append(
            [tweet.rawContent])

    tweet_df = pd.DataFrame(tweet_list, columns=[
        'text'])
    # Replace punctuations with blanks and lower strings
    tweet_df['text'] = tweet_df['text'].str.lower(
    ).str.replace('[!,.":()#/-]', '', regex=True)

    # Creates a pandas Dataframe containing words from df that
    # are used in tweets and gets their frequency
    tweet_word_count = tweet_df.text.str.split(
        expand=True).stack().value_counts().reset_index()

    # Adds column names to the Dataframe
    tweet_word_count.columns = ['Word', 'Frequency']

    # Drop index

    # Programming languages
    prog_lang = ['python', 'javascript', 'java', 'c++']

    # Delete all words in dataframe that exists in stop_words
    for index, row in tweet_word_count.iterrows():
        if row['Word'] not in prog_lang:
            tweet_word_count.drop(index, inplace=True)

    return tweet_word_count


def fetch_sql_flavors():
    tweet_list = []
    # Using TwitterSearchScraper to scrape data and append tweets to list about sql flavors
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#sql').get_items()):
        if i > max_tweets:
            break
        tweet_list.append(
            [tweet.rawContent])

    tweet_df = pd.DataFrame(tweet_list, columns=[
        'text'])
    # Replace punctuations with blanks and lower strings
    tweet_df['text'] = tweet_df['text'].str.lower(
    ).str.replace('[!,."():#-/]', '', regex=True)

    # Creates a pandas Dataframe containing words from df that
    # are used in tweets and gets their frequency
    tweet_word_count = tweet_df.text.str.split(
        expand=True).stack().value_counts().reset_index()

    # Adds column names to the Dataframe
    tweet_word_count.columns = ['Word', 'Frequency']

    return tweet_word_count


# tweet_df.to_csv(f"csv_files/{user_input}.csv")
