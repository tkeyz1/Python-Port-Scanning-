# BASIC PORT SCANNER

#import socket 
from rich.table import Table
from rich.console import console 
from rich.live import live 
console - console()
import socket

target_ip ="192.168.1.1"
common_ports = [21,22,23,25,53,80,110,143,443,445,3389]
closed_ports =0
failed_ports =[]

table = Table(title="Port Scan", style="purple")
table.add_column("Port", style="yellow")
table.add_column("Status", style="green")


with Live(table, console=console, refresh_per_second=4):
    for port in common_ports:
        try:
            with socket.socket(socket.AF_TNET, socket. SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target_ip, port))

                if result == 0:
                    table.add_row(str(port), "OPEN")
                                  
                else:
                    closed_ports +=1

        except Exception as e:
             failed_ports.append(port) 


if failed_ports != []:
    console.print(f"[red]FAILED Port(s): (failed_ports)")

console.print(f"[red]Closed/Filtered Port(s): (closed_ports)") 
console.print("[green]SCAN NOW COMPLETE[/green]")