from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware_instance = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware_instance)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware_instance = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware_instance)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as exc:
            return str(exc)

        # if hardware_name not in [hardware.name for hardware in System._hardware]:
        #     return 'Hardware does not exist'
        # software = ExpressSoftware(name, capacity_consumption,memory_consumption)
        # hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
        # try:
        #     hardware.install(software)
        #     System._software.append(software)
        # except Exception as exc:
        #     return exc.args[0]

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as exc:
            return str(exc)
        # if hardware_name not in [hardware.name for hardware in System._hardware]:
        #     return 'Hardware does not exist'
        # software = LightSoftware(name, capacity_consumption, memory_consumption)
        # hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
        # try:
        #     hardware.install(software)
        #     System._software.append(software)
        # except Exception as exc:
        #     return exc.args[0]

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
            software = [software for software in System._software if software.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return 'Some of the components do not exist'

        # hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
        # software = [software for software in System._software if software.name == software_name][0]
        # if not hardware or not software:
        #     return 'Some of the components do not exist'
        # else:
        #     hardware.uninstall(software)
        #     System._software.remove(software)

    @staticmethod
    def analyze():
        result = 'System Analysis\n'
        result += f'Hardware Components: {len(System._hardware)}\n'
        result += f'Software Components: {len(System._software)}\n'
        result += f'Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum(h.memory for h in System._hardware)}\n'
        result += f'Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} / {sum(h.capacity for h in System._hardware)}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}\n'
            result += f'Express Software Components: {len([el for el in hardware.software_components if el.type == "Express"])}\n'
            result += f'Light Software Components: {len([el for el in hardware.software_components if el.type == "Light"])}\n'
            result += f'Memory Usage: {sum([el.memory_consumption for el in hardware.software_components])} / {hardware.memory}\n'
            result += f'Capacity Usage: {sum([el.capacity_consumption for el in hardware.software_components])} / {hardware.capacity}\n'
            result += f'Type: {hardware.type}\n'
            names = ", ".join([el.name for el in hardware.software_components])
            result += f'Software Componets: {names if names else None}'
            # if hardware.software_components:
            #     result += f'Software Componets: {", ".join([el.name for el in hardware.software_components])}\n'
            # else:
            #     result += 'None'

        return result
