import datetime

from psycopg.types.range import Range

import psycopg
import pytz

# ! Postgresql Data types


def main():
    #
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        with connection.cursor() as cursor:
            # * Range Data type
            # create table
            #
            #
            cursor.execute(("select "
                            "%s::int4range, "
                            "%s::int8range, "
                            "%s::int8range, "
                            "%s::numrange, "
                            "%s::numrange, "
                            "%s::tsrange, "
                            "%s::tstzrange, "
                            "%s::daterange;"), (
                                (0, 5),
                                (6, 10),
                                Range(lower=11),
                                Range(21, 30),
                                Range(upper=41),
                                (
                                    datetime.datetime(2020, 1, 1),
                                    datetime.datetime(2020, 12, 31),
                                ),
                                (
                                    datetime.datetime(
                                        2021,
                                        1,
                                        1,
                                        tzinfo=pytz.timezone("Asia/Calcutta"),
                                    ),
                                    datetime.datetime(
                                        2021,
                                        12,
                                        31,
                                        tzinfo=pytz.timezone("Asia/Calcutta")),
                                ),
                                (
                                    datetime.date(2022, 12, 31),
                                    datetime.date(2023, 12, 31),
                                ),
                            ))
            #
            results = cursor.fetchall()
            x: Range
            for result in results:
                for x in result:
                    print(x,
                          x.lower,
                          x.upper, (x.lower_inc, x.upper_inc),
                          sep=" ░▒▓█▓▒░ ")
                    # print(type(x))
                    # print(dir(x))
                    print()
                print()
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
