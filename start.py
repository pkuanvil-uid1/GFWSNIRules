#!/bin/python
import json
import os
import platform
import subprocess

def parse_rules(filename):
    with open(filename) as file:
        rules = json.load(file)

    host_rules = rules.get("host-rules", [])
    host_resolver_rules = rules.get("host-resolver-rules", [])

    return {
        "host-rules": ", ".join(host_rules),
        "host-resolver-rules": ", ".join(host_resolver_rules)
    }

def get_chrome_path():
    chrome_env = os.getenv('CHROME')
    if chrome_env:
        return chrome_env
    # Modify your chrome install path here
    os_platform = platform.system()
    if os_platform == "Windows":
        return r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
    elif os_platform == "Linux":
        return "google-chrome"
    else:
        return "Please enter your chrome path here"

def generate_command_line(rules):
    command_line = get_chrome_path()
    
    if "host-rules" in rules:
        command_line += f' --host-rules="{rules["host-rules"]}"'

    if "host-resolver-rules" in rules:
        command_line += f' --host-resolver-rules="{rules["host-resolver-rules"]}"'

    # Ignore certificate errors
    command_line += " --ignore-certificate-errors"

    return command_line

rules = parse_rules("rules.json")
command_line = generate_command_line(rules)

# Run the command
print(command_line)
subprocess.run(command_line, shell=True)
