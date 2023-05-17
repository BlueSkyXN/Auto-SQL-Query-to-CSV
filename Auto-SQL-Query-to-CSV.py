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
    try:
        conn = pymysql.connect(host=db_info['host'], 
                               user=db_info['user'], 
                               password=db_info['password'], 
                               db=db_info['database'],
                               port=int(db_info['port']))
        return pd.read_sql_query(query, conn)
    except pymysql.Error as e:
        print("数据库连接错误:", str(e))
        return None

def write_to_csv(df, path, encoding):
    if encoding.lower() == 'a' or encoding.lower() == 'ansi':
        df.to_csv(path, index=False, encoding='ansi')
        print("输出文件编码：ANSI")
    elif encoding.lower() == 'u' or encoding.lower() == 'utf8' or encoding.lower() == 'utf-8':
        df.to_csv(path, index=False, encoding='utf-8')
        print("输出文件编码：UTF-8")
    else:
        print("不支持的编码类型。")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sql_path', help='Path to the SQL file.')
    parser.add_argument('db_info_path', help='Path to the file with DB info.')
    parser.add_argument('output_path', help='Path to the output CSV file.')
    parser.add_argument('-c', '--encoding', default='u', help='CSV file encoding. Default is UTF-8.')
    args = parser.parse_args()

    encoding = args.encoding.lower()

    if encoding not in ['a', 'ansi', 'u', 'utf8', 'utf-8']:
        print("不支持的编码类型。")
        return

    query = read_sql_file(args.sql_path)
    db_info = read_db_info_file(args.db_info_path)

    df = execute_sql(db_info, query)
    if df is not None:
        write_to_csv(df, args.output_path, encoding)
        print("任务已完成！")
        print("输出文件路径：", args.output_path)

if __name__ == "__main__":
    main()
