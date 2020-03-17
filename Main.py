import ServerApplication
import time
import re

# We can move these resource paths to a config file

accounts_resource = "Resources/AccountNames.json"
user_tweet_map_resource = "Resources/UserTweetIDMap.json"
firestore_credentials_resource = "Resources/service-account-file.json"

server_app = ServerApplication.ServerApplication(accounts_resource, user_tweet_map_resource,
                                                 firestore_credentials_resource)

var = 1
while var == 1:  # This constructs an infinite loop
    server_app.run()
    time.sleep(120)

