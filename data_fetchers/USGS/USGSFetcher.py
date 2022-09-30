"""
Tool for fetching earthquake data from USGS.
Results are exported to GeoJSON file.
"""



import requests
import pandas as pd
import geopandas as gpd
from pathlib import Path
import datetime

from quakes_api.settings import DATA_DIR



# LEVELS and PERIODS are based on the USGS API specification
LEVELS = {'1.0', '2.5', '4.5', 'significant', 'all'}
PERIODS = {'hour', 'day', 'week', 'month'}
# URL for creating the requests - {} will be filled with the values from LEVELS nad PERIODS sets
URL = "	 https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_{}.geojson"

EXPORT_PATH = Path(DATA_DIR, "USGS")

class USGSFetcher:
    """
        Some documentation
    """

    def __init__(self, level, period):
        if level not in LEVELS:
            raise ValueError("Bad level value. Choose one from: " + str(LEVELS))
        if period not in PERIODS:
            raise ValueError("Bad level value. Choose one from: " + str(PERIODS))

        self.request_url = URL.format(level, period)
        self.name = f"{level}{period}"

        try:
            r = requests.get(self.request_url)
        except requests.exceptions.RequestException as e:
            raise IOError(e)
        
        self.data = r.json()

    def __str__(self):
        return f"Requests URL: {self.request_url}, Features: {len(self)}"

    def __len__(self):
        return len(self.data["features"])

    def fetchData(self):
        """
            Fetches the data to GeoPandas dataframe.
        """
        df = gpd.GeoDataFrame()
        for i, feature in enumerate(self.data['features']):
            
            coordinates = feature["geometry"]["coordinates"]

            geometry = gpd.points_from_xy([coordinates[0]], [coordinates[1]])

            row = gpd.GeoDataFrame(feature["properties"], index=[i], geometry=geometry, crs='EPSG:4326')
            row = row[['mag', 'place', 'time', 'type', 'title', 'geometry']]
            df = pd.concat([df, row])
    
        return df

    def exportData(self,):
        """
            Writes data to geojson file.
        """
        df = self.fetchData()
        identifier = str(datetime.datetime.now()).replace(" ", "-")
        path = Path(EXPORT_PATH / f"USGS_{identifier}_{self.name}.geojson")
        df.to_file(path, driver="GeoJSON")

        return path


