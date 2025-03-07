import mysql.connector
from mysql.connector import Error

try:
    # MySQLサーバーに接続
    connection = mysql.connector.connect(
        host="localhost",         # ローカルサーバーの場合は 'localhost'
        user='mshita',            # MySQLのユーザー名
        password='Tachi_0118'      # パスワード
    )

    if connection.is_connected():
        print('MySQLサーバーへの接続に成功しました')

        # データベース作成クエリ
        create_db_query = "CREATE DATABASE invoice_db"

        # カーソルを使用してクエリを実行
        cursor = connection.cursor()
        cursor.execute(create_db_query)
        print("データベース 'invoice_db' を作成しました。")

except Error as e:
    print(f"エラーが発生しました: {e}")

finally:
    # リソースを解放
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQLサーバーとの接続を閉じました")
