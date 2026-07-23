import pandas as pd


def build_date_dimension(start="2020-01-01", end="2030-12-31"):

    dates = pd.date_range(start=start, end=end)

    df = pd.DataFrame()

    df["full_date"] = dates

    df["day"] = dates.day

    df["month"] = dates.month

    df["month_name"] = dates.month_name()

    df["quarter"] = dates.quarter

    df["year"] = dates.year

    df["week"] = dates.isocalendar().week.astype(int)

    df["day_of_week"] = dates.day_name()

    return df