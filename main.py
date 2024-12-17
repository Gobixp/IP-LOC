import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table, box
from rich.progress import Progress
import time
import sys
import os
import re

console = Console()

class IPLocationTracker:
    def __init__(self):
        self.api_key = "8b72e48f3c346a"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        banner = """
 ██╗██████╗      ██╗      ██████╗  ██████╗
 ██║██╔══██╗     ██║     ██╔═══██╗██╔════╝
 ██║██████╔╝     ██║     ██║   ██║██║     
 ██║██╔═══╝      ██║     ██║   ██║██║     
 ██║██║          ███████╗╚██████╔╝╚██████╗
 ╚═╝╚═╝          ╚══════╝ ╚═════╝  ╚═════╝
        """
        
        console.print(Panel(
            banner, 
            title="[bold green]Advanced IP Location Tracker[/]", 
            border_style="green",
            expand=False
        ))

        social_links = [
            ("Github", "https://github.com/wanzxploit"),
            ("Instagram", "https://instagram.com/wanz_xploit"),
            ("YouTube", "https://youtube.com/wanzxploit")
        ]

        social_table = Table(show_header=False, box=None, padding=(0, 1))
        for platform, link in social_links:
            social_table.add_row(f"[green]{platform}[/]", f"[white]{link}[/]")
        
        console.print(Panel(
            social_table, 
            title="[bold green]Social Media[/]", 
            border_style="green",
            expand=False
        ))

    def validate_ip(self, ip):
        ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        return bool(re.match(ip_pattern, ip or ''))

    def get_ip_info(self, ip):
        if not ip or not self.validate_ip(ip):
            console.print("[bold red]Invalid IP address format![/]")
            return None

        try:
            url = f"https://ipinfo.io/{ip}?token={self.api_key}"
            response = requests.get(url)
            data = response.json()

            if 'error' in data:
                console.print(f"[bold red]API Error: {data['error']['title']}[/]")
                return None

            # Convert country code to full name if possible
            country_code = data.get('country', 'N/A')
            if country_code == 'ID':
                country_name = "Indonesia"
            elif country_code == 'US':
                country_name = "United States"
            elif country_code == 'GB':
                country_name = "United Kingdom"
            else:
                country_name = country_code

            data['country'] = country_name

            return data
        except requests.RequestException as e:
            console.print(f"[bold red]Network Error: {e}[/]")
            return None
        except ValueError as e:
            console.print(f"[bold red]Data Processing Error: {e}[/]")
            return None

    def display_ip_info(self, ip_data):
        if not ip_data:
            return

        table = Table(
            show_header=True, 
            header_style="bold green",
            border_style="green",
            box=box.ROUNDED,
            padding=(0, 1)
        )
        
        table.add_column("Category", style="green", no_wrap=True)
        table.add_column("Information", style="white")

        details = [
            ("IP Address", ip_data.get('ip', 'N/A')),
            ("Country", ip_data.get('country', 'N/A')),
            ("Region", ip_data.get('region', 'N/A')),
            ("City", ip_data.get('city', 'N/A')),
            ("Hostname", ip_data.get('hostname', 'N/A')),
            ("Internet Provider", ip_data.get('org', 'N/A')),
            ("Timezone", ip_data.get('timezone', 'N/A')),
            ("Geographical Location", ip_data.get('loc', 'N/A'))
        ]

        for category, info in details:
            table.add_row(category, str(info))

        console.print(Panel(
            table, 
            title="[bold green]IP Location Details[/]", 
            border_style="green", 
            expand=False
        ))

    def main(self):
        self.clear_screen()
        self.show_banner()

        try:
            ip = console.input("[bold green]Enter IP to track: [/]").strip()
            
            with Progress(console=console) as progress:
                task = progress.add_task("[green]Tracking IP...", total=100)
                for _ in range(100):
                    progress.update(task, advance=1)
                    time.sleep(0.02)

            ip_data = self.get_ip_info(ip)
            
            if ip_data:
                self.display_ip_info(ip_data)
            
            console.print(
                Panel(
                    "[bold green]IP Location Tracker by Wanz Xploit[/]", 
                    border_style="green", 
                    expand=False
                )
            )

        except KeyboardInterrupt:
            console.print("\n[bold red]Tracking stopped by user.[/]")
        except Exception as e:
            console.print(f"[bold red]Unexpected error: {type(e).__name__} - {e}[/]")

def main_entry():
    try:
        tracker = IPLocationTracker()
        tracker.main()
    except Exception as e:
        print(f"Critical error: {type(e).__name__} - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main_entry()