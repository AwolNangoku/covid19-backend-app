import psycopg2

from dbConn import dbConnect


def fetch_country(country_name):

    pg_conn = None
    dbCountry = None
    try:

        pg_conn = dbConnect()
        pg_cursor = pg_conn.cursor()
        pg_cursor.execute(
            """SELECT * FROM countries_table"""
        )

        country_row = pg_cursor.fetchone()

        while country_row is not None:
            if country_row[1] == country_name:
                dbCountry = dict(
                    id=country_row[0],
                    country=country_row[1],
                    confirmed=country_row[2],
                    deaths=country_row[3],
                    recovered=country_row[4],
                    population=country_row[5],
                    continent=country_row[6]
                )

            country_row = pg_cursor.fetchone()

        pg_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if pg_conn is not None:
            pg_conn.close()

    return dbCountry
