import argparse
import logging
import sys

STOCKS = 'stocks'
DIVIDENDS = 'dividends'


print(sys.argv)


def process_dividends(*args):
    logging.debug(args)
    logging.info(args)
    logging.warning(args)


def process_stocks(*args):
    print(args)


def set_log_level(options_log):
    levels = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }
    level = levels.get(options.log.lower())
    if level is None:
        raise ValueError(
            f"log level given: {options.log}"
            f" -- must be one of: {' | '.join(levels.keys())}")
    logging.basicConfig(level=level)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('exports_filenames', nargs='*')
    parser.add_argument(
        "-type",
        "--type",
        default=DIVIDENDS,
        choices=[STOCKS, DIVIDENDS]
    )
    parser.add_argument(
        "-log",
        "--log",
        default="warning",
        help=(
            "Provide logging level. "
            "Example --log debug', default='warning'"
        ),
    )

    options = parser.parse_args()
    set_log_level(options.log)

    if options.type == DIVIDENDS:
        process_dividends(options.exports_filenames)
    elif options.type == STOCKS:
        process_stocks(options.exports_filenames)
