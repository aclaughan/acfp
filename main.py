#!/usr/local/bin/python3
# ------------------------------------------------------------------------------
#        name : false ping.py
#      author : alan claughan
#     version : 1.0.0
#        date : 26-07-2020
# description : sometimes you need to capture a ping for a demonstration and
#               you dont always have access to the network. This will vary the
#               number of pings, the response time and calculate the summary
#               statistics
#
# ==============================================================================
#

import logging
import sys
from random import randint, uniform

logging.basicConfig(level = logging.DEBUG)

DISPLAY_NUMBER = 3


# TODO: add variations for different platforms


def ave_number(number_list):
    return sum(number_list) / len(number_list)


def var_number(number_list):
    mu = ave_number(number_list)
    return ave_number([(x - mu) ** 2 for x in number_list])


def fake_ping(host):
    numbers = []

    no_of_pings = int(randint(200, 400))

    print(
            f'Started ping from remote host to {host}\n\n$ ping {host}\n'
            f'PING {host} ({host}) 56(84) bytes of data.'
            )

    for x in range(no_of_pings):
        if x < DISPLAY_NUMBER or x > no_of_pings - (DISPLAY_NUMBER + 1):
            timer = uniform(2.0, 2.7)
            numbers.append(timer)
            print(
                    f'64 bytes from {host}: icmp_seq={x} '
                    f'ttl=64 time={timer:.3f} ms'
                    )

        if x == (DISPLAY_NUMBER + 1):
            print(' ...\n  results removed to reduce document size\n ...')

    print(
            f'^C\n--- {host} ping statistics ---\n'
            f'{no_of_pings} packets transmitted, {no_of_pings} '
            f'packets received, 0.0% packet loss\n'
            f'round-trip min/avg/max/stddev = {min(numbers):.3f}/'
            f'{ave_number(numbers):.3f}/{max(numbers):.3f}/'
            f'{var_number(numbers) * 10:.3f} ms\n'
            f'\nThe ping continued uninterrupted, with {no_of_pings} '
            f'ICMP echos sent, {no_of_pings} ICMP replies received. '
            f'There were zero packets dropped.\n\n'
            )


def main():
    # hosts = [str(sys.argv[1])]
    # hosts = ["192.168.1.1", "168.202.74.131"]
    hosts = ["192.168.1.1"]

    for host in hosts:
        fake_ping(host)


if __name__ == '__main__':
    main()

# logging.debug(stuff)
