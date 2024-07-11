#!/usr/bin/env python3

import json
import subprocess

def get_terraform_output():
    result = subprocess.run(['terraform', 'output', '-json'], capture_output=True, text=True, cwd='../terraform')
    return json.loads(result.stdout)

def generate_hostname(ip, prefix):
    return f"{prefix}-{ip.replace('.', '-')}.dru-testing.com"

def main():
    terraform_output = get_terraform_output()

    web_public_ip = terraform_output['web_public_ip']['value']
    db_public_ip = terraform_output['db_public_ip']['value']

    inventory = {
        'webserver': {
            'hosts': [generate_hostname(web_public_ip, 'ws')]
        },
        'database': {
            'hosts': [generate_hostname(db_public_ip, 'db')]
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()

