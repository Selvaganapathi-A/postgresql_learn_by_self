import psycopg

# ! Postgresql Data types


def main():
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        print("Connection Info", connection.adapters)
        with connection.cursor() as cursor:
            # * Boolean Datatype = True
            cursor.execute(
                "select CAST(1 as BOOLEAN), CAST('yes' as BOOLEAN), CAST('y' as BOOLEAN), CAST('true' as BOOLEAN), CAST('t' as BOOLEAN), true;"
            )
            #
            result = cursor.fetchall()
            print(result)
            #
            #
            #
            #
            # * Boolean Datatype = False
            cursor.execute(
                "select CAST(0 as BOOLEAN), CAST('no' as BOOLEAN), CAST('false' as BOOLEAN), CAST('f' as BOOLEAN), false;"
            )
            #
            result = cursor.fetchall()
            print(result)
            #
        connection.commit()
        connection.close()
    pass


if __name__ == "__main__":
    main()
    pass
