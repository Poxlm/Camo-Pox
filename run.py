import subprocess
from colorama import Fore, Style, init
import time

init()

php_server_process = None
serveo_process = None

def start_php_server(port):
    php_server_command = f"php -S localhost:{port}"
    php_server_process = subprocess.Popen(php_server_command, shell=True)
    print(Fore.GREEN + "PHP Server Started" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Port: {port}" + Style.RESET_ALL)
    return php_server_process

def start_serveo_tunnel(port, subdomain):
    serveo_command = f"ssh -R {subdomain}:80:localhost:{port} serveo.net"
    serveo_process = subprocess.Popen(serveo_command, shell=True)
    print(Fore.CYAN + "Creating Serveo Tunnel..." + Style.RESET_ALL)
    print(Fore.YELLOW + f"Subdomain: {subdomain}" + Style.RESET_ALL)
    return serveo_process

def stop_all_tunnels(php_server_process, serveo_process):
    if php_server_process:
        php_server_process.terminate()
        print(Fore.YELLOW + "PHP Server Stopped" + Style.RESET_ALL)
    if serveo_process:
        serveo_process.terminate()
        print(Fore.YELLOW + "Serveo Tunnel Stopped" + Style.RESET_ALL)

def loading_animation(duration):
    animation = "|/-\\"
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(4):
            print(Fore.CYAN + "Loading " + animation[i % 4] + Style.RESET_ALL, end="\r")
            time.sleep(0.2)

if __name__ == "__main__":
    print(Fore.YELLOW + "📸 Camo Pox 📸" + Style.RESET_ALL)
    
    port = input("🚀 Enter the Port for Your PHP Server (e.g., 8000): ").strip()
    if not port.isdigit():
        print(Fore.RED + "Invalid Port Number. Please Provide a Valid Port." + Style.RESET_ALL)
        exit()

    subdomain = input("🔗 Enter Your Desired Subdomain: ").strip()
    
    if not subdomain:
        print(Fore.RED + "Please Provide a Subdomain." + Style.RESET_ALL)
        exit()

    print(Fore.CYAN + "Starting servers and creating tunnels..." + Style.RESET_ALL)
    loading_animation(2)  

    php_server_process = start_php_server(port)
    serveo_process = start_serveo_tunnel(port, subdomain)
    serveo_link = f"https://{subdomain}.serveo.net"

    print(Fore.GREEN + "Serveo Tunnel Link:" + Style.RESET_ALL)
    print(Fore.CYAN + serveo_link + Style.RESET_ALL)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_all_tunnels(php_server_process, serveo_process)
        print(Fore.YELLOW + "Exiting Camo Pox. Goodbye!" + Style.RESET_ALL)
