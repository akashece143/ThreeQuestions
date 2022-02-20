How to deploy

 

1- Open AWS CloudFormation Service >> Create Stack >> paste the whole code  >> Run

2- It will ask below Parameters

    1- Stack Name

    2- DBAllocatedStorage           

    3- DBInstanceID     

    4- DBMultiAZ         (default is false)

    5- Engine             (1-mysql 2-postgres 3-oracle-ee 4-sqlserver-se)

    6- MaxAllocatedStorage

    7- PreferredBackupWindow       (default is mentioned)

    8- PreferredMaintenacneWindow  (default is mentioned)

    9- RDSName

   10- SubnetId1     

   11- SubnetId2

   12- VpcCid

 

What this stack does

1- We can create Database of our choice from below -

   Mysql

   postgres

   oracle-ee

   sqlserver-se

 

2- It is creating DB and Db Security group and adding rule in it