# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import df_functions as dff  # pandas Dataframe functions for cleaning and counting

# Creating global list to append tweet data


# Setting a max amount of tweets to fetch as global var
max_tweets = 500
tweet_list = []


def fetch_topic(keyword):
    # Scrape and append tweets to tweet_list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()):
        if i >= max_tweets:  # number of tweets to scrape
            break

        # Add the tweet to the list
        tweet_list.append([tweet.content])


def app(topic):

    if topic == "programming":
        # Programming languages, hardcoded for now
        topic_keywords = ['python', 'javascript', 'java', 'c++']

        fetch_topic('#programming')
        fetch_topic('#code')

    elif topic == 'sql':
        # SQL flavors, hardcoded for now
        topic_keywords = ['sqlserver', 'postgresql',
                          'mysql', 'sqlite']
        fetch_topic('#sql')
        fetch_topic('#database')

    # Create a DataFrame from the list of tweets
    tweet_df = dff.create_tweet_dataframe(tweet_list)

    # Replace punctuations with blanks and lowercase strings
    tweet_df = dff.clean_dataframe(tweet_df)

    # Convert tweet_df into a dataframe containing keywords used in tweets and their frequencies
    tweet_word_count = dff.get_tweet_word_count(tweet_df)

    tweet_word_count = dff.drop_words(topic_keywords, tweet_word_count)

    return tweet_word_count
