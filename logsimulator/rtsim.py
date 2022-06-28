import pandas as pd
import time
import schedule

from . import datasource

class rtsim:
    def __init__(self, data: pd.DataFrame, update_interval_secs: float = 0.2) -> None:
        self.update_interval_secs = update_interval_secs
        
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise TypeError('Supplied data must be a pd.DataFrame')

    def run(self):
        schedule.every(5).seconds.do(self.get_next_depth)

    def get_next_depth(self):
        depth_level = 0
        while depth_level <= len(self.data):
            print(f'{self.data.loc[[depth_level]]}')
            time.sleep(self.update_interval_secs)
            print(depth_level)

            depth_level += 1

if __name__ == "__main__":
    rtsim(data='aaa')
