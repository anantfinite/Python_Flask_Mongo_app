from pkg_resources import require
from pyparsing import Optional


def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "plot": item["plot"],
        "genres": item["genres"],
        "runtime": item["runtime"],
        "cast": item["cast"],
        #"num_mflix_comments": item["num_mflix_comments"], #11
        #"poster": Optional[str(item["poster"])], #11 not working
        "title": item["title"],
        #"fullplot": item["fullplot"], #11
        #"languages": item["languages"], #11
        "countries": item["countries"],
        "released": item["released"],
        "directors": item["directors"],
        "awards": item["awards"],
        #"rated": item["rated"], #11
        "lastupdated": item["lastupdated"],
        "year": item["year"],
        "imdb": item["imdb"],
        "type": item["type"],
        "tomatoes": item["tomatoes"],
    }

def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]

# class small_mflix(Document):
#     _id = IntField(require=False)
#     plot = StringField(require=False)
#     genres = ListField(require=False)
#     runtime = IntField(require=False)
#     cast = ListField(require=False)
#     num_mflix_comments = IntField(require=False)
#     poster = StringField(require=False)
#     title = StringField(require=False)
#     fullplot = StringField(require=False)
#     languages = ListField(require=False)
#     countries = ListField(require=False)
#     released = DateTimeField(require=False)
#     directors = ListField(require=False)
#     awards = ListField(require=False)
#     rated = DateTimeField(require=False)
#     awards = ListField(require=False)
#     lastupdated = StringField(require=False)
#     year = StringField(require=False)
#     imdb = ListField(require=False)
#     type = StringField(require=False)
#     tomatoes = ListField(require=False)


