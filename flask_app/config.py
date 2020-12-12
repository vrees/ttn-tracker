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
app_key = "key ttn-account-v2.t1A5JKlhe47sPKS596YtrvEzJ3UMwFtgoboTwaIqEYw"

# Application devices
devices = [
    "ttgo-t-beam-esp32-ttnmapper",      // green housing
    "ttgo-t-beam-esp32-ttnmapper-2",    // blue housing
    "ttgo-t-beam-esp32-ttnmapper-3",
    "ttgo-t-beam-esp32-ttnmapper-4"
]

# Where to place gateway markers
gateway_locations = [
    ('Buehl/Hofsgrund 01', 47.89693136, 7.89731799),
    ('bn_Schauinsland 02', 47.9098484, 7.8913307)
]

bing_api_key = ''


def config_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=path_db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
