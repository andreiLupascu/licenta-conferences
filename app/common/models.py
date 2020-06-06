# class Event:
#     def __init__(self, type, description, program):

class Conference:
    def __init__(self, title, path_to_logo, location, path_to_description, country, start_date, end_date):
        self.title = title
        self.path_to_logo = path_to_logo
        self.location = location
        self.path_to_description = path_to_description
        self.country = country
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f'Title: {self.title}; Logo: {self.path_to_logo}; Location: {self.location}; Description: {self.path_to_description}; Country: {self.country}; Start Date: {self.start_date}; End date: {self.end_date} '
    # def add_event(self, event):
