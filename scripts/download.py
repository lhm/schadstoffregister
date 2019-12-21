import requests
from io import BytesIO
from zipfile import ZipFile
from utils import root
import requests_cache

cache = root / '.cache'
requests_cache.install_cache(str(cache))

url = 'https://www.thru.de/fileadmin/SITE_MASTER/content/Dokumente/Downloads/01_Topthemen/PRTR-Daten_2017/CSV_PRTR-Export_GERMANY_2019-11-25.zip'
response = requests.get(url)
response.raise_for_status()

content = response.content
zipfile = ZipFile(BytesIO(content))
filesdir = root / 'files'
zipfile.extractall(path=filesdir)

