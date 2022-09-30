from USGSFetcher import USGSFetcher

import pandas as pd
import geopandas as gpd

f = USGSFetcher("1.0", "week")

print(str(f))

print(len(f))



df = f.fetchData()
print(df.head())


f.exportData()
