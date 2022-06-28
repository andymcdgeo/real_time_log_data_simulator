from dataclasses import dataclass
import pandas as pd

@dataclass
class SimDataObject:
    data: pd.DataFrame

    def __post_init__(self):
        if isinstance(self.data, pd.DataFrame):
            self.data = self.data
        else:
            raise TypeError('Supplied data must be in the form of a Pandas Dataframe')

