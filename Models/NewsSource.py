# This is the model class of a news source which will store news and other related information about the source
class NewsSource(object):

    # instance attributes
    def __init__(self, name, numberoffollowers, location, website, newslist, latestdatefetchedinmillis):
        self.name = name
        self.numberOFFollowers = numberoffollowers
        self.location = location
        self.website = website
        self.newsList = newslist
        self.latestDateFetchedInMillis = latestdatefetchedinmillis

    def addnews(self, news):
        self.newsList += news

    def setnews(self, newslist):
        self.newsList = newslist
