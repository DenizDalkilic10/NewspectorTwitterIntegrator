from Models import TwitterAccount
from Models import Tweet
from Services import TwitterServices
from Services import FirestoreServices

accounts_resource = "../Resources/AccountNames.json"
user_tweet_map_resource = "../Resources/UserTweetIDMap.json"
firestore_credentials_resource = "../Resources/service-account-file.json"

twitter_service = TwitterServices.TwitterServices(accounts_resource, user_tweet_map_resource)
firestore_service = FirestoreServices.FireStoreServices(firestore_credentials_resource);

for i in twitter_service.user_tweet_map:
    profile = twitter_service.fetch_account_info(i)
    p = TwitterAccount.TwitterAccount(profile.username, profile.name, profile.followers_count, profile.following_count,
                                      profile.likes_count, profile.tweets_count, profile.website, profile.profile_photo,
                                      profile.birthday, profile.biography, list())

    firestore_service.add_twitter_account(p)

    tweets = twitter_service.fetch_latest_tweets_from_account(i, 1, twitter_service.user_tweet_map[i])

    if len(tweets) != 0:
        for tweet in tweets:
            t = Tweet.Tweet(p.username, tweet["tweetId"], tweet["isRetweet"], tweet["time"],
                            tweet["text"], tweet["replies"], tweet["retweets"], tweet["likes"],
                            tweet["entries"])
            p.add_tweets(t)

        for tweet in p.tweet_list:
            print("Account: " + p.username + " | Tweet: " + tweet.text + " | " + tweet.tweet_id)
            firestore_service.add_tweet(tweet)

        twitter_service.update_map(i, int(tweets[0]["tweetId"]))

twitter_service.save_map_to_resources(twitter_service.user_tweet_map, user_tweet_map_resource)
