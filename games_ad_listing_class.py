from db_class import *

# Define a class Games

class Games(Connectdb):

# Define methods

    # Shows one game ad in the table
    def read_one(self, game):
        query = self.filter_query(f"SELECT * FROM GamesList WHERE Game = '{game}'").fetchone()
        return query

    # Shows all game ads in the table
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

    # Update one game ad in the table
    def update_one(self, column, updated_value, name):
        self.filter_query(f"UPDATE GamesList SET {column} = '{updated_value}' WHERE Game = '{name}'")
        self.conn_db.commit()

    # Deletes one recipe from the recipe table
    def destroy_one(self, name):
        self.filter_query(f"DELETE FROM GamesList WHERE Game = '{name}'")
        self.conn_db.commit()

    # Gets one position from table
    def read_position_seller(self, name):
        query = self.filter_query(f"SELECT Position FROM GamesList WHERE Seller = '{name}'").fetchone()[0]
        return query

    def read_position_game(self, name):
        query = self.filter_query(f"SELECT Position FROM GamesList WHERE Game = '{name}'").fetchone()[0]
        return query

    # Returns position info from looking up postcode returned from table on postcodes.io api
    def add_lat_and_long(self, name):
        got_position = self.read_position_game(name)
        request_position = requests.get(f"http://api.postcodes.io/postcodes/{got_position}".lower().strip())
        converted_position = request_position.json()
        latitude = converted_position['result']['latitude']
        longitude = converted_position['result']['longitude']
        self.update_one('latitude', latitude, name)
        self.update_one('longitude', longitude, name)
        return latitude, longitude

    # Tuple to string converter
    def convertTuple(self, tup):
        str = ''.join(tup)
        return str

    # Sets up seller list
    def seller_list(self):
        query = self.filter_query(f"SELECT Seller FROM GamesList")
        seller_list = []
        while True:
            for record in query:
                converted_query = self.convertTuple(record)
                seller_list.append(converted_query)
                if record is None:
                    break
            return seller_list

    # Gets one phone from table
    def read_phone(self, name):
        query = self.filter_query(f"SELECT Phone FROM GamesList WHERE Seller = '{name}'").fetchone()[0]
        return query