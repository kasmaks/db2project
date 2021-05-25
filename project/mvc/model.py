import pymongo
from polyglot.text import Text
import pymorphy2
from db_settings.db_settings import DB


class Model:

    def __init__(self):
        self.conn = pymongo.MongoClient(DB.host, DB.port)
        db = self.conn[DB.db]
        self.data_coll = db[DB.collection]

    def get_all_named_entities(self, entity_name, field):
        named_entities = []
        counter = 0
        for news in self.data_coll.find({}, {field: 1}):
            news_text = news[field]
            if len(news_text) > 0:
                text = Text(news_text, hint_language_code="uk")
                self.get_named_entities_from_text(text, named_entities, entity_name)
                counter += 1
                print(counter)
                # if counter > 200:
                #     break
        return named_entities

    def get_named_entities_from_text(self, text, named_entities, entity_name):
        entities = text.entities
        for entity in entities:
            if entity.tag == entity_name and len(self.get_named_entity_from_entity(entity)) > 0:
                named_entities.append(self.get_named_entity_from_entity(entity))
        return named_entities

    def get_named_entity_from_entity(self, entity):
        named_entity = ""
        morph = pymorphy2.MorphAnalyzer(lang='uk')
        for e in entity:
            p = morph.parse(e)[0]
            if 'NOUN' in p.tag:
                named_entity += " " + p.normal_form
        return named_entity.strip().upper()

    def get_all_named_entities_with_date(self, entity_name, field):
        named_entities_with_date = []
        number_of_news = 0
        for news in self.data_coll.find({}, {field: 1, "date": 1}):
            date = news["date"]
            news_text = news[field]
            if len(news_text) > 0:
                text = Text(news_text, hint_language_code="uk")
                named_entities = self.get_named_entities_from_text(text, [], entity_name)
                named_entities_with_date.append({"date": date,
                                                 "named_entities": named_entities})
                number_of_news += 1
                print(number_of_news)
        return named_entities_with_date

    def get_all_named_entities_of_media(self, entity_name, field, media):
        named_entities = []
        number_of_news = 0
        for news in self.data_coll.find({"media": media}, {field: 1}):
            news_text = news[field]
            if len(news_text) > 0:
                text = Text(news_text, hint_language_code="uk")
                self.get_named_entities_from_text(text, named_entities, entity_name)
                number_of_news += 1
                print(number_of_news)
                # if number_of_news > 200:
                #     break
        named_entities_of_media = {"media": media,
                                   "named_entities": named_entities,
                                   "number_of_news": number_of_news}
        return named_entities_of_media

    def get_all_tags(self, field):
        all_tags = []
        for news in self.data_coll.find({}, {field: 1}):
            tags = news[field]
            for tag in tags:
                all_tags.append(tag.strip().upper())
        return all_tags

    def get_polarity_from_media(self, field, media):
        number_of_news = 0
        polarity_sum = 0
        for news in self.data_coll.find({"media": media}, {field: 1}):
            news_text = news[field]
            if len(news_text) > 0:
                text = Text(news_text, hint_language_code="uk")
                polarity_sum += text.polarity
                number_of_news += 1
        if number_of_news > 0:
            return polarity_sum / number_of_news
        return 0
