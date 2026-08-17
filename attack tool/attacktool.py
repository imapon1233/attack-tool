

import os
import sys
import time
import platform
import socket
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box

console = Console()

SECTIONS = [
    "HOME",
    "OSINT",
    "NETWORK",
    "SOCIAL",
    "CYBER",
    "SYSTEM",
    "FAQ",
    "DISCLAIMER",
    "DISCORD",
    "EXIT"
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ========================= SPLASH =========================

def splash():
    frames = [
        "[magenta]            [/]",
        "[magenta]      /      [/]",
        "[magenta]     /A      [/]",
        "[magenta]    /AT      [/]",
        "[magenta]   /ATT      [/]",
        "[magenta]  /ATTA      [/]",
        "[magenta] /ATTAC      [/]",
        "[magenta]/ATTACK      [/]",
        "[magenta]/ATTACK TOOL[/]",
    ]
    for f in frames:
        clear()
        console.print(Align.center(f))
        console.print(Align.center("[cyan]PRESS ENTER TO ACCESS[/]"))
        time.sleep(0.07)
    input()

# ========================= DASHBOARD =========================

def dashboard():
    clear()

    side = Panel(
        f"[cyan]Operator: /attack\n"
        f"Status: READY\n"
        f"Mode: ACTIVE\n"
        f"OS: {platform.system()} {platform.release()}\n"
        f"Discord: https://discord.gg/kKVfJ5WxpK[/]",
        title="[magenta]SYSTEM[/]",
        border_style="magenta"
    )

    table = Table(title="[magenta]MAIN MENU /attack[/]", box=box.ROUNDED, border_style="magenta")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Section", justify="center", style="white")

    for i, sec in enumerate(SECTIONS):
        table.add_row(str(i), sec)

    console.print(
        Panel.fit(
            Align.center("[bold magenta]/ATTACK DASHBOARD — ULTRA EDITION[/]"),
            border_style="magenta"
        )
    )

    console.print(table)
    console.print(side)

def run_cmd(cmd):
    clear()
    console.print(f"[cyan]Eseguo: [white]{cmd}[/]")
    console.print("[yellow]Nota: l'esecuzione di comandi esterni è a tuo rischio e responsabilità.[/]")
    os.system(cmd)
    input("\nPremi INVIO per tornare...")

# ========================= OSINT =========================

def osint():
    while True:
        clear()
        table = Table(title="[magenta]OSINT Tools[/]", box=box.ROUNDED, border_style="magenta")
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Tool", justify="center", style="white")

        tools = [
            "Sherlock (username)",
            "Maigret (username)",
            "Holehe (email)",
            "PhoneInfoga (telefono)",
            "Instaloader (Instagram)",
            "Instagram-Scraper",
            "IPinfo",
            "WHOIS",
            "theHarvester",
            "SpiderFoot",
            "OSINT Framework",
            "Indietro"
        ]

        for i, t in enumerate(tools):
            table.add_row(str(i), t)

        console.print(table)
        choice = input("\nSeleziona ID: ").strip()

        if choice == "0":
            user = input("Username: ")
            run_cmd(f"sherlock {user}")

        elif choice == "1":
            user = input("Username: ")
            run_cmd(f"maigret {user}")

        elif choice == "2":
            email = input("Email: ")
            run_cmd(f"holehe {email}")

        elif choice == "3":
            num = input("Numero (+39...): ")
            run_cmd(f"phoneinfoga scan -n {num}")

        elif choice == "4":
            user = input("Instagram username: ")
            run_cmd(f"instaloader {user}")

        elif choice == "5":
            user = input("Instagram username: ")
            run_cmd(f"instagram-scraper {user}")

        elif choice == "6":
            ip = input("IP: ")
            run_cmd(f"curl ipinfo.io/{ip}")

        elif choice == "7":
            dom = input("Dominio: ")
            run_cmd(f"whois {dom}")

        elif choice == "8":
            target = input("Dominio/Email: ")
            run_cmd(f"theHarvester -d {target} -b all")

        elif choice == "9":
            run_cmd("xdg-open https://www.spiderfoot.net")

        elif choice == "10":
            run_cmd("xdg-open https://osintframework.com")

        elif choice == "11":
            return

# ========================= NETWORK =========================

def network():
    while True:
        clear()
        table = Table(title="[magenta]Network Tools[/]", box=box.ROUNDED, border_style="magenta")
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Tool", justify="center", style="white")

        tools = [
            "Ping",
            "Traceroute",
            "Nmap (base)",
            "Nmap (ports 1-1000)",
            "Curl Header",
            "DNS Lookup",
            "DNS Records",
            "Reverse DNS",
            "Indietro"
        ]

        for i, t in enumerate(tools):
            table.add_row(str(i), t)

        console.print(table)
        choice = input("\nSeleziona ID: ").strip()

        if choice == "0":
            host = input("Host: ")
            run_cmd(f"ping -c 4 {host}" if os.name != "nt" else f"ping {host}")

        elif choice == "1":
            host = input("Host: ")
            run_cmd(f"traceroute {host}" if os.name != "nt" else f"tracert {host}")

        elif choice == "2":
            host = input("Host: ")
            run_cmd(f"nmap {host}")

        elif choice == "3":
            host = input("Host: ")
            run_cmd(f"nmap -p 1-1000 {host}")

        elif choice == "4":
            url = input("URL: ")
            run_cmd(f"curl -I {url}")

        elif choice == "5":
            dom = input("Dominio: ")
            run_cmd(f"nslookup {dom}")

        elif choice == "6":
            dom = input("Dominio: ")
            run_cmd(f"dig {dom} ANY")

        elif choice == "7":
            ip = input("IP: ")
            run_cmd(f"nslookup {ip}")

        elif choice == "8":
            return

# ========================= SOCIAL =========================

def social():
    while True:
        clear()
        table = Table(title="[magenta]Social Web[/]", box=box.ROUNDED, border_style="magenta")
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Site", justify="center", style="white")

        sites = [
            "WhatsApp Web",
            "Telegram Web",
            "TikTok",
            "Instagram",
            "Twitter/X",
            "Reddit",
            "GitHub",
            "LinkedIn",
            "Indietro"
        ]

        for i, s in enumerate(sites):
            table.add_row(str(i), s)

        console.print(table)
        choice = input("\nSeleziona ID: ").strip()

        if choice == "0":
            run_cmd("xdg-open https://web.whatsapp.com")

        elif choice == "1":
            run_cmd("xdg-open https://web.telegram.org")

        elif choice == "2":
            run_cmd("xdg-open https://www.tiktok.com")

        elif choice == "3":
            run_cmd("xdg-open https://www.instagram.com")

        elif choice == "4":
            run_cmd("xdg-open https://twitter.com")

        elif choice == "5":
            run_cmd("xdg-open https://www.reddit.com")

        elif choice == "6":
            run_cmd("xdg-open https://github.com")

        elif choice == "7":
            run_cmd("xdg-open https://www.linkedin.com")

        elif choice == "8":
            return

# ========================= CYBER =========================

def cyber():
    while True:
        clear()
        table = Table(title="[magenta]Cyber Security Tools[/]", box=box.ROUNDED, border_style="magenta")
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Tool", justify="center", style="white")

        tools = [
            "Hash Generator",
            "Port Scan (safe)",
            "WHOIS (web)",
            "SSL Labs",
            "Shodan",
            "CVE Search",
            "Indietro"
        ]

        for i, t in enumerate(tools):
            table.add_row(str(i), t)

        console.print(table)
        choice = input("\nSeleziona ID: ").strip()

        if choice == "0":
            text = input("Testo da hashare: ")
            import hashlib
            md5 = hashlib.md5(text.encode()).hexdigest()
            sha1 = hashlib.sha1(text.encode()).hexdigest()
            sha256 = hashlib.sha256(text.encode()).hexdigest()

            clear()
            table = Table(title="[magenta]Hash Result[/]", box=box.ROUNDED, border_style="magenta")
            table.add_column("Algoritmo", style="cyan")
            table.add_column("Hash", style="white")
            table.add_row("MD5", md5)
            table.add_row("SHA1", sha1)
            table.add_row("SHA256", sha256)
            console.print(table)
            input("\nPremi INVIO per tornare...")

        elif choice == "1":
            host = input("Host: ")
            ports = [80, 443, 22, 21, 25]
            results = []
            for p in ports:
                s = socket.socket()
                s.settimeout(0.5)
                try:
                    s.connect((host, p))
                    results.append(f"{p} OPEN")
                except:
                    results.append(f"{p} CLOSED")
                s.close()

            clear()
            table = Table(title=f"[magenta]Port Scan — {host}[/]", box=box.ROUNDED, border_style="magenta")
            table.add_column("Porta", style="cyan")
            table.add_column("Stato", style="white")
            for line in results:
                port, status = line.split(" ", 1)
                table.add_row(port, status)
            console.print(table)
            input("\nPremi INVIO per tornare...")

        elif choice == "2":
            dom = input("Dominio: ")
            run_cmd(f"xdg-open https://who.is/whois/{dom}")

        elif choice == "3":
            dom = input("Dominio: ")
            run_cmd(f"xdg-open https://www.ssllabs.com/ssltest/analyze.html?d={dom}")

        elif choice == "4":
            query = input("Shodan query: ")
            run_cmd(f"xdg-open https://www.shodan.io/search?query={query}")

        elif choice == "5":
            product = input("Prodotto/Software: ")
            run_cmd(f"xdg-open https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={product}")

        elif choice == "6":
            return

# ========================= SYSTEM =========================

def system_info():
    clear()
    table = Table(title="[magenta]System Info[/]", box=box.ROUNDED, border_style="magenta")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("OS", platform.system())
    table.add_row("Release", platform.release())
    table.add_row("Version", platform.version())
    table.add_row("Machine", platform.machine())
    table.add_row("Python", platform.python_version())

    console.print(table)
    input("\nPremi INVIO per tornare...")

# ========================= FAQ =========================

def faq():
    clear()
    text_it = (
        "[bold magenta]FAQ (Italiano)[/]\n\n"
        "1. Questo tool è illegale?\n"
        "   No, usa solo fonti OSINT pubbliche.\n\n"
        "2. Posso usarlo per indagare su qualcuno?\n"
        "   Solo per scopi legittimi e autorizzati.\n\n"
        "3. Sei responsabile se mi metto nei guai?\n"
        "   No, l'uso improprio è a tua responsabilità.\n\n"
        "4. Fa hacking?\n"
        "   No, non esegue exploit o intrusioni.\n\n"
        "5. Posso usarlo per cybersecurity?\n"
        "   Sì, per analisi e formazione.\n\n"
    )

    text_en = (
        "[bold magenta]FAQ (English)[/]\n\n"
        "1. Is this tool illegal?\n"
        "   No, it uses only public OSINT sources.\n\n"
        "2. Can I investigate someone with it?\n"
        "   Only for legitimate, authorized purposes.\n\n"
        "3. Are you responsible if I get in trouble?\n"
        "   No, misuse is entirely your responsibility.\n\n"
        "4. Does it perform hacking?\n"
        "   No, it does not exploit or break into systems.\n\n"
        "5. Can I use it for cybersecurity?\n"
        "   Yes, for analysis, training and security checks.\n\n"
    )

    console.print(Panel(text_it, border_style="magenta"))
    console.print(Panel(text_en, border_style="magenta"))
    input("\nPremi INVIO per tornare...")

# ========================= DISCLAIMER =========================

def disclaimer():
    clear()
    text_it = (
        "[bold red]DISCLAIMER (Italiano)[/]\n\n"
        "Questo tool è stato creato esclusivamente a scopo informativo ed educativo.\n"
        "Non incoraggio, non approvo e non sono responsabile di alcun uso improprio,\n"
        "illegale o dannoso di questo software. Chiunque lo utilizzi per attività non\n"
        "autorizzate, violazioni della privacy, stalking, hacking, truffe o altre azioni\n"
        "illegali lo fa sotto la propria totale responsabilità.\n\n"
    )

    text_en = (
        "[bold red]DISCLAIMER (English)[/]\n\n"
        "This tool was created solely for informational and educational purposes.\n"
        "I do not encourage, endorse, or take responsibility for any misuse, illegal\n"
        "activity, or harmful behavior involving this software. Anyone using it for\n"
        "unauthorized activities, privacy violations, stalking, hacking, fraud, or\n"
        "any other illegal action does so entirely at their own risk.\n\n"
    )

    console.print(Panel(text_it, border_style="red"))
    console.print(Panel(text_en, border_style="red"))
    input("\nPremi INVIO per tornare...")

# ========================= DISCORD =========================

def discord_link():
    clear()
    console.print(Panel(
        "[cyan]Join the official /attack community:\n\n"
        "[bold magenta]https://discord.gg/kKVfJ5WxpK[/]",
        title="[magenta]DISCORD SERVER[/]",
        border_style="magenta"
    ))
    input("\nPremi INVIO per tornare...")

# ========================= MAIN =========================

def main():
    splash()

    while True:
        dashboard()
        choice = input("\nSeleziona ID: ").strip()

        if choice == "0":
            pass
        elif choice == "1":
            osint()
        elif choice == "2":
            network()
        elif choice == "3":
            social()
        elif choice == "4":
            cyber()
        elif choice == "5":
            system_info()
        elif choice == "6":
            faq()
        elif choice == "7":
            disclaimer()
        elif choice == "8":
            discord_link()
        elif choice == "9":
            clear()
            console.print("[red]Exiting /attack...[/]")
            sys.exit()
        else:
            console.print("[red]Scelta non valida[/]")
            time.sleep(1)

if __name__ == "__main__":
    main()

