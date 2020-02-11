import mysql.connector
import pymysql

sql = pymysql.connect(host="localhost",
                      user="nazar",
                      password="Lacr1m0sa!",
                      db='test')


with sql as connect:
    connect.execute('show tables')
    res = connect.fetchall()

print(res)


# mydb = mysql.connector.connect(
#     host="localhost",
#     user="nazar",
#     passwd="xP809RC6"
# )
#
# print(mydb)