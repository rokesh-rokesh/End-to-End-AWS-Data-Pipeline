# Building an end-to-end data pipeline on AWS:
In this AWS-based end-to-end data pipeline,Finanical balance sheet data is retrieved from an API using AWS Lambda, and the parsed information is temporarily stored in an Amazon S3 bucket. AWS Glue Crawlers are employed to dynamically identify and update the schema of the raw data within the S3 storage. A Glue PySpark job is developed to perform data transformations, and the processed data is loaded into Amazon Redshift for efficient storage and retrieval. Amazon Athena is utilized for querying the data directly from the Redshift. Finally, insights are gained through visualization using Amazon QuickSight, which connects seamlessly to the Athena data source, enabling a comprehensive and data analytics and visualization workflow.

![AWS project(1)](https://github.com/rokesh-rokesh/End-to-End-AWS-Data-Pipeline/assets/84179582/f31add9c-d50b-48b5-b618-c2549fb194b2)


##   1.Download Company Balance Sheet from API:
 Identify the API endpoint and authentication mechanisms.
        Create an AWS Lambda function to periodically fetch data from the API.
        Parse the response and store the data temporarily.

##    2.Data Ingestion into S3 using Lambda:
Set up an Amazon S3 bucket to store the raw data.
        Modify the Lambda function to upload the parsed data to the S3 bucket.

##    3.Data Crawling using AWS Glue Crawlers:
 Create an AWS Glue Crawler to discover the schema of the raw data in the S3 bucket.
        Schedule the crawler to run at specified intervals to keep the schema updated.

##    4.Data Transformation using Glue PySpark Job:
 Develop a PySpark script to transform the raw data into a suitable format.
        Create an AWS Glue PySpark job, upload the script, and configure the job to run on the transformed data.
        Schedule the Glue job to run periodically to process new data.

##    5.Load Data into Amazon Redshift:
   Set up an Amazon Redshift cluster to store the transformed data.
        Configure the Glue PySpark job to load the transformed data into Redshift using JDBC connections.

##    6.Query Data using Amazon Athena:
  Create an Amazon Athena table that points to the data stored in Amazon Redshift.
        Write SQL queries in Athena to analyze and explore the data.
        ![Athena_img(1)](https://github.com/rokesh-rokesh/End-to-End-AWS-Data-Pipeline/assets/84179582/731ea8b1-f49a-4a38-86fb-dd67b645998a)


##    7.Visualize Data using Amazon QuickSight:
  Set up an Amazon QuickSight account.
        Connect QuickSight to the Amazon Athena data source.
        Create visualizations, dashboards, and analyses in QuickSight to gain insights into the data.
        
  ![Current_ratio_2024-01-19T09_20_36_page-0001](https://github.com/rokesh-rokesh/End-to-End-AWS-Data-Pipeline/assets/84179582/c82e577e-b6a8-414d-b3ed-99dea4a88412)
