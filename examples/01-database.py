import transcine
import os

DATABASE_PATH = os.path.join(os.getcwd(), "data", "databases", "database.duckdb")

db = transcine.Database(DATABASE_PATH)

print(db.get_tables())

db.create_table(
    "videos", # nom de la table
    {"uuid" : "TEXT", # colonnes de la table + type de donnée de la colonne
     "video_path": "TEXT", 
     "title" : "TEXT", 
     "year" : "INT", 
     "duration" : "FLOAT", 
     "width" : "INT", 
     "height" : "INT"} 
)

# db.add_entry({"id":"vid1", "name":"hello world"})