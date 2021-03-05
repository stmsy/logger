#!/usr/bin/env python

from ring.add import add
from ring.mult import mult
from ring.sub import sub


if __name__ == '__main__':
    # Log messages from another module
    add(1.0, 2, verbosity=5)
