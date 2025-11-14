---

# NYC Yellow Taxi 2025 Analysis

## Project Overview

This project analyzes the **New York City Yellow Taxi dataset for 2025**, containing over 35 million trip records. The goal is to demonstrate skills in **data scraping, big data processing, PySpark, and data cleaning**, while extracting meaningful insights from a large-scale dataset.

The dataset includes details such as trip distance, fare, passenger count, pickup and dropoff locations, payment type, and other charges.

---

## Key Features / Skills Demonstrated

* **Web Scraping with Selenium:**

  * Automated browser interaction to extract dynamic content from web pages.
  * Located HTML elements using `div` attributes, handled expandable FAQ sections.
  * Managed edge cases like missing sections or delayed page loads.

* **PySpark Data Processing:**

  * Efficiently handled a 35M+ row dataset using PySpark DataFrames and SQL queries.
  * Data cleaning: removed nulls and filtered anomalous or negative values.
  * Partition management to avoid memory errors while writing large datasets.

* **Exploratory Analysis:**

  * Summary statistics for numeric columns (`trip_distance`, `fare_amount`, `total_amount`).
  * Passenger count distribution and average trip distance by payment type.

* **Parquet Storage:**

  * Saved cleaned and filtered datasets in **Parquet format** for efficient storage and retrieval.

* **Environment Management:**

  * Configured Python environment, Java (OpenJDK 11), and Spark for local execution.

---

## Dataset

The dataset has the following columns:

| Column                | Type      |
| --------------------- | --------- |
| VendorID              | integer   |
| tpep_pickup_datetime  | timestamp |
| tpep_dropoff_datetime | timestamp |
| passenger_count       | long      |
| trip_distance         | double    |
| RatecodeID            | long      |
| store_and_fwd_flag    | string    |
| PULocationID          | integer   |
| DOLocationID          | integer   |
| payment_type          | long      |
| fare_amount           | double    |
| extra                 | double    |
| mta_tax               | double    |
| tip_amount            | double    |
| tolls_amount          | double    |
| improvement_surcharge | double    |
| total_amount          | double    |
| congestion_surcharge  | double    |
| Airport_fee           | double    |
| cbd_congestion_fee    | double    |

---

## Environment Setup

1. **Python & PySpark**

   * Python 3.11
   * PySpark 3.x

2. **Java**

   * OpenJDK 11 installed and configured via `JAVA_HOME`.

3. **Selenium**

   * ChromeDriver installed for automating Chrome browser.
   * Managed dynamic content extraction with Selenium.

4. **Virtual Environment**

   * Used `venv` or `conda` to isolate dependencies.

5. **IDE**

   * Code tested in **PyCharm** and **Jupyter Notebook**.

---

## Steps Taken

### 1. Data Scraping (Selenium)

* Opened web pages and expanded sections dynamically:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
button = driver.find_element_by_css_selector("div[data-answer='faq2025']")
button.click()
```

* Extracted HTML content and saved raw text or structured data for analysis.

### 2. Load Data (PySpark)

```python
df = spark.read.parquet("yellow_tripdata_2025.parquet")
```

### 3. Data Cleaning

* Dropped nulls in critical columns.
* Filtered out negative fare or total_amount values.

### 4. Exploratory Data Analysis

* Summary statistics:

```python
df.describe("trip_distance", "fare_amount", "total_amount").show()
```

* Passenger count distribution:

```python
df.groupBy("passenger_count").count().show()
```

* Average trip distance by payment type:

```python
df.groupBy("payment_type").avg("trip_distance").show()
```

### 5. Save Cleaned / Filtered DataFrames

```python
df_clean.write.mode("overwrite").parquet("yellow_taxi_2025_clean.parquet")
```

* Saved filtered queries as separate DataFrames for later analysis.

---

## Challenges & Solutions

* **Large Dataset Handling**

  * Initial attempts to write the full dataset caused `OutOfMemoryError`.
  * Resolved by increasing partitions and optimizing Spark configurations.

* **Java Configuration Issues**

  * PySpark requires a compatible Java version. Installed OpenJDK 11 and set `JAVA_HOME`.

* **Null and Anomalous Data**

  * Identified columns with nulls and negative values; cleaned data accordingly.

* **Dynamic Web Content**

  * Some web sections required Selenium to expand elements before scraping.
  * Managed connection and element-not-found errors with retries and waits.

---

## Next Steps / Enhancements

* Perform **geospatial analysis** on pickup/dropoff locations.
* Analyze **tip patterns by time of day or passenger count**.
* Visualize results using **Matplotlib / Seaborn / PySpark DataFrame plots**.

---

## Conclusion

This project demonstrates the ability to:

* Automate **web scraping with Selenium**.
* Handle **large-scale datasets with PySpark**.
* Perform **data cleaning, transformation, and analysis**.
* Configure complex environments for **Java, PySpark, and Python**.

---

**Technologies Used:** Python, PySpark, Selenium, Jupyter Notebook, Parquet, OpenJDK 11, ChromeDriver, PyCharm

---
