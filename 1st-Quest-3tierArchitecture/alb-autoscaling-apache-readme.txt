How to deploy
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

 
What this stack does
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