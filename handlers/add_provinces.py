import psycopg2
from dbConn import dbConnect


def add_provinces(provinces):

    sql_insert_provinces = "INSERT INTO provinces_table(country_id, province, confirmed, deaths, recovered, updated) VALUES(%s,%s,%s,%s,%s,%s)"
    pg_conn = None
    try:
        pg_conn = dbConnect()
        pg_cursor = pg_conn.cursor()

        pg_cursor.executemany(sql_insert_provinces, provinces)
        pg_conn.commit()
        # close communication with the database
        pg_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if pg_conn is not None:
            pg_conn.close()
