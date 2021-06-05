from models.product import Product
from service.database_connector import get_connection

def modify_data(raw_data):
    data = []
    for i in raw_data:
        data.append({"id":i[0],"name":i[1],"price":i[2]})
    return data 

def get_products():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        row = cur.fetchall()
        cur.close()
        conn.close()
    except:
        return {"error": True}
    return modify_data(row)

def create_product(product:Product):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO products(name,price) VALUES(%s,%s)",(product.name,product.price))
        conn.commit()
        cur.execute("SELECT * FROM products")
        row = cur.fetchall()
        cur.close()
        conn.close()
    except:
        return {"error": True}
    return modify_data(row)

def edit_product(product_id:int,product:Product):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE products SET name=%s, price=%s WHERE id=%s",(product.name,product.price,product_id))
        conn.commit()
        cur.execute("SELECT * FROM products")
        row = cur.fetchall()
        cur.close()
        conn.close()
    except:
        return {"error": True}
    return modify_data(row)

def delete_product(product_id:int):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE id='"+str(product_id)+"'")
        conn.commit()
        cur.execute("SELECT * FROM products")
        row = cur.fetchall()
        cur.close()
        conn.close()
    except:
        return {"error": True}
    return modify_data(row)