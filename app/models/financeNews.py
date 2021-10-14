class FinanceNews:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self, idNumber, name, description, publishedAt, agoTime, url, source_name, img_url, source_url, topic): #, tag_terms, nasdaq_tickers):
        self.idNumber = idNumber
        self.name = name
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.img_url = img_url
        self.source_name = source_name
        self.source_url = source_url
        self.topic =  topic
        #self.tag_terms = tag_terms
        #self.nasdaq_tickers = nasdaq_tickers
        self.agoTime =agoTime