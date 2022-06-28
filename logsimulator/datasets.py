import pandas as pd
import pkg_resources

def load_volve_19_dataset() -> pd.DataFrame:
    """Return a dataframe of well 15/9-19 from the Equinor Volve dataset.

    Contains the following fields:
        DEPTH
        CALI
        DT
        DTS
        GR
        NPHI
        PHIE
        RHOB
        RT
        TEMP

    Returns
    -------
    pd.DataFrame
        Returns a pandas dataframe object containing data from well 15/9-19 of the Volve field
    """
    stream = pkg_resources.resource_stream(__name__, 'data/EQR_Volve_Well_15_9-19.csv')
    return pd.read_csv(stream)

def load_volve_f5_dataset() -> pd.DataFrame:
    raise NotImplemented

def load_volve_drilling_dataset() -> pd.DataFrame:
    raise NotImplemented

if __name__ == "__main__":
    df = load_volve_19_dataset()
    print(df.head())
