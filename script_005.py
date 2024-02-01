import psycopg

# ! Postgresql Data types


def main():
    #
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        with connection.cursor() as cursor:
            # * Array Data types
            # create table
            cursor.execute(("create table if not exists demo_arrays("
                            "pk smallserial,"
                            "a integer[]"
                            ");"))
            # insert data

            cursor.execute(
                "insert into demo_arrays(a) values (%s);",
                ("{5, 8, 9, 10}", ),
            )
            cursor.execute(
                "insert into demo_arrays(a) values (%s);",
                ([924, 3, 7], ),
            )
            #
            # ! add array of items to array
            cursor.execute(
                "update demo_arrays set a =  array_cat(a, %s) where pk = 2;",
                ([49, 63, 70, 84, 140, 280], ),
            )
            #
            # ! add single item to array
            cursor.execute(
                "update demo_arrays set a = array_append(a, %s) where pk = 1;",
                (238, ),
            )
            #
            cursor.execute(
                query="select * from demo_arrays order by pk asc nulls last;")
            #
            results = cursor.fetchall()
            for result in results:
                for x in result:
                    print(x)
                    print(type(x))
                print()
                # for x in result:
                #     print(f"{x!r}")
                print()
            print()
            #
            cursor.execute("drop table if exists demo_arrays;")
            #
        connection.commit()
        connection.close()
    pass


if __name__ == "__main__":
    main()
    pass
