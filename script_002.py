import psycopg

# ! Postgresql Data types


def main():
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        print("Connection Info", connection.adapters)
        with connection.cursor() as cursor:

            # * Boolean Character Data types
            # ! CHARACTER VARYING(n), VARCHAR(n)	variable-length with length limit
            # ! CHARACTER(n), CHAR(n)	fixed-length, blank padded
            # ! TEXT, VARCHAR	variable unlimited length
            # create table
            cursor.execute(
                ("create temp table if not exists demo_charcter_data_type("
                 "a char(64), "
                 "b varchar(48), "
                 "c varchar, "
                 "d text, "
                 "e bpchar(64),"
                 "f bpchar"
                 ");"))
            # insert data
            cursor.execute(
                "insert into demo_charcter_data_type values (%s, %s, %s, %s, %s, %s);",
                ((
                    "char data type(32)",
                    "varchar data type(48) ------",
                    "text data type",
                    "varchar_umlimited length",
                    "varchar_umlimited length",
                    "varchar_umlimited length",
                )))
            cursor.execute("select * from demo_charcter_data_type;")
            #
            results = cursor.fetchall()
            for result in results:
                for x in result:
                    print(f"{x!r}")
                print()
            print()
            #
            cursor.execute("drop table if exists demo_charcter_data_type;")
            #
        connection.commit()
        connection.close()
    pass


if __name__ == "__main__":
    main()
    pass
