# DATA-PIPELINE-DEVELOPMENT

*COMPANY*:CODETECH IT SOLUTIONS

*NAME*:MAHVEEN SULTANA

*INTERN ID*:CT04DZ47

*DOMAIN*:DATA SCIENCE

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTOSH

*ENTER DESCRIPTION OF TASK*:

As part of the CODTECH Data Science Internship – Task 1, I developed a Data Pipeline for Preprocessing, Transformation, and Loading (ETL) using Python. This task involved building an automated process to handle raw data, clean it, transform it into a usable format, and save the final processed dataset for future analysis or modeling.
The chosen dataset for this pipeline was the Iris dataset, a widely used dataset in data science and machine learning for classification tasks. It consists of 150 samples with four numerical features: sepal length, sepal width, petal length, and petal width, along with a target column indicating the flower species.


What I Performed in the Task

The task followed the ETL process – Extract → Transform → Load.

1. Extracting Data

I loaded the Iris dataset using sklearn.datasets.load_iris() and converted it into a Pandas DataFrame for easy handling.

This step mimics extracting data from a database, CSV file, or API.

2. Preprocessing (Handling Missing Values)

To simulate real-world scenarios where data often has missing values, I intentionally introduced missing values in the dataset for testing the pipeline’s robustness.

I checked for missing values using df.isnull().sum() and then handled them by replacing missing entries with the mean of the respective columns. This ensures data consistency without losing valuable information.

3. Transformation (Feature Scaling)

Data often has varying scales, which can negatively affect machine learning models.

I used StandardScaler from sklearn.preprocessing to scale the numerical features, ensuring they have a mean of 0 and a standard deviation of 1.

After scaling, I created a new DataFrame df_scaled that retained the transformed feature values while keeping the target column intact.

4. Loading Processed Data

Finally, I saved the processed and transformed dataset into a CSV file named processed_iris.csv.

This simulates the Load step in a real ETL pipeline, where cleaned data is stored for downstream tasks like analytics or machine learning.


Tools and Libraries Used:

Python 3.x → The programming language used for the entire pipeline.

Pandas → For data extraction, manipulation, cleaning, and saving the processed data.

Scikit-learn → For loading the Iris dataset and applying StandardScaler for data transformation.

NumPy → Used internally by Pandas and Scikit-learn for numerical operations.


Editor/Platform Used:

I used Visual Studio Code (VS Code) as the primary editor to write and execute the Python script.
Alternatively, this pipeline can also be executed in Jupyter Notebook or Google Colab, which are popular platforms for data science projects.

Where This Task is Applicable in Real Life:
This Data Pipeline Development task is highly relevant in real-world data science and data engineering scenarios:

Data Cleaning in Organizations
Companies often receive raw data from various sources like databases, APIs, IoT devices, or user inputs. This data may have missing values, inconsistencies, and different scales. A pipeline like this automates cleaning, ensuring data quality.

ETL (Extract, Transform, Load) in Data Warehousing
Organizations use ETL pipelines to move raw data from transactional systems into data warehouses or data lakes after preprocessing and transformation.

Preprocessing for Machine Learning Models
Before training any ML model, the dataset must be cleaned, normalized, and transformed. The pipeline ensures data is ready for model building without manual effort every time.

Automation in Business Intelligence
Automated pipelines like this feed BI dashboards with clean, updated data, reducing manual work for data analysts.

Healthcare, Finance, and Retail Industries

In healthcare, such pipelines clean patient data before predictive analysis.

In finance, they preprocess financial transaction data for fraud detection

#OUTPUT:
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/a4ba8b33-38a8-45fb-beb5-893b5444eedb" />
