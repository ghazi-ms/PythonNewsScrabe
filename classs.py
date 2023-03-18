class news:
    def __init__(self, title, link):
        self.title=title
        self.link=link

    def __str__(self):
        return ("the title is :"+self.title+", the link is:"+self.link)

    def GetTitle(self):
        return str(self.title)

    def GetLink(self):
        return str(self.link)
