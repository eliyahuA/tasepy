from requests import get
from requests.exceptions import RequestException
from typing import List
from rich.console import Console
from rich.table import Table
from rich.progress import track
from argparse import ArgumentParser

console = Console()

def get_status_emoji(status_code: int) -> str:
    status_string = ['✅ OK', '➡️ REDIRECT', '❌ CLIENT ERROR', 
                     '🔥 SERVER ERROR', '❓ UNKNOWN']
    return status_string[max(min(status_code // 100, 6) - 2, 0)]

def main():
    parser = ArgumentParser(description='TASE API SITE CHECKER')
    parser.add_argument('-url', type=str, required=True, help='TASE API site URL')
    args = parser.parse_args()
    urls=[args.url]
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
    return status_code

if __name__ == "__main__":
    print(main())
