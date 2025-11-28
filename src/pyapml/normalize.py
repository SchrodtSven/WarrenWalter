#
# AUTHOR Sven Schrodt
# SINCE 2025-11-12
#

import pandas as pd


class Normalize:
    """ Class helping normalize given data including
        - detect uniq vals
        - sanitize name(s)
    """

    nm_rlz = {"fnd": " ", "rpl": "_"}

    @staticmethod
    def sanitize_name(nm: str) -> str:
        return nm.replace(Normalize.nm_rlz["fnd"], Normalize.nm_rlz["rpl"])
