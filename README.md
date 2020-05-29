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
---
### Task 2: Using your wrapper classes you should test AWS Instance.
##### The following tests were created for testing AWSInstance:
- test_instance_state
- test_instance_type
- test_network_interface_number
- test_instance_tags_count
- test_instance_tag_name
- test_instance_key_name
- test_root_device_type
- test_ebs_size
- test_network_interface_private_ip
- test_network_interface_public_ip
---
##### Special environment variables have been created:
- REGION_NAME = eu-central-1
- INSTANCE_ID = i-06007db6d3063ca53
- PATH_TO_PROJECT = /home/fedor/boto3_project/onboarding-qa