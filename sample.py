import pandas


if __name__ == "__main__":
    df = pandas.read_parquet('s3://data.oddsmagnet.com/history/ingest_year=2022/ingest_month=9/ingest_day=10/')
    print(df)