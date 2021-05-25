import pandas as pd
import random
from datetime import datetime


class Controller:

    medias = ["TSN", "Hromadske", "UkrPravda", "24tv"]

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def get_entities_from_media(self, entity_name, field, media):
        entities = self.model.get_all_named_entities_of_media(entity_name=entity_name, field=field, media=media)
        series = pd.Series(entities["named_entities"])
        return series.value_counts()

    def get_entities(self, entity_name, field):
        entities = self.model.get_all_named_entities(entity_name=entity_name, field=field)
        series = pd.Series(entities)
        return series.value_counts()

    def parse_user_input(self):

        choose = None
        while choose != "0":
            self.view.print_menu()
            choose = input("Enter a number : ")
            # top 10 popular tags
            if choose == "1":
                number = 10
                tags = self.model.get_all_tags("tags")
                series = pd.Series(tags)
                print(series.value_counts().nlargest(number).to_string())

            # top 20 locations(Texts)
            if choose == "2":
                number = 20
                print(self.get_entities(entity_name="I-LOC", field="news_text").nlargest(number).to_string())

            # top 20 people(Texts)
            if choose == "3":
                number = 20
                print(self.get_entities(entity_name="I-PER", field="news_text").nlargest(number).to_string())

            # top 7 locations(Titles)
            if choose == "4":
                number = 7
                print(self.get_entities(entity_name="I-LOC", field="title").nlargest(number).to_string())

            # top 7 people(Titles)
            if choose == "5":
                number = 7
                print(self.get_entities(entity_name="I-PER", field="title").nlargest(number).to_string())
            if choose == "6":
                number = 5
                media = self.get_random_media()
                print(media)
                print(self.get_entities_from_media(entity_name="I-PER", field="news_text", media=media)
                      .nlargest(number).to_string())
            if choose == "7":
                number = 5
                media = self.get_random_media()
                print(media)
                print(self.get_entities_from_media(entity_name="I-LOC", field="news_text", media=media)
                      .nlargest(number).to_string())
            if choose == "8":
                number = 5
                media = self.get_random_media()
                print(media)
                print(self.get_entities_from_media(entity_name="I-PER", field="title", media=media)
                      .nlargest(number).to_string())
            if choose == "9":
                number = 5
                media = self.get_random_media()
                print(media)
                print(self.get_entities_from_media(entity_name="I-LOC", field="title", media=media)
                      .nlargest(number).to_string())
            if choose == "10":
                data = []
                for media in self.medias:
                    data.append(self.model.get_polarity_from_media(field="title", media=media))
                self.view.show_bar_chart(data, self.medias, "Polarity Chart", "Medias", "Polarities")
            if choose == "11":
                data = []
                for media in self.medias:
                    data.append(self.model.get_polarity_from_media(field="news_text", media=media))
                self.view.show_bar_chart(data, self.medias, "Polarity Chart", "Medias", "Polarities")
            if choose == "12":
                number = 5
                named_entities_with_date = self.model.\
                    get_all_named_entities_with_date(entity_name="I-PER", field="news_text")
                data = {}
                for ne in named_entities_with_date:
                    ne["date"] = self.date_to_string(ne["date"])
                    if ne["date"] in data:
                        data[ne["date"]] = self.add_two_arrays(data[ne["date"]], ne["named_entities"])
                    else:
                        data[ne["date"]] = []

                for key, value in data.items():
                    print(key)
                    print(pd.Series(value).value_counts().nlargest(number).to_string())
                    print("\n")
                if choose == "13":
                    number = 5
                    named_entities_with_date = self.model. \
                        get_all_named_entities_with_date(entity_name="I-LOC", field="news_text")
                    data = {}
                    for ne in named_entities_with_date:
                        ne["date"] = self.date_to_string(ne["date"])
                        if ne["date"] in data:
                            data[ne["date"]] = self.add_two_arrays(data[ne["date"]], ne["named_entities"])
                        else:
                            data[ne["date"]] = []

                    for key, value in data.items():
                        print(key)
                        print(pd.Series(value).value_counts().nlargest(number).to_string())
                        print("\n")
            if choose == "0":
                break

    def get_random_media(self):
        n = random.randint(0, len(self.medias) - 1)
        return self.medias[n]

    def add_two_arrays(self, arr1, arr2):
        for e in arr2:
            arr1.append(e)
        return arr1

    def date_to_string(self, date):
        year = datetime.fromisoformat(date).year
        month = datetime.fromisoformat(date).month
        day = datetime.fromisoformat(date).day
        return "%s.%s.%s" % (day, month, year)
