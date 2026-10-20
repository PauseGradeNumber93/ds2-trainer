"""Colored log helpers for the trainer console."""
from colorama import Fore, Style


def ok(msg: str) -> str:
    return f"{Fore.GREEN}[+]{Style.RESET_ALL} {msg}"


def warn(msg: str) -> str:
    return f"{Fore.YELLOW}[!]{Style.RESET_ALL} {msg}"


def err(msg: str) -> str:
    return f"{Fore.RED}[-]{Style.RESET_ALL} {msg}"