
import psycopg2
from dbConn import dbConnect


def add_new_country(country):
    sql_insert_country = """INSERT INTO countries_table(country, confirmed, deaths, recovered, population, continent)
             VALUES(%s, %s, %s, %s, %s, %s) RETURNING country_id;"""
    pg_conn = None
    country_id = None
    try:
        pg_conn = dbConnect()
        pg_cursor = pg_conn.cursor()

        pg_cursor.execute(sql_insert_country, (country['country'], country['confirmed'],
                          country['deaths'], country['recovered'], country['population'], country['continent']))

        # get the generated id back
        country_id = pg_cursor.fetchone()[0]

        pg_conn.commit()
        pg_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if pg_conn is not None:
            pg_conn.close()

    return country_id
