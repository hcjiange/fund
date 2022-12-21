import os
from main import main
import argparse

if __name__ == "__main__":
    print("running. pid: " + str(os.getpid()))

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--do', type=str, default="sync_stocks")
    args = parser.parse_args()
    main.do(args.do)

