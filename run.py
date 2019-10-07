from games_ad_listing_class import *

db_games = Games()

# print(db_games.read_one('FIFA 20'))

# db_games.read_all()

# db_games.new('God of War', 'frensis97ferrari', '09182736450', '30', 'EC1V 0ES', '', '')

# db_games.update_one('Game','GTA V', 'God of War')

# print(db_games.add_lat_and_long('frensis97ferrari'))

# db_games.destroy_one('uhfsd')

start_input = ''

while start_input != 'neither':
    start_input = input('Welcome! This is SpartaGames! Would you like to BROWSE through our game listings, ADD a listing yourself, or NEITHER? ').lower()
    if start_input == 'add':
        login_input = input('Great! What is your username? ').lower()
        for user in db_games.seller_list():
            if user in login_input:
                q_game = input('What game would you like to sell? ').capitalize()
                phone = db_games.read_phone(login_input)
                q_price = input('For how much would you like to sell your game? ')
                position = db_games.read_position_seller(login_input)
                new_game = db_games.new(q_game, login_input, phone, q_price, position, '', '')
                q_lat_long = ''
                while q_lat_long != 'no':
                    q_lat_long = input('Game listed! Would you like to add latitude and longitude? ').lower()
                    if q_lat_long == 'yes':
                        db_games.add_lat_and_long(q_game)
                    elif q_lat_long == 'no':
                        print('No problem!')
                        break
                    else:
                        print("Didn't quite get that...")
            else:
                print('Login details not recognized, redirecting to welcome page...')
                break

    elif start_input == 'browse':
        db_games.read_all()
    elif start_input == 'neither':
        print('Fine suit yourself...')
    else:
        print('Not a valid input, please try again:')
