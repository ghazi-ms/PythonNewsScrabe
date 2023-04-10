import time


class news:

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.description = ""
        self.location = ""
        self.timeStamp = time.time()

    def __str__(self):
        return "the title is :" + self.title + ",\n the link is:" + self.link + "\n the Description\n" + self.description + "\n the loc:" + self.location + "\n the time:" + self.timeStamp

    def getIntoList(self,points):
        return {
        "id": 'id'+self.timeStamp,
        "title": self.title,
        "description": self.description,
        "points": points,
        "timeStamp": self.timeStamp
        }

    def GetTitle(self):
        return str(self.title)

    def GetLink(self):
        return str(self.link)

    def Getlocation(self):
        return str(self.location)

    def SetLocation(self, Loc):
        self.location = Loc

    def GettimeStamp(self):
        return str(self.timeStamp)

    def SettimeStamp(self, timestamp):
        self.timeStamp = timestamp

    def Setdescription(self, description):
        self.description = description

    def Getdescription(self):
        return str(self.description)
