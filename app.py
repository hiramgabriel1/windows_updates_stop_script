import subprocess

# TODO: stop service updates windows
def stop_services_windows_update():
    # & command to stop service: net stop wuauserv
    subprocess.run(["sc", "stop", "wuauserv", "/f"], shell=True)

# TODO: stop service update in start PC
def stop_services_windows_start():
    # & command to stop service at start PC
    subprocess.run(["sc", "config", "wuauserv", "start=disabled"], shell=True)
    
# TODO: start service updates windows
def start_services_windows_updates():
    # & command to start service: net start wuauserv
    subprocess.run(["net", "start", "wuauserv"], shell=True)
    
# TODO: run app!
if __name__ == "__main__":
    stop_services_windows_update()