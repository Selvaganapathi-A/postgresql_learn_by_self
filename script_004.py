import datetime
import zoneinfo

import psycopg

# ! Postgresql Data types


def main():
    india_timezone = zoneinfo.ZoneInfo(key="Asia/Calcutta")
    datetime_without_timezone = datetime.datetime(
        year=2024,
        month=5,
        day=31,
        hour=15,
        minute=18,
        second=12,
        microsecond=999999,
    )
    datetime_with_timezone = datetime.datetime(year=2024,
                                               month=5,
                                               day=31,
                                               hour=15,
                                               minute=18,
                                               second=12,
                                               microsecond=999999,
                                               tzinfo=india_timezone)
    time_without_timezone = datetime.time(
        hour=23,
        minute=59,
        second=36,
        microsecond=234023,
    )
    time_with_timezone = datetime.time(hour=23,
                                       minute=59,
                                       second=36,
                                       microsecond=234023,
                                       tzinfo=india_timezone)
    date = datetime.date(
        year=1994,
        month=9,
        day=26,
    )
    time_interval = datetime.timedelta(
        days=5,
        seconds=40000,
        microseconds=999999999,
        hours=18,
    )
    #
    print(india_timezone)
    print()
    print(datetime_with_timezone)
    print(datetime_without_timezone)
    print(date)
    print(time_with_timezone)
    print(time_without_timezone)
    print(time_interval)
    print()
    #
    with psycopg.Connection.connect(
            conninfo="dbname=postgres user=postgres password=Windows@11"
    ) as connection:
        with connection.cursor() as cursor:
            # * Date/Time/Interval Data types
            # create table
            cursor.execute((
                "create table if not exists demo_datetime("
                "a timestamp default NULL,"  # without timezone both date or datetime
                "b timestamp with time zone default NULL,"  # with timezone
                "c date default NULL,"
                "d time default NULL,"  # without timezone
                "e time with time zone default NULL,"  # with timezone
                "f interval default NULL"
                ");"))
            # insert data

            cursor.executemany(
                "insert into demo_datetime(a,b,c,d,e,f) values (%s, %s, %s, %s, %s, %s);",
                ((
                    datetime_without_timezone,
                    datetime_with_timezone,
                    date,
                    time_without_timezone,
                    "15:57:29.982347",
                    time_interval,
                ), ),
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
