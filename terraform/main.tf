#Webserver VM definition

resource "aws_instance" "web" {
  ami           = "ami-0f392485798778f4f"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServer"
  }

  provisioner "local-exec" {
    command = "echo ${aws_instance.web.public_ip} >> ../ansible/hosts"
  }
}

#DB VM definition

resource "aws_instance" "db" {
  ami           = "ami-0f392485798778f4f"
  instance_type = "t2.micro"

  tags = {
    Name = "Database"
  }

  provisioner "local-exec" {
    command = "echo ${aws_instance.db.public_ip} >> ../ansible/hosts"
  }
}

