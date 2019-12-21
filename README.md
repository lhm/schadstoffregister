# Pollutant Release and Transfer Register

Data from the german PRTR ("Schadstoffregister")

Source: [CSV_PRTR-Export_GERMANY_2019-11-25.zip](https://www.thru.de/fileadmin/SITE_MASTER/content/Dokumente/Downloads/01_Topthemen/PRTR-Daten_2017/CSV_PRTR-Export_GERMANY_2019-11-25.zip)

Publisher [Umweltbundesamt - Thru.de](https://www.thru.de)

## Preparation

```
make data/prtr-emissions.csv
```

This will download the zipped data, extract and do some minor cleanup, putting the results in the data directory.

To create a file in Geojson format using the contained spatial data:
```
make data/prtr-emissions.geojson
```

## Notes

Currently only releases to air ("Freisetzungen") are processed. The original dataset also contains data about release to land and water.

## Requirements

Python3 is used, all dependencies are installed automatically into a Virtualenv
when using the `Makefile`.

## License

The Python files in `scripts` are released under an
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).

Use of data is subject to the [terms of use](https://www.thru.de/index.php?id=479&L=3) from Thru.de:
```
We permit and encourage both downloading and any other use of the information available on Thru.de, in compliance with the following conditions:
  - you must credit Thru.de as the source of the information, and
  - the contents of the information may be neither changed, falsified nor otherwise used in an unlawful manner.
```
