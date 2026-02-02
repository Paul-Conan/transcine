import duckdb
import os


class Database:
    def __init__(self, path):
        self.path = path # on donne le chemin d'un fichier bdd

        if os.path.isfile(path): # si ce fichier bdd existe, ok on connecte c'est cool
            self.db = duckdb.connect(self.path)
        else: # sinon on vérifie si le dossier existe
            if os.path.isdir(os.path.split(path)[0]): # si oui 
                self.db = duckdb.connect(self.path)
            else: # si non, on crée d'abord le dossier au bon endroit
                os.makedirs(os.path.split(path)[0], exist_ok = True)
                self.db = duckdb.connect(self.path)

    def get_tables(self): # fonction pour connaître le nombre de tables ; surtout utile pour déboggage
        return self.db.execute("SHOW TABLES").fetchall()

    def create_table(self, table_name, table_dict):
        execute_string = f"CREATE TABLE {table_name}("
        for header_name in table_dict:
            execute_string = execute_string + f"{header_name} {table_dict[header_name]}, "
        execute_string = execute_string[:-2] + ")" # le [:-2] retire le ", " en trop à la fin du string
        # ça donne ce string : CREATE TABLE video(video_path TEXT, ...... width INT)
        self.db.execute(execute_string)

    def remove_table(self, table_name):
        self.db.execute(f"DROP TABLE IF EXISTS {table_name}")

    def add_entry(self, items):
        
        
        
        
        placeholders = ", ".join("?" for _ in items)
        self.db.execute(f"INSERT INTO videos VALUES ({placeholders})", items)