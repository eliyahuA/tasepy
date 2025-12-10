#!/usr/bin/tcsh -f
"/bin/true" '''\'
exec /usr/bin/python3.14 $0 https://datawise.tase.co.il/v1
'''
"""
https://habr.com/ru/articles/962608
"""
from typer import Argument, run
from requests import get
from requests.exceptions import RequestException
from typing import List
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

def get_status_emoji(status_code: int) -> str:
    status_string = ['✅ OK', '➡️ REDIRECT', '❌ CLIENT ERROR', 
                     '🔥 SERVER ERROR', '❓ UNKNOWN']
    return status_string[max(min(status_code // 100, 6) - 2, 0)]

def main(urls: List[str] = Argument(..., help="URL list")):
    table = Table(title="[bold]תוצאות בדיקת אתרי אינטרנט")
    table.add_column("                     סטטוס", justify="left", style="green bold")
    table.add_column("קוד סטטוס", justify="center")
    table.add_column("כתובת אתר", justify="center", style="cyan", no_wrap=True)

    for url in track(urls, description="[bold] בדיקת אתרים"):
        try:
            response = get(url, timeout=5)
            status_code = response.status_code
            status_text = get_status_emoji(status_code)
            
            row_style = ""
            if 300 <= status_code < 400:
                row_style = "yellow"
            elif status_code >= 400:
                row_style = "red"
            
            table.add_row(url, str(status_code), status_text, style=row_style)

        except RequestException as err:
            error_symbol='💥'
            table.add_row(url, "N/A", f"{error_symbol} ERROR: {err.__class__.__name__}", style="bold red")

    console.print(table)

if __name__ == "__main__":
    run(main)
