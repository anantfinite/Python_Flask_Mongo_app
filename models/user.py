
from datetime import date
from pydantic import BaseModel
from typing import Optional



class User(BaseModel):

        plot:str
        genres:list
        runtime:str
        cast:list
        #num_mflix_comments:Optional[int]
        #poster:Optional[str]
        title:str
        #fullplot:Optional[str]
        #languages:Optional[list]
        countries:list
        released:date
        directors:list
        awards:list
        #rated:str
        lastupdated:str
        year:int
        imdb:list
        type: str
        tomatoes: list

    








# class User(BaseModel):
#     name :str
#     email: str
#     password : str


# class User(BaseModel):
#     name :str
#     age: int
#     teams : list
    

# user_list = [
#   User(**user) for user in users
# ]















