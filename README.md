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
 - tags
 - image_id
 - private_ip
 - public_ip
 - state
 - security_groups
 - total_information
---
EBSVolume:
 - tags
 - size
 - type
 - state
 - total_information
---
NetworkInterface:
 - tags
 - tenant
 - ip_address
 - dns_name
 - status
 - vpc_id
 - total_information
### How to use:
To get all the necessary information you need to use run.py file.
You must pass the identifier and region of this instance to the constructor of the class.
Further, using its attributes, you can get the necessary information.
