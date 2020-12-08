# -*- coding: utf-8 -*-
# Where to store SQLite database
path_db = '/var/ttn_tracker/ttn_tracker_database.db'

# Period to download new data and display on the map (recommended not to go lower than 10 seconds)
refresh_period_seconds = 15

# Where the map initially loads
start_lat = 47.896998
start_lon = 7.8968636

# TTN Application
application = "buehl-ttgo-ttn-mapper"
app_key = "70B3D57ED00203F6"

# Application devices
devices = [
    "ttgo-t-beam-esp32-ttnmapper",
    "ttgo-t-beam-esp32-ttnmapper-2"
]

# Where to place gateway markers
gateway_locations = [
    ('Viktors Gateway 01', 47.89693136, 7.89731799),
    ('Gateway 02', 47.8972000, 7.89600)
]

bing_api_key = ''


def config_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=path_db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
