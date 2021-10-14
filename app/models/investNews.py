class InvestNews:
    '''
    News class to define News Objects
    '''
    def __init__(self,title,description,publishedAt,content,url,source_name,img_url,agoTime):
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.source_name = source_name
        self.img_url = img_url
        self.agoTime = agoTime