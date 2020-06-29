"""
TerrainLayer
===========

Extruded terrain using AWS Open Data Terrain Tiles and Mapbox Satellite imagery
"""

import pydeck
import os

# Import Mapbox API Key from environment
MAPBOX_API_KEY = os.environ["MAPBOX_API_KEY"]

# AWS Open Data Terrain Tiles
TERRAIN_IMAGE = '"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"'

# Define how to parse elevation tiles
ELEVATION_DECODER = {"rScaler": 256, "gScaler": 1, "bScaler": 1 / 256, "offset": -32768}

SURFACE_IMAGE = '"https://api.mapbox.com/v4/mapbox.satellite/{{z}}/{{x}}/{{y}}@2x.png?access_token={}"'.format(
    MAPBOX_API_KEY
)

terrain_layer = pydeck.Layer(
    "TerrainLayer", data=None, elevation_decoder=ELEVATION_DECODER, texture=SURFACE_IMAGE, elevation_data=TERRAIN_IMAGE
)

view_state = pydeck.ViewState(latitude=46.24, longitude=-122.18, zoom=11.5, bearing=140, pitch=60)

r = pydeck.Deck(terrain_layer, initial_view_state=view_state)

r.to_html("terrain_layer.html", notebook_display=False)
