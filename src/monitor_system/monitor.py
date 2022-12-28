import os

class monitorSystem:
    def system_details():
        local_dict = {}
        system_details = os.uname()
        list_data = ["sysname", "nodename", "release", "version", "machine"]
        for item in list_data:
            try:
                output = getattr(system_details, item)
                local_dict[item] = output
            except Exception as err:
                local_dict[item] = str(err)
        return local_dict
    
    def ram():
        local_dict = {}
        return local_dict


c = monitorSystem.system_details()
print(c)