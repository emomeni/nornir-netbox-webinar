#!./venv/bin/python

from nornir import InitNornir
import json

nr = InitNornir(config_file="config.yaml")

for host in nr.inventory.hosts.values():
    host_data = host.dict()
    formatted_json = json.dumps(host_data, indent=4)
    print(formatted_json)
