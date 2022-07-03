from pymongo import MongoClient, mongo_client

#conn = MongoClient()
#this database contains 15 documents
conn = MongoClient("mongodb+srv://anantkr:Samsungindia@mflixcluster.xasm1.mongodb.net/?retryWrites=true&w=majority")

#this connection contains COMPLETE documents
#conn = pymongo.MongoClient("mongodb+srv://m220student:<password>@mflix.3ek6q.mongodb.net/?retryWrites=true&w=majority")





#db = client.test
#conn = MongoClient("mongogb://localhost:27017/test")

#db = conn.movie_db_atlas

# collection = db.movie_db_atlas
# #print(client.stats)
# #t= client.list_database_names()
# t= conn.movie_db_atlas.small_mflix
# print(t.count_documents({}))
