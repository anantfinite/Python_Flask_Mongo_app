#controller services here

from bson import ObjectId
from fastapi import APIRouter
from pyparsing import Optional
from models.user import User
from config.db import conn
#from hrms_schemas.user import userEntity,usersEntity
from typing import Optional
from mflix_schema.user import userEntity, usersEntity

user = APIRouter()

@user.get('/')
async def find_all_movies():
    
    print(usersEntity(conn.movie_db_atlas.small_mflix.find().limit(1)))
    return usersEntity(conn.movie_db_atlas.small_mflix.find())
    #return {"messge": "successfully output performed"}

@user.get('/')
async def find_all_movies():
    print("-----------")
    #print(conn.local.user.find())
    print(usersEntity(conn.movie_db_atlas.small_mflix.find()))
    print("---------------")
    return usersEntity(conn.movie_db_atlas.small_mflix.find())

@user.get("/find_by_id/{id}")
async def find_by_id(id):
    return userEntity(conn.movie_db_atlas.small_mflix.find_one({"_id":ObjectId(id)}))



@user.get("/find_by_genere_war_Short_Drama/")
async def find_by_genere(genres: str):
    return usersEntity(conn.movie_db_atlas.small_mflix.find({"genres":genres}))    
    
from fastapi import Path
@user.get("/rating_gte/")
#async def find_by_rating(imdb: float,tomato:int=Path(...,gt=0) ):
async def find_by_rating(imdb: Optional [float],tomato=None ):

    query = {"$or": [{"imdb.rating": {"$gte":imdb}},{"tomatoes.viewer.rating": {"$gte":tomato}}]}
   #{"imdb.rating": {"$gte":imdb}}
    return usersEntity(conn.movie_db_atlas.small_mflix.find(query))



# @user.put('/{id}')
# async def update_things(id, user : User):
#     #structure =userEntity(conn.movie_db_atlas.small_mflix.find_one({"_id":ObjectId(id)}))
#     conn.movie_db_atlas.small_mflix.find_one_and_update({"_id":ObjectId(id)},
#     {
#         "$set" : dict(user)
#     })
#     #print("---------------")
#     #first update and then return using usersEntity, or else it will return before updating

#     return userEntity(conn.movie_db_atlas.small_mflix.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def Delete_things(id):
    conn.movie_db_atlas.small_mflix.find_one_and_delete({"_id":ObjectId(id)})
    return {"message":"successfully deleted"}




