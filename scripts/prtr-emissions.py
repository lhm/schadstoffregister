import pandas as pd
from utils import root

infile = root / 'files/2019-11-25_PRTR-Deutschland_Freisetzungen.csv'
outfile = root / 'data/prtr-emissions.csv'

df = pd.read_csv(
        infile,
        sep=';',
        encoding='latin1',
        dtype={
            'plz': object,
            'schutzgrund_fracht': object,
            'confidential_reason_release': object,
            'haupttaetigkeit': object,
            'nace_id': object
        },
        na_values=['-', '--', '_', '.']
)

# TODO plz D-69181

df.to_csv(outfile, index=False)
