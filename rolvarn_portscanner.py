import asyncio
import argparse
from colorama import Fore
from datetime import datetime

rolvarn_portscanner = Fore.RED + """
 ██▀███   ▒█████   ██▓  ██▒   █▓ ▄▄▄       ██▀███   ███▄    █                                         
▓██ ▒ ██▒▒██▒  ██▒▓██▒ ▓██░   █▒▒████▄    ▓██ ▒ ██▒ ██ ▀█   █                                         
▓██ ░▄█ ▒▒██░  ██▒▒██░  ▓██  █▒░▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒                                        
▒██▀▀█▄  ▒██   ██░▒██░   ▒██ █░░░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒                                        
░██▓ ▒██▒░ ████▓▒░░██████▒▒▀█░   ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░                                        
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▐░   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒                                         
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░                                        
  ░░   ░ ░ ░ ░ ▒    ░ ░     ░░    ░   ▒     ░░   ░    ░   ░ ░                                         
   ░         ░ ░      ░  ░   ░        ░  ░   ░              ░                                         
                            ░                                                                         
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                    ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                             ░                                                        
Only Educational Purposes                                                       by ~ ROLVARN          
======================================================================================================

"""
async def portscan(ip,port):
    try:
        reader, writer = await asyncio.open_connection(ip,port)

        print(Fore.GREEN+ "[+]"+Fore.WHITE+f" {ip}:"+Fore.LIGHTYELLOW_EX +f"{port}"+Fore.WHITE)
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def main():
    start = datetime.now()
    print(rolvarn_portscanner)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip",help="Hedef IP adresi",required=True)
    parser.add_argument("-p","--port",help="Hedef Port(lar)",required=True)
    args = parser.parse_args()
    ip_arg = args.ip
    port_arg = args.port


    
    ports = []
    if port_arg == "all":
        for p in range(1,65536):
            ports.append(portscan(ip_arg,int(p)))

    else:
        for p in port_arg.split(","):
            ports.append(portscan(ip_arg,int(p)))
    
    await asyncio.gather(*ports)
    print("Scan completed.")
    finish = datetime.now()
    duration = (finish-start).total_seconds()
    print("Estimated : "+ str(duration) + " sec.")


asyncio.run(main())