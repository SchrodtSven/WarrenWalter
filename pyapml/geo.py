#
# Class managing access to geo data (mainly lat/long)
# 
# AUTHOR Sven Schrodt
# SINCE 2025-11-12
# 

import pandas as pd

class Geo:

    dta = None

    @staticmethod
    def get_geo(ctry:str):  
        if Geo.dta is None:
            Geo.read()

        tmp = Geo.dta[Geo.dta["Country"] == ctry][["Lat", "Long"]]
        return (float(tmp.Lat), float(tmp.Long))


    @staticmethod
    def read(fn:str="dta/world_geo.csv"):  
        Geo.dta = pd.read_csv(fn)


if __name__ == "__main__":
    Geo.read()

    print(Geo.get_geo("France"))