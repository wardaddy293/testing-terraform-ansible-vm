# VM Deployment with Terraform and Ansible

## Overview

This project automates the deployment and configuration of a web server and a database server using Terraform and Ansible. The web server runs Nginx, and the database server runs MariaDB with a Flask application providing a REST API to access data from the database.

## Assumptions

1. **Operating System**: Both VMs use Debian 11.
2. **Cloud Provider**: AWS is used for deploying the VMs.
3. **AWS Region**: The region used is `eu-west-3` (Paris).
4. **Certificates**: Self-signed SSL certificates are used for HTTPS configuration on Nginx.
5. **Dynamic Inventory**: Ansible uses a dynamic inventory script to obtain the IP addresses of the VMs from Terraform outputs.
6. **Database**: MariaDB is used as the database server.
7. **REST API**: Flask is used to create a REST API to fetch data from the database.

## Prerequisites

- Terraform
- Ansible
- AWS CLI
- Python 3 and pip
- Access to AWS with appropriate permissions to create VMs


## Deployment Instructions

**Step 1: Clone the Repository**

```sh
git clone https://github.com/yourusername/vm-deployment-with-terraform-ansible.git
cd vm-deployment-with-terraform-ansible
```

**Step 2: Initialize and Apply Terraform Configuration**

```sh
cd terraform
terraform init
terraform apply -auto-approve
```

**Step 3: Configure Ansible Inventory**

Terraform outputs the IP addresses of the created VMs. The terraform_inventory.py script dynamically generates the Ansible inventory based on these outputs.

**Step 4: Run Ansible Playbook**

```sh
cd ../ansible
ansible-playbook playbook.yml
```
**Step 5: Make a REST Call to the Flask Application**

 Replace <database_server_ip> with the actual IP address of your database server

```sh
curl http://<database_server_ip>:5000/top_scorers
```

 Expected Output

```json
[
    {
        "country": "Italy",
        "goals": 13
    },
    {
        "country": "Spain",
        "goals": 13
    },
    {
        "country": "England",
        "goals": 11
    },
    {
        "country": "Denmark",
        "goals": 12
    },
    {
        "country": "Switzerland",
        "goals": 9
    }
]
```

## Detailed Explanation of Files

#Terraform Configuration

main.tf: Defines the AWS resources (web server and database server instances).
variables.tf: Specifies variables used in the Terraform configuration.
outputs.tf: Outputs the public IP addresses of the VMs.
provider.tf: Configures the AWS provider.

#Ansible Configuration

ansible.cfg: Configures Ansible to use the dynamic inventory script.
terraform_inventory.py: Generates the Ansible inventory dynamically based on Terraform outputs.
playbook.yml: Ansible playbook that runs roles for web server and database server configurations.
roles/webserver: Contains tasks and templates for configuring Nginx on the web server.
roles/database: Contains tasks and files for configuring MariaDB and deploying the Flask application.

#Flask Application

app.py: Flask application providing a REST API to fetch data from the MariaDB database.
requirements.txt: Specifies dependencies for the Flask application.
db_setup.sql: SQL script to set up the database schema and insert mock data.

#Contact

For any qustions, please contact [puiu.alex93@gmail.com].
