import pandas as pd
import geopandas
from utils import root

infile = root / 'data/prtr-emissions.csv'
outfile = root / 'data/prtr-emissions.geojson'

df = pd.read_csv(
        infile,
        dtype={
            'jahr': 'int64', # prevent geopandas errors from pd.Int64
            'plz': object,
            'schutzgrund_fracht': object,
            'confidential_reason_release': object,
            'haupttaetigkeit': object,
            'nace_id': object
        }
)

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.geo_long_wgs84, df.geo_lat_wgs84))
gdf.to_file(outfile, driver='GeoJSON')