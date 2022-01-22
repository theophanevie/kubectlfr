import sys

from kubectlfr.main import kubectlfr


def main() -> None:
    kubectlfr(sys.argv[1:])
