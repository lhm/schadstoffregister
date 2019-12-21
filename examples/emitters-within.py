import geopandas
import matplotlib.pyplot as plt
from pathlib import Path

root = Path(__file__).parents[1]

def load_data():
    df = geopandas.read_file(root / 'data/prtr-emissions.geojson')
    data = df[(df.jahr == 2017) & (df.bundesland == "Sachsen")]
    cols = ['betriebsname', 'plz', 'ort', 'geometry']
    data = data[cols]
    return data

def load_areas():
    return geopandas.read_file(root / 'examples/landkreise-sn.geojson')

def filter_by_area(data, area):
    return geopandas.sjoin(data, area, op='within')

def plot(data, area):
    fig, ax = plt.subplots(figsize = (10,6))
    area.plot(color=None, edgecolor='k', linewidth = 2, ax=ax)
    data.plot(color='red', ax=ax)

def emitters_in_leipzig():
    areas = load_areas()
    data = load_data()
    lei = areas.loc[[10]]
    res = filter_by_area(data, lei)
    plot(res, lei)
    plt.show()

if __name__ == '__main__':
    emitters_in_leipzig()
