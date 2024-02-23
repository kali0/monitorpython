import os
import platform
import subprocess
from scapy.all import sniff, IP,  TCP, UDP, send, Ether, ARP
from scapy.layers import http

# Dictionary to store the websites accessed by each device
websites_accessed = {}

# Função para verificar a disponibilidade de um host usando o comando ping
def ping(host):
    operating_system = platform.system().lower()

    # Executa o comando ping com base no sistema operacional
    if operating_system == "windows":
        ping_command = ['ping', '-n', '1', '-w', '1000', host]
    else:
        ping_command = ['ping', '-c', '1', '-W', '1', host]

    try:
        subprocess.check_output(ping_command)
        return True
    except subprocess.CalledProcessError:
        return False

# Função para capturar e analisar o tráfego HTTP
def capture_http_traffic(packet):
    if packet.haslayer(http.HTTPRequest):
        # Extrai informações relevantes, como o endereço IP de origem e a URL acessada
        src_ip = packet[IP].src
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

        # Armazena a informação no dicionário
        if src_ip in websites_accessed:
            websites_accessed[src_ip].append(url)
        else:
            websites_accessed[src_ip] = [url]

        print(f"Dispositivo {src_ip} acessou: {url}")

# Lista de hosts para monitorar
hosts = ['192.168.0.1', '192.168.0.166', '192.168.0.160', '192.168.0.162']

print("Monitoramento em andamento...")

# Inicia o monitoramento do tráfego HTTP
sniff(prn=capture_http_traffic, filter="tcp port  80 or tcp port 443", store=False)

# Verifica se cada host está online e armazena as URLs acessadas por cada dispositivo
for host in hosts:
    if not ping(host):
        print(f"\t{host}: Offline")
    else:
        print(f"\t{host}: Online")
        urls_accessed = websites_accessed.get(host)
        if urls_accessed is None:
            print("\t\tNenhuma acesso à internet registrado.")
        else:
            for url in urls_accessed:
                print(f"\t\t{url}")

# Loop para verificar a disponibilidade dos hosts
for host in hosts:
    if ping(host):
        print(f"O host {host} está disponível.")
    else:
        print(f"O host {host} está indisponível.")

# Captura o tráfego de rede em tempo real
def start_traffic_capture():
    sniff(filter="tcp port 80", prn=capture_http_traffic, store=0)

# Inicia a captura de tráfego
start_traffic_capture()

# Print the websites accessed by each device
for device, websites in websites_accessed.items():
    print(f"Websites acessados pelo dispositivo {device}:")
    for website in websites:
        print(f"- {website}")
