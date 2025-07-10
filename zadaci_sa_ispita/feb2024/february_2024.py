import csv
import json
from pathlib import Path
from sys import stderr
from pprint import pprint
from datetime import datetime, date

from execution_logger import *

def load_reviews_data(fpath):
    try:
        with open(fpath, 'r') as fobj:
            return list(csv.DictReader(fobj))
    except FileNotFoundError:
        stderr.write(f"Error while trying to read from file <{fpath}>. The file cannot be located!\n")
        return None
    except OSError as err:
        stderr.write(f"Error while trying to read data from file <{fpath}>\n{err}\n")
        return None

def preprocess_review_date(review_date):
    try:
        date_parts = review_date.split()
        if len(date_parts) != 3:
            return None
        day, month, year = date_parts
        day = "".join([ch for ch in day if ch.isdigit()])
        dt = datetime.strptime(f"{day} {month} {year}", "%d %B %Y")
        return dt.date()
    except Exception as e:
        stderr.write(f"Error occurred while trying to parse review date ({review_date}):\n{e}\n")
        return None


def write_to_json(summaries, fname):

    reports_dir = Path.cwd().parent / 'results'
    if not reports_dir.exists(): reports_dir.mkdir()

    try:
        with open(reports_dir / fname, 'w') as fobj:
            json.dump(summaries, fobj, indent=4)
    except OSError as err:
        stderr.write(f"Error while trying to write review summaries to json file <{reports_dir / fname}:>\n{err}\n")


@execution_logger
def airlines_review_summary(fpath, start_date, end_date):
    review_data = load_reviews_data(fpath)
    if not review_data:
        return

    selected_reviews = []
    for review in review_data:
        if bool(review['Verified']):
            review['Review_Date'] = preprocess_review_date(review['Review_Date'])
            if review['Review_Date'] and (start_date < review['Review_Date'] < end_date):
                selected_reviews.append(review)

    from collections import defaultdict
    airline_ratings = defaultdict(list)
    for review in selected_reviews:
        airline_ratings[review['Airline_Name']].append(int(review['Rating']))

    from statistics import median
    airline_summaries = list()
    for airline in airline_ratings.keys():
        airline_dict = dict()
        airline_dict['airline'] = airline
        airline_dict['avg_rating'] = median(airline_ratings[airline])
        airline_dict['positive_reviews'] = list()
        airline_dict['negative_reviews'] = list()
        for review in selected_reviews:
            if review['Airline_Name'] == airline:
                if int(review['Rating']) > airline_dict['avg_rating']:
                    airline_dict['positive_reviews'].append(review['Review'])
                else:
                    airline_dict['negative_reviews'].append(review['Review'])
        airline_summaries.append(airline_dict)

    airline_summaries.sort(key=lambda s: s['avg_rating'], reverse=True)

    fname = f"airlines_review_report_for_{datetime.strftime(start_date, '%d-%m-%y')}-"
    fname += f"{datetime.strftime(end_date, '%d-%m-%y')}.json"
    write_to_json(airline_summaries, fname)


if __name__ == '__main__':

    review_file = Path.cwd().parent / 'data' / 'airline_reviews.csv'
    start_date = date(2021, 12, 15)
    end_date = date(2022, 1, 15)
    airlines_review_summary(review_file, start_date, end_date)