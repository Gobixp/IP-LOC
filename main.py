from flask import Flask, request, send_from_directory
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import logging
import pycountry
import os
from datetime import datetime

app = Flask(__name__)
console = Console()

log = logging.getLogger('werkzeug')
log.disabled = True

API_KEY = "8b72e48f3c346a"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_styled_table() -> Table:
    table = Table(
        show_header=True,
        header_style="bold white on rgb(50,50,50)",
        border_style="rgb(50,50,50)",
        expand=True
    )
    table.add_column("Category", style="cyan", width=20)
    table.add_column("Details", style="green")
    return table

def get_country_name(country_code):
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        return country.name if country else country_code
    except Exception as e:
        return f"Error: {str(e)}"

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}?token={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'country' in data:
            data['country'] = get_country_name(data['country'])
        return data
    return {"error": "Unable to fetch IP information"}

def create_header(title: str) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_row(f"[b]{title}")
    grid.add_row(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return Panel(
        Align.center(grid),
        style="white on rgb(25,25,25)",
        border_style="rgb(50,50,50)",
        padding=(1, 0),
    )

def display_terminal_info(ip_info):
    table = create_styled_table()
    ordered_keys = [
        ("ip", "IP Address"),
        ("country", "Country"),
        ("region", "State/Region"),
        ("city", "City"),
        ("loc", "Coordinates"),
        ("org", "Organization"),
        ("timezone", "Time Zone"),
        ("postal", "Postal Code")
    ]
    for key, label in ordered_keys:
        if key in ip_info:
            table.add_row(label, str(ip_info[key]))
    console.print("\n")
    console.print(Panel(table, border_style="rgb(50,50,50)"))
    console.print("\n")

def create_server_info() -> Panel:
    table = Table.grid(padding=1, expand=True)
    table.add_column(justify="center")
    table.add_row("[b]Server Configuration")
    table.add_row("[cyan]To access your server from a public URL, run the following in a new session: ")
    table.add_row("[green]ssh -R 80:localhost:8080 nokey@localhost.run")
    return Panel(
        Align.center(table),
        border_style="rgb(50,50,50)",
        padding=(1, 2),
    )

def create_footer_info():
    return Panel(
        "Starting server at http://localhost:8080",
        border_style="rgb(50,50,50)"
    )

@app.route('/')
def index():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip_info = get_ip_info(ip_address)
    
    if "error" not in ip_info:
        display_terminal_info(ip_info)
    else:
        console.print(
            Panel(f"[red]Error: {ip_info['error']}", border_style="red", title="Error", title_align="left")
        )
    
    return send_from_directory(os.path.join(os.getcwd(), 'site'), 'index.html')

@app.route('/info')
def get_info():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip_info = get_ip_info(ip_address)
    
    if "error" not in ip_info:
        display_terminal_info(ip_info)
        return "IP information has been displayed in the terminal."
    else:
        console.print(
            Panel(f"[red]Error: {ip_info['error']}", border_style="red", title="Error", title_align="left")
        )
        return "Error fetching IP information. Please check the terminal for details."

if __name__ == '__main__':
    clear_screen()
    console.print("\n")
    console.print(create_header("IP Information Tracker"))
    console.print(create_server_info())
    console.print(create_footer_info())
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.INFO)

    print("\n * Author: Wanz Xploit")
    print(" * Tools: IP-LOC")
    
    app.run(host='0.0.0.0', port=8080)