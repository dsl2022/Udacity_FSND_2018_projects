#!/usr/bin/env python3

import psycopg2

# queries
ques_1 = 'What are the most popular three articles of all time?'

query_1 = (
    "select title, count(*) as views from articles inner join "
    "log on concat('/article/', articles.slug) = log.path "
    "where log.status like '%200%' "
    "group by log.path, articles.title order by views desc limit 3;")

ques_2 = 'Who are the most popular article authors of all time?'

query_2 = (
    "select authors.name, count(*) as views from articles inner join "
    "authors on articles.author = authors.id inner join "
    "log on concat('/article/', articles.slug) = log.path where "
    "log.status like '%200%' group by authors.name order by views desc")

ques_3 = 'On which days did more than 1% of requests lead to errors?'

query_3 = (
    "select * from ( "
    "select a.day, "
    "round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2) "
    "as errp from "
    "(select date(time) as day, count(*) as hits from log group by day) as a "
    "inner join "
    "(select date(time) as day, count(*) as hits from log where status "
    "like '%404%' group by day) as b "
    "on a.day = b.day) "
    "as t where errp > 1.0; ")


def connect(database_name="news"):
    # Connect to the PostgreSQL database. Returns a database connection
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except RuntimeError:
        print("Failed to connect to the database")


def get_results(query):
    # Return query results
    db, cursor = connect()
    # execute query
    cursor.execute(query)
    return cursor.fetchall()
    # close query
    db.close()


def print_results(results):
    # print query result
    # print question.
    print(results[1])
    # loop through and print results
    for index, result in enumerate(results[0]):
        print("\t {} : {} -- {} views".format(index+1,
              result[0], str(result[1])))
    print('')


def print_error_results(query_results):
    # print error results
    print(query_results[1])
    for results in query_results[0]:
        print("\t {} -, {} % errors".format(results[0], str(results[1])))
        print('')


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_results(query_1), ques_1
    popular_authors_results = get_results(query_2), ques_2
    load_error_days = get_results(query_3), ques_3
    # print query results
    print_results(popular_articles_results)
    print_results(popular_authors_results)
    print_error_results(load_error_days)
