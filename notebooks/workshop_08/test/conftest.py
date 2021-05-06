import logging
from pytest_socket import socket_allow_hosts


def pytest_addoption(parser):
    parser.addoption(
        "--local", action="store_true",
        default=False,
        help="disable external calls")


def pytest_configure(config):
    if config.option.local:
        # Allow only localhost connections
        logging.warning('disabling external calls')
        socket_allow_hosts(['127.0.0.1', '::1'])

