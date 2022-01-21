import subprocess
import click
from typing import List, Tuple, Dict

from kubectlfr.translation import TRANSLATION


def translate(args: List[str], translation: Dict[str, str]) -> List[str]:
    args_translated = []

    for arg in args:
        if arg in translation:
            args_translated.append(translation[arg])
        else:
            args_translated.append(arg)

    return args_translated


def run_kubectl(args: List[str]) -> Tuple[str, int]:
    cmd_exec = subprocess.run(["kubectl", *args], capture_output=True)

    return cmd_exec.stdout.decode("utf-8") + cmd_exec.stderr.decode("utf-8"), cmd_exec.returncode


@click.command()
@click.argument("args", nargs=-1)
def kubectlfr(args: List[str]) -> None:

    args_translated = translate(args, TRANSLATION)
    output, return_code = run_kubectl(args_translated)

    print(output)
    exit(return_code)
