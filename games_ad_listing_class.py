from db_class import *

# Define a class Games

class Games(Connectdb):

# Define methods

    # Shows one recipe in the recipe table
    def read_one(self, game):
        query = self.filter_query(f"SELECT * FROM Recipes WHERE Game = '{game}'").fetchone()
        return query

    