import os
import sys

from ReceiveApp.model import main as receive_main


if __name__ == '__main__':
    try:
        receive_main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
