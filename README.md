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

### Terraform Configuration

```
main.tf: Defines the AWS resources (web server and database server instances).
variables.tf: Specifies variables used in the Terraform configuration.
outputs.tf: Outputs the public IP addresses of the VMs.
provider.tf: Configures the AWS provider.
```

### Ansible Configuration

```
ansible.cfg: Configures Ansible to use the dynamic inventory script.
terraform_inventory.py: Generates the Ansible inventory dynamically based on Terraform outputs.
playbook.yml: Ansible playbook that runs roles for web server and database server configurations.
roles/webserver: Contains tasks and templates for configuring Nginx on the web server.
	tasks/main.yml: Installs and configures Nginx, and deploys the SSL certificates and the site configuration.
	templates/custom_nginx_site.j2: Nginx configuration template for the site.
	templates/index.html.j2: HTML template for the web server's home page.
roles/db: Contains tasks and files for configuring MariaDB and deploying the Flask application.
	tasks/main.yml: Installs and configures MariaDB, and sets up the Flask application.
	files/rest-api.py: Flask application providing a REST API to fetch data from the MariaDB database.
	files/requirements.txt: Specifies dependencies for the Flask application.
	files/db_setup.sql: SQL script to set up the database schema and insert mock data.
```

### Web Server Configuration

Hostname Configuration


The hostname for the web server is dynamically generated based on the public IP address of the instance. The terraform_inventory.py script generates hostnames in the format ws-<ip>.dru-testing.com, where <ip> is the public IP address with dots replaced by dashes. This will need to be later added to the DNS to be able to access the webserver via HTTPS.


Nginx Configuration


Nginx is configured to serve the web application over HTTPS using self-signed SSL certificates. The configuration steps are as follows:

	1. Install Nginx:
	   The main.yml file in the webserver role installs Nginx and ensures it is running.

	2.Deploy SSL Certificates:
	   The self-signed SSL certificates are copied from the certs directory to the appropriate location on the web server.

	3. Nginx Site Configuration:
	   The Nginx site configuration is defined in the custom_nginx_site.j2 template. This configuration sets up the server to listen on port 80 and redirect HTTP traffic to HTTPS on port 443. The SSL certificates are specified in this configuration.

	4. Deploy HTML Template:
	   The index.html.j2 template is used to create the home page for the web server. This file is deployed to the /var/www/html directory on the web server.


#Contact

For any qustions, please contact [puiu.alex93@gmail.com].
