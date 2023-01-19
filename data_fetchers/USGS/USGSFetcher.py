"""
Tool for fetching earthquake data from USGS.
Results are exported to GeoJSON file.
"""


import requests
import pandas as pd
import geopandas as gpd
from pathlib import Path
import datetime


# for testing in developoment
try:
    from quakes_api.settings import DATA_DIR
except ModuleNotFoundError:
    DATA_DIR = "../../data"

# LEVELS and PERIODS are based on the USGS API specification
MODES = {"feed", "fdsnws"}
LEVELS = {"1.0", "2.5", "4.5", "significant", "all"}
PERIODS = {"hour", "day", "week", "month"}
# URL for creating the requests - {} will be filled with the values from LEVELS nad PERIODS sets

URL_FDSNWS = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}"
URL_FEED = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_{}.geojson"


class USGSFetcher:
    """
    Get data from USGS API
    YY / MM / DD
    MODES = {'feed', 'fdsnws'}
    LEVELS = {'1.0', '2.5', '4.5', 'significant', 'all'}
    PERIODS = {'hour', 'day', 'week', 'month'}
    """

    def __init__(
        self,
        mode="feed",
        level="all",
        period="day",
        starttime="2022-11-11",
        endtime="2022-11-12",
    ):
        if level not in LEVELS:
            raise ValueError("Bad level value. Choose one from: " + str(LEVELS))
        if period not in PERIODS:
            raise ValueError("Bad period value. Choose one from: " + str(PERIODS))
        if mode not in MODES:
            raise ValueError("Bad mode value. Choose one from: " + str(MODES))

        self.mode = mode

        if mode == "feed":
            self.request_url = URL_FEED.format(level, period)
            self.name = f"{level}{period}"
            self.EXPORT_PATH = Path(DATA_DIR, "USGS")
        else:
            self.starttime = starttime
            self.endtime = endtime
            self.request_url = URL_FDSNWS.format(starttime, endtime)
            self.name = f"{mode.upper()}{starttime}{endtime}"
            self.EXPORT_PATH = Path(DATA_DIR, "USGS", "export")

        # create dir
        self.EXPORT_PATH.mkdir(parents=True, exist_ok=True)
        try:
            r = requests.get(self.request_url)
        except requests.exceptions.RequestException as e:
            raise IOError(e)
        print(self.request_url)
        self.data = r.json()

    def __str__(self):
        return f"Requests URL: {self.request_url}, Features: {len(self)}"

    def __len__(self):
        return len(self.data["features"])

    def transformData(self):
        """
        Fetches the data to GeoPandas dataframe.
        """
        df = gpd.GeoDataFrame()

        for i, feature in enumerate(self.data["features"]):

            # copy id from feature['id'] to feature['properties']
            feature["properties"]["id"] = feature["id"]

            coordinates = feature["geometry"]["coordinates"]

            geometry = gpd.points_from_xy([coordinates[0]], [coordinates[1]])

            row = gpd.GeoDataFrame(
                feature["properties"], index=[i], geometry=geometry, crs="EPSG:4326"
            )
            row = row[
                ["id", "mag", "place", "time", "type", "title", "code", "geometry"]
            ]
            df = pd.concat([df, row])

        return df

    def exportData(
        self,
    ):
        """
        Download, transform and write data to geojson file.
        """
        df = self.transformData()
        identifier = str(datetime.datetime.now()).replace(" ", "-")
        path = Path(self.EXPORT_PATH / f"USGS_{identifier}_{self.name}.geojson")
        print(path)
        df.to_file(path, driver="GeoJSON")
        return path
