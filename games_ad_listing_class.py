from db_class import *

# Define a class Games

class Games(Connectdb):

# Define methods

    # Shows one game in the table
    def read_one(self, game):
        query = self.filter_query(f"SELECT * FROM GamesList WHERE Game = '{game}'").fetchone()
        return query

    # Shows all games in the table
    def read_all(self):
        query = self.filter_query(f"SELECT * FROM GamesList")
        while True:
            record = query.fetchone()
            if record is None:
                break
            print('GameAdID:', record[0], 'Game: ' + record[1], 'Seller: ' + record[2], 'Phone: ' + record[3], 'Price: ' + record[4], 'Position: ' + record[5], 'Latitude: ' + record[6], 'Longitude: ' + record[7])

    # Creates new game ad in the table
    def new(self, game, seller, phone, price, position, latitude, longitude):
        self.filter_query(f"INSERT INTO GamesList (Game, Seller, Phone, Price, Position, Latitude, Longitude) VALUES {game, seller, phone, price, position, latitude, longitude}")
        self.conn_db.commit()