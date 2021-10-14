class StoryNews:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self, idNumber, name, publishedAt, title, description, url, img_url, source_url):
        self.name = name
        self.publishedAt = publishedAt
        self.title = title
        self.description = description
        self.url = url
        self.img_url = img_url
        self.source_url = source_url
