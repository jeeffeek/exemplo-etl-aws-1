from csv_to_parquet import process_csv

def main():
    csv_file = "data/movies_and_tv_shows.csv"
    output_dir = "output"
    bucket_name = "jeeffeek-sql-athena-parquet"
    s3_key = "parquet/movies_and_tv_shows.parquet"
    
    process_csv(csv_file, output_dir, bucket_name, s3_key)


if __name__ == "__main__":
    main()
