import os
import platform
import subprocess

# Função para realizar o ping em um endereço IP
def ping(ip):
    # Verifica o sistema operacional
    sistema = platform.system().lower()
    
    # Configurações de comando de ping para Windows
    if sistema == "windows":
        comando = ['ping', '-n', '1', ip]  # "-n 1" envia apenas 1 pacote
    else:
        comando = ['ping', '-c', '1', ip]  # Para Linux ou Mac
    
    # Executa o comando de ping e retorna o status
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Verifica o retorno do comando
    if resultado.returncode == 0:
        return True  # IP está ativo
    else:
        return False  # IP não está ativo

# Função para escanear a rede
def escanear_rede(ip_range):
    ativos = []
    
    # Faz o ping em todos os IPs no intervalo
    for i in range(1, 255):  # Varre de .1 até .254
        ip = f"{ip_range}.{i}"
        if ping(ip):
            ativos.append(ip)  # Adiciona IP ativo à lista
    
    return ativos

# Defina o intervalo de IPs para escanear (ajuste conforme a sua rede)
# Exemplo: se o seu IP local for 192.168.1.10, você usaria 192.168.1
ip_range = "192.168.1"

# Escaneia a rede e exibe os IPs ativos
ips_ativos = escanear_rede(ip_range)

if ips_ativos:
    print("Dispositivos ativos encontrados na rede:")
    for ip in ips_ativos:
        print(ip)
else:
    print("Nenhum dispositivo ativo encontrado.")
