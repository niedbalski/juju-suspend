from juju_suspend.environment import Environment

import argparse
import sys


def parse_options():
    parser = argparse.ArgumentParser(
        description="""Juju plugin for suspend and resume a running
        environment""")

    parser.add_argument("--novarc",
                        default=None,
                        help='(OpenStack only): Path to the novarc',
                        type=str,
                        metavar='novarc')

    parser.add_argument("--suspend",
                        action='store_true',
                        help='Suspend the current environment')

    parser.add_argument("--resume",
                        action='store_true',
                        help='Resume a suspended environment')

    args = parser.parse_args()
    return args


def main():

    options = parse_options()
    try:
        env = Environment(options)

        if options.suspend:
            env.suspend()

        if options.resume:
            env.resume()

    except Exception as ex:
        sys.exit(str(ex))

if __name__ == "__main__":
    main()
