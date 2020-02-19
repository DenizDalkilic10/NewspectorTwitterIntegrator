# This is the model class of a news
class News(object):

    # instance attributes
    def __init__(self, sourcename, headline, link, dateinmillis):
        self.sourceName = sourcename
        self.headline = headline
        self.link = link  # if present
        self.dateInMillis = dateinmillis


