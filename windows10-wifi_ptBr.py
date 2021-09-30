import subprocess
import re

command_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"],
    capture_output=True).stdout.decode(encoding='iso-8859-1')

profile_names = (re.findall(r"[^:|\s]+$", command_output, flags=re.MULTILINE))
wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

        profile_info = profile_info.replace(r'\\s+', '')

        if re.search("Chave de segu.+:\s+Presente", profile_info):
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search(
                "(?<=Conte.do da Chave:).+\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)


for x in range(len(wifi_list)):
    print(wifi_list[x])
