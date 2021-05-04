"""
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
PRICES_ARCHIVE = os.path.join(ROOT, 'archiwum_tab_a_2020.csv')
DIVIDENDS_PATH = os.path.join(ROOT, 'dividends.csv')


class NBPPrices:
    def __init__(self):
        self.prices = {}
        with open(PRICES_ARCHIVE) as f:
            prices = csv.DictReader(f, delimiter=';')
            for row in prices:
                date = datetime.datetime.strptime(row['data'], '%Y%m%d')
                self.prices[date] = row

    def exchange_rate(self, date, currency, day_before=True):
        currency = f'1{currency}'

        query_start_date = date
        if day_before:
            query_start_date = query_start_date - datetime.timedelta(days=1)

        for day_offset in range(0, 10):
            try:
                query_date = query_start_date
                query_date -= datetime.timedelta(days=day_offset)
                rate = self.prices[query_date][currency]
                rate = rate.replace(',', '.')
                return Decimal(rate)
            except:
                logging.debug(f'prices.prices does not have key for: {query_date}')

        raise Exception(f'No exchange found {date}, {currency}, {day_before}')


def process_dividends(dividends):
    prices = NBPPrices()

    total_pln = Decimal('0')
    tax_paid = Decimal('0')

    for row in dividends:
        date = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
        currency = row['currency']
        amount = Decimal(row['amount'])

        exchange_rate = prices.exchange_rate(date, currency)
        amount_pln = round(amount * exchange_rate, 2)

        logging.debug(f'{date}: {amount} {currency} was worth {amount_pln} PLN ({exchange_rate} rate)')

        total_pln += amount_pln

    tax_to_pay = round(total_pln * Decimal('0.19'), 2)

    print(f'Total dividends:\t{total_pln} PLN')
    print(f'Total tax to pay:\t{tax_to_pay} PLN')


if __name__ == '__main__':
    with open(DIVIDENDS_PATH) as f:
        dividends = csv.DictReader(f, fieldnames=['date', 'currency', 'amount'])
        dividends = list(dividends)

    process_dividends(dividends)
