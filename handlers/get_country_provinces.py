import psycopg2

from dbConn import dbConnect


def fetch_country_provinces(country_id):

    pg_conn = None
    listofProvinces = list()
    try:

        pg_conn = dbConnect()
        pg_cursor = pg_conn.cursor()
        pg_cursor.execute(
            """SELECT * FROM provinces_table"""
        )

        province_row = pg_cursor.fetchone()

        while province_row is not None:
            if province_row[2] == country_id:
                listofProvinces.append(
                    dict(
                        id=province_row[0],
                        province=province_row[1],
                        country_id=province_row[2],
                        confirmed=province_row[3],
                        deaths=province_row[4],
                        recovered=province_row[5],
                        updated=province_row[6],
                    )
                )
            province_row = pg_cursor.fetchone()

        pg_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if pg_conn is not None:
            pg_conn.close()

    return listofProvinces
