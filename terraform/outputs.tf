# Output the public IP of webserver VM
output "web_public_ip" {
  description = "The public IP address of the webserver VM"
  value       = aws_instance.web.public_ip
}

# Output the public IP of DB VM
output "db_public_ip" {
  description = "The public IP address of the DB VM"
  value       = aws_instance.db.public_ip
}

