# End-to-End Cricket Analytics Pipeline: Cloud Data Engineering with Cricbuzz API and Google Cloud

This cricket analytics pipeline is a complete, automated system that transforms live cricket data into visual dashboards using Google Cloud Platform. The project demonstrates modern data engineering practices by connecting multiple cloud services to create an end-to-end solution for sports data analytics.

## Architecture



<img width="837" height="388" alt="Architecture_Graphical_abstract drawio" src="https://github.com/user-attachments/assets/6f74c29e-6cd7-416a-a265-2b9d5386c4cb" />



<img width="765" height="350" alt="CricBuzz_Tech_Graphical_abstarct drawio" src="https://github.com/user-attachments/assets/2371b145-72a0-4518-a15e-c66cef3961f5" />



## The role of Data Engineering and Google cloud platforms
In today's data-driven world, data engineering serves as the critical backbone that transforms raw information into actionable insights. Data engineers build the pipelines, infrastructure, and systems that enable organizations to collect, process, store, and analyze vast amounts of data efficiently. As data volumes grow exponentially and real-time analytics become increasingly essential, scalable and reliable data infrastructure is no longer a luxury—it's a business necessity.

Google Cloud Platform (GCP) has emerged as a leading solution for modern data engineering challenges by offering a comprehensive, fully-managed ecosystem of services. GCP provides:

-**Serverless Architecture**: Services like Cloud Functions and Dataflow eliminate infrastructure management overhead

-**Seamless Integration**: Native connectivity between storage, processing, and analytics services

-**Real-time Processing**: Capabilities for both batch and streaming data pipelines

-**Cost Efficiency**: Pay-as-you-go pricing with automatic scaling

-**Enterprise Security**: Built-in security, compliance, and governance features

This project demonstrates how GCP's integrated services can be leveraged to build production-ready data pipelines that are scalable, maintainable, and cost-effective for organizations of all sizes.


## What This Project Does:

<img width="1123" height="615" alt="Screenshot 2026-01-28 012827" src="https://github.com/user-attachments/assets/38cec382-15ba-4486-a6e1-8726d3381d88" />


-**Data Collection**: Python scripts extract real-time cricket statistics (player rankings, match scores, team performance) from the Cricbuzz API.

-**Automated Processing**: When new data arrives in Cloud Storage, automated triggers initiate data processing pipelines without manual intervention.

-**Data Transformation**: Google Dataflow cleans, formats, and prepares the raw data for analysis, handling tasks like data validation, error correction, and format standardization.

-**Centralized Storage**: Processed data is stored in BigQuery, Google's cloud data warehouse, making it easily accessible for querying and analysis.

-**Visualization**: Interactive dashboards in Looker Studio display player rankings, performance trends, and statistical insights through charts, graphs, and tables.
