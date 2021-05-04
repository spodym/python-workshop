"""
Practice using pdb/ipdb. Try using dir(), help().
With default data this script should print:

DEBUG:root:prices.prices does not have key for: 2020-05-02 00:00:00
DEBUG:root:prices.prices does not have key for: 2020-05-01 00:00:00
DEBUG:root:2020-05-03 00:00:00: 200 EUR was worth 908.48 PLN (4.5424 rate)
DEBUG:root:2020-07-03 00:00:00: 200 USD was worth 790.56 PLN (3.9528 rate)
Total dividends:	1699.04 PLN
Total tax to pay:	322.82 PLN
"""

import csv
import datetime
import logging
import os
from decimal import Decimal

logging.getLogger().setLevel(logging.DEBUG)

ROOT = os.path.dirname(__file__)

# use proper function to join dir path with filename
PRICES_ARCHIVE = __(ROOT, 'archiwum_tab_a_2020.csv')
DIVIDENDS_PATH = __(ROOT, 'dividends.csv')


class NBPPrices:
    def __init__(self):
        self.prices = {}
        with __ as f:
            # prices csv already has header
            # mind that it is not using comma as delimiter
            prices = csv.DictReader(__)
            for row in prices:
                # check how self.prices is used in exchange_rate
                # check how row data looks at this point
                date = datetime.datetime.strptime(__, __)
                self.prices[date] = __

    def exchange_rate(self, date, currency, day_before=True):
        currency = f'1{currency}'

        query_start_date = date
        if day_before:
            # use timedelta to move date back by one day
            query_start_date = query_start_date - __

        for day_offset in range(0, 10):
            try:
                query_date = query_start_date
                query_date -= datetime.timedelta(days=day_offset)
                rate = self.prices[query_date][currency]

                # rate needs some extra processing
                rate = __
                return __
            except:
                logging.debug(f'prices.prices does not have key for: {query_date}')

        raise Exception(f'No exchange found {date}, {currency}, {day_before}')


def process_dividends(dividends):
    prices = NBPPrices()

    total_pln = Decimal('0')
    tax_paid = Decimal('0')

    for row in dividends:
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        # datetime.strptime need proper format argument '%Y-__'
        date = datetime.datetime.strptime(row['date'], __)
        currency = row['currency']

        # row['amount'] need some extra processing
        amount = __

        exchange_rate = prices.exchange_rate(date, currency)

        # calculate amount_pln from amount and exchange rate
        # round it to 2 decimals
        amount_pln = __

        logging.debug(f'{date}: {amount} {currency} was worth {amount_pln} PLN ({exchange_rate} rate)')

        total_pln += amount_pln

    # tax is 19% from total amount
    # remember to use Decimal
    # round it as before
    tax_to_pay = __

    print(f'Total dividends:\t{total_pln} PLN')
    print(f'Total tax to pay:\t{tax_to_pay} PLN')


if __name__ == '__main__':
    # open csv file and load content to list
    # take a look how this list is later used
    # how list elements are used?
    # use special kind of csv reader
    with __ as f:
        dividends = csv.__(f, fieldnames=__)
        dividends = list(dividends)

    process_dividends(dividends)
