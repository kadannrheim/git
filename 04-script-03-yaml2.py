#!/usr/bin/env python3

import socket
import time
import json
import yaml

servers = {"drive.google.com": "", "mail.google.com": "", "google.com": ""}
while True:
    for url, ip in servers.items():
        ip_addr = socket.gethostbyname(url)
        if ip == "":
            servers[url] = ip_addr
            print("{} - {}".format(url, ip_addr))
        elif ip != ip_addr:
            print("[error] {} IP mismatch: {} -> {}".format(url, ip, ip_addr))
            servers[url] = ip_addr
    with open('servers.json', 'w') as json_file:
        json_file.write(json.dumps(servers, indent=2))
    with open('servers.yaml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(servers, indent=2, explicit_start=True, explicit_end=True))
    time.sleep(2)