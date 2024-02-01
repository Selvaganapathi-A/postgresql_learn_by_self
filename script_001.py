import psycopg

# ! Postgresql Data types


def main():
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        print("Connection Info", connection.adapters)
        with connection.cursor() as cursor:
            # * Boolean Datatype = True

            # create table
            cursor.execute(
                ("create temp table if not exists demo_boolean_data_type("
                 "pk serial primary key,"
                 "dt_boolean boolean"
                 ");"))
            # insert data
            query = (
                "insert into demo_boolean_data_type(dt_boolean) values (%(b_data)s);"
            )
            print(query)
            cursor.executemany(
                query,
                (
                    # ~ True
                    {
                        "b_data": True,
                    },
                    {
                        "b_data": 'yes',
                    },
                    {
                        "b_data": 'y',
                    },
                    {
                        "b_data": 'true',
                    },
                    {
                        "b_data": 't',
                    },
                    # ~ False
                    {
                        "b_data": 'no',
                    },
                    {
                        "b_data": 'false',
                    },
                    {
                        "b_data": 'f',
                    },
                    {
                        "b_data": False,
                    },
                ))
            cursor.execute("select * from demo_boolean_data_type;")
            #
            result = cursor.fetchall()
            for (pk, x) in result:
                print(pk, x)
            #
        connection.commit()
        connection.close()
    pass


if __name__ == "__main__":
    main()
    pass
