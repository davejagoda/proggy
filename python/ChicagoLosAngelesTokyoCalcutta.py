#!/usr/bin/env python3

import argparse
import datetime
import zoneinfo

parser = argparse.ArgumentParser()
parser.add_argument("utc_hh", type=int, help="UTC hour (24 HH format)")
args = parser.parse_args()

t = datetime.time(args.utc_hh, 0)
jan_1 = datetime.datetime.combine(
    datetime.date(2024, 1, 1), t, tzinfo=datetime.timezone.utc
)
jul_1 = datetime.datetime.combine(
    datetime.date(2024, 7, 1), t, tzinfo=datetime.timezone.utc
)

locs = ["America/Chicago", "America/Los_Angeles", "Asia/Tokyo", "Asia/Calcutta"]


def is_dst(t):
    if datetime.timedelta(0) == t.dst():
        return False
    return True


for loc in locs:
    for d in [jan_1, jul_1]:
        u = datetime.datetime.combine(d, t, tzinfo=datetime.timezone.utc)
        # print(f'UTC: {u} {is_dst(u)}')
        l = u.astimezone(zoneinfo.ZoneInfo(loc))
        # print(f'{loc} {l} {is_dst(l)}')
        print(f"{loc} {l.hour} {l.minute}")
