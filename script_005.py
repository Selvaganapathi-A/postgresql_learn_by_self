import psycopg

# ! Postgresql Data types


def main():
    #
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        with connection.cursor() as cursor:
            # * Date/Time/Interval Data types
            # create table
            cursor.execute(("create table if not exists demo_datetime("
                            ""
                            ");"))
            # insert data

            cursor.executemany(
                "insert into demo_datetime(a,b,c,d,e,f) values (%s, %s, %s, %s, %s, %s);",
                (),
            )
            cursor.execute(query="select * from demo_datetime;")
            #
            results = cursor.fetchall()
            for result in results:
                for x in result:
                    print(x)
                print()
                for x in result:
                    print(f"{x!r}")
                print()
            print()
            #
            cursor.execute("drop table if exists demo_datetime;")
            #
        connection.commit()
        connection.close()
    pass


if __name__ == "__main__":
    main()
    pass
