# ThreeQuestions
Three Tier Architecture,Instance metadata query and Python Function

## **1st-Quest-3tierArchitecture**

### ALB WITH AUTOSCALING

**_How to deploy_** 

  1- Open AWS CloudFormation Service >> Create Stack >> paste the whole code  >> Run

  2- It will ask below Parameters

       1- Stack Name

       2- ImageID            (default is mentioned for North Virginia)

       3- Instance Size      (default is t2.small)

       4- KeyName

       5- LaunchTemplate version (default 1)

       6- MyALBName           (default is mentioned and it should be unique)

       7- SNASubscription Email

       8- Subnet1       (Subnet for ALB)

       9- Subnet2       (Subnet for ALB)

      10- Subnets       (EC2 Subnets)

      11- VPC
      
**_What this stack does_**

   1- It is creating one Application load balancer

   2- It is creating Target group

   3- It is creating Autoscaling group

   4- It is creating Launch configuration

   5- It is creating Ec2 servers in autoscaling group

   6- It is creating SNS topic  for emails

   7- It is creating Security group for ALB

   8- It is creating instance security group

   9- It is adding rules in security group

   10- Health check paramters of ALB  are also adding by this script

   11- It is adding listners in ALB

   12- It is also adding scaling policies

   13- It is installing http server in EC2


 ### RDS (MYSQL,Postres,Mssql,Oracle)

**_How to deploy_**

1- Open AWS CloudFormation Service >> Create Stack >> paste the whole code  >> Run

2- It will ask below Parameters

    1- Stack Name

    2- DBAllocatedStorage           

    3- DBInstanceID     

    4- DBMultiAZ         (default is false)

    5- Engine             
       - mysql
       - postgres
       - oracle-ee
       - sqlserver-se
       

    6- MaxAllocatedStorage

    7- PreferredBackupWindow       (default is mentioned)

    8- PreferredMaintenacneWindow  (default is mentioned)

    9- RDSName

   10- SubnetId1     

   11- SubnetId2

   12- VpcCid

_  **What this stack does**_
 
 1- We can create Database of our choice from below -

   Mysql

   postgres

   oracle-ee

   sqlserver-se

 2- It is creating DB and Db Security group and adding rule in it
