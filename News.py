from datetime import datetime


class News:
    """
        Represents a news article with its title, link, source, description, location, and entities.
    """

    def __init__(self, title, link, source, time):
        self.id = ''
        self.title = title
        self.link = link
        self.description = ""
        self.location = ""
        self.newsSource = source
        self.timeStamp = self.format_date(time)
        self.points = []

    def format_date(self, unformatted_date):
        formatted_date = ""
        if self.newsSource == 'roya':
            parsed_date = datetime.strptime(unformatted_date, "%Y-%m-%dT%H:%M:%S%z")
            formatted_date = parsed_date.strftime("%m/%d/%Y, %H:%M:%S")
        elif self.newsSource == 'alghad':
            date_object = datetime.strptime(unformatted_date, "%a, %d %b %Y %H:%M:%S %Z")
            formatted_date = date_object.strftime("%m/%d/%Y, %H:%M:%S")
        if formatted_date == "":
            formatted_date = unformatted_date

        return formatted_date

    def __str__(self):
        """return the data elements as a string."""
        return "the title is :" + self.title + ",\n the link is:" + self.link + "\n the Description\n" + \
               self.description + "\n the loc:" + self.location + "\n the time:" + self.timeStamp

    def __eq__(self, other):
        """check if the given object is equal to this object."""
        if isinstance(other, self.__class__):
            return self.title == other.title
        return False

    def arabic_text_to_small_sum(self, arabic_text, modulus=1000):
        """
            Converts the given Arabic text to a small sum.
            :param arabic_text: The Arabic text to convert.
            :param modulus: The modulus to use.
            :return: None
        """
        # Use the ord() function to get the Unicode code point of each character in the Arabic text string
        code_points = [ord(c) for c in arabic_text]

        # Compute the sum of the code points
        total_sum = sum(code_points)

        # Take the modulo of the sum with a smaller number
        small_sum = total_sum % modulus
        if self.id != 1 or self.id != 2:
            self.id = small_sum

    def get_source(self):
        """
            Gets the news source.
            :return: The news source.
        """
        return self.newsSource

    def to_dictionary(self):
        """
            Converts the news to a dictionary.
            :return: The dictionary.
        """
        self.arabic_text_to_small_sum(self.title)
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "Coordinates": self.points,
            "Locations": self.location,
            "timeStamp": self.timeStamp,
            "newsSource": self.newsSource
        }

    def set_points(self, updated_points):
        """
            Sets the points.
            :param updated_points: The updated points.
            :return: None
        """
        self.points = updated_points

    def get_points(self):
        """
            Gets the points.
            :return: The points.
        """
        return self.points

    def get_title(self):
        """
            Gets the title.
            :return: The title.
        """
        return str(self.title)

    def get_link(self):
        """
            Gets the link.
            :return: The link.
        """
        return str(self.link)

    def get_location(self):
        """
            Gets the location.
            :return: The location.
        """
        return str(self.location)

    def set_location(self, location):
        """
            Sets the location.
            :param location: The location.
            :return: None
        """
        self.location = location

    def add_location(self, location):
        """
            Adds the location.
            :param location: The location.
            :return: None
        """
        if self.location == "":
            self.location = location
        else:
            self.location = self.location + "," + location

    def get_timestamp(self):
        """
            Gets the timestamp.
            :return: The timestamp.
        """
        return str(self.timeStamp)

    def set_timestamp(self, timestamp):
        """
            Sets the timestamp.
            :param timestamp: The timestamp.
            :return: None
        """
        self.timeStamp = timestamp

    def set_description(self, description):
        """
            Sets the description.
            :param description: The description.
            :return: None
        """
        self.description = description

    def get_description(self):
        """
            Gets the description.
            :return: The description.
        """
        return str(self.description)
