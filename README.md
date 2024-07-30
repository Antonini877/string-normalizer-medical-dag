# Medical Text Feature Extraction with Apache Airflow

## Overview

This project demonstrates how to use Apache Airflow to automate the process of reading a CSV file containing medical names, processing the text, and creating feature columns. The project includes the following steps:

1. **Reading a CSV file**: The CSV file contains medical names that need to be processed.
2. **Text Processing**: The text is processed to extract meaningful features.
3. **Feature Creation**: The processed text is used to create new feature columns.
4. **Storing the Results**: The final processed data with the new feature columns is stored in a SQL database for further analysis.

## Prerequisites

To run this project, you need the following:

1. **Docker and Docker Compose**: To containerize the Airflow environment.
2. **Apache Airflow**: To manage the workflow.
3. **MySQL Database**: To store the processed data.
4. **Python Packages**: pandas.



- **dags/medical_feature_extraction_dag.py**: Contains the DAG definition for the workflow.
- **scripts/text_processing.py**: Contains the text processing and feature extraction logic.
- **docker-compose.yml**: Docker Compose file to set up the Airflow environment.

## Setup



1. **Set Up the Environment**:
    Ensure you have Docker and Docker Compose installed on your machine.

2. **Start the Airflow Services**:
    ```sh
    docker compose up airflow-init
    ```

3. **Start the Airflow Services**:
    ```sh
    docker compose up 
    ```

4. **Access the Airflow UI**:
    Open your browser and go to `http://localhost:8080` to access the Airflow web interface.



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, please contact [antonio.frioli1@gmail.com].

---

Feel free to customize this README to fit your specific project details and requirements.