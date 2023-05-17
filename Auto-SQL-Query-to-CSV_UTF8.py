import argparse
import pandas as pd
import pymysql

def read_sql_file(path):
    with open(path, 'r') as file:
        return file.read()

def read_db_info_file(path):
    with open(path, 'r') as file:
        db_info = {}
        lines = file.readlines()
        for line in lines:
            key, value = line.split('=')
            db_info[key.strip()] = value.strip().replace("'", "")
        return db_info

def execute_sql(db_info, query):
    conn = pymysql.connect(host=db_info['host'], 
                           user=db_info['user'], 
                           password=db_info['password'], 
                           db=db_info['database'],
                           port=int(db_info['port']))
    return pd.read_sql_query(query, conn)

def write_to_csv(df, path):
    df.to_csv(path, index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sql_path', help='Path to the SQL file.')
    parser.add_argument('db_info_path', help='Path to the file with DB info.')
    parser.add_argument('output_path', help='Path to the output CSV file.')
    args = parser.parse_args()

    query = read_sql_file(args.sql_path)
    db_info = read_db_info_file(args.db_info_path)

    df = execute_sql(db_info, query)
    write_to_csv(df, args.output_path)
    
    # 输出任务信息
    print("输出文件路径：", args.output_path)
    print("输出文件编码：ANSI")


if __name__ == "__main__":
    main()
