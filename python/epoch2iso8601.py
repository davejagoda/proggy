#!/usr/bin/env python3

import datetime
import sys

for date in sys.argv[1:]:
    print(
        datetime.datetime.isoformat(
            datetime.datetime.fromtimestamp(
                float(date)
            )
        )
    )
