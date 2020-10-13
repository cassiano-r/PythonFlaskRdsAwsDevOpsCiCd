import pymysql

conn = pymysql.connect(
        host= 'cassiano.ceck7bgheba8.us-east-1.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'adminadmin',
        db = 'cassianodb'        
        )
        
#insert query
def insert_details(name,email,comment,gender):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
    conn.commit()
    cur.close()
    
#read the data
def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    cur.close()
    return details

