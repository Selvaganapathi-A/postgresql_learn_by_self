import psycopg

# ! Postgresql Data types


def main():
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        with connection.cursor() as cursor:
            # * Numeric Data types
            # create table
            cursor.execute(
                ("create temp table if not exists demo_numeric_data_type("
                 "a smallint,"
                 "b integer,"
                 "c bigint,"
                 "d real,"
                 "e double precision,"
                 "f smallserial,"
                 "g serial,"
                 "h bigserial,"
                 "i decimal,"
                 "j numeric(8, 2),"
                 "k numeric(8, -1),"
                 "l decimal(8, 2)"
                 ");"))
            # insert data
            cursor.executemany(
                "insert into demo_numeric_data_type(a,b,c,d,e,i,j,k,l) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    (
                        1,
                        1,
                        1,
                        1.25,
                        1.556,
                        3.142857,
                        768.8977969,
                        768.8977969,
                        896768.89,
                    ),
                    (
                        2,
                        3,
                        4,
                        5.25,
                        98734.556,
                        9.9076847,
                        4354.645353145,
                        4354.645353145,
                        999999.648,
                    ),
                ))
            cursor.execute("select * from demo_numeric_data_type;")
            #
            results = cursor.fetchall()
            for result in results:
                print(result)
            print()
            #
            cursor.execute("select 12.34::money;")
            #
            results = cursor.fetchall()
            for result in results:
                print(result)
            print()
            #
            cursor.execute("drop table if exists demo_numeric_data_type;")
            #
        connection.commit()
        connection.close()
    pass


if __name__ == "__main__":
    main()
    pass
