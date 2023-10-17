#!./venv/bin/python

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def napalm_get_lldp_neighbors(task):
	task.run(task=napalm_get, getters=["lldp_neighbors"])

results=nr.run(task=napalm_get_lldp_neighbors)

print_result(results)
