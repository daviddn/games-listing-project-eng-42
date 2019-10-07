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

    # Gets one position from table
    def read_position(self, name):
        query = self.filter_query(f"SELECT Position FROM GamesList WHERE Game = '{name}'").fetchone()[0]
        return query

    # Returns position info from looking up postcode returned from table on postcodes.io api
    def add_lat_and_long(self, name):
        got_position = self.read_position(name)
        request_position = requests.get(f"http://api.postcodes.io/postcodes/{got_position}".lower().strip())
        converted_position = request_position.json()
        latitude = converted_position['result']['latitude']
        longitude = converted_position['result']['longitude']
        self.update_one('latitude', {latitude}, name)
        self.update_one('longitude', {longitude}, name)
        return latitude, longitude
