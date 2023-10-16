from nornir import InitNornir
from nornir_napalm .plugins.tasks import  napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date
import pathlib

def backup_device_configs(task):
    backup_directory = "backups"
    pathlib.Path(backup_directory).mkdir(exist_ok=True)
    r = task.run(task=napalm_get, getters=["get_config"])
    task.run(
        task=write_file,
        content=r.result["get_config"]["running"],
        filename=f"" + str(backup_directory) + "/" + str(task.host.name) + str(date.today()) + ".cfg",
    )


nr = InitNornir(config_file="config.yaml")


result = nr.run(
    name="Creating Backup Archive", task=backup_device_configs
)

print_result(result)
