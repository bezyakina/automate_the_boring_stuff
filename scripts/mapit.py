#!/usr/bin/env python3
# mapIt.py - Launches a Yandex.Maps in the browser using an address from the
# command line or clipboard.

import webbrowser, sys
from jaraco import clipboard
from urllib import request

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = clipboard.paste()

encoded_address = request.quote(address.encode('utf-8'))
webbrowser.open('https://yandex.ru/maps/213/moscow/?text=' + encoded_address)
