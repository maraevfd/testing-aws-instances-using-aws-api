Marayeu Fiodar Task 1: acquaintance with boto3
==============================================
Get information about AWS ec2 instance using boto3. 
(instance-id: i-06007db6d3063ca53)
Create Python wrapper classes for EC2Instance, EBSVolume and NetworkInterface 
which would contain all needed attributes for appropriate class description.
---
Wrapper classes and their attributes:
EC2Instance:
 - volumes
 - network_interfaces
 - get_tags
 - get_image_id
 - get_private_ip
 - get_public_ip
 - get_state
 - get_security_groups
 - get_total_information
---
EBSVolume:
 - get_tags
 - get_size
 - get_type
 - get_state
 - get_total_information
---
NetworkInterface:
 - get_tags
 - get_tenant
 - get_ip_address
 - get_dns_name
 - get_status
 - get_vpc_id
 - get_total_information
### How to use:
To get all the necessary information you need to use run.py file.
You must pass the identifier and region of this instance to the constructor of the class.
Further, using its methods, you can get the necessary information.
