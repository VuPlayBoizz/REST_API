output "ec2_security_group_id" {
    value = aws_security_group.ec2_security_group.id
}

output "rds_mysql_security_group_id" {
    value = aws_security_group.rds_mysql_security_group.id
}