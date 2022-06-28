import pandas as pd
import time

from . import datasource

class rtsim:
    def __init__(self, data: pd.DataFrame, update_interval_secs: float = 0.2) -> None:
        self.update_interval_secs = update_interval_secs
        
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise TypeError('Supplied data must be a pd.DataFrame')

    def run(self):
        raise NotImplemented

if __name__ == "__main__":
    rtsim(data='aaa')
