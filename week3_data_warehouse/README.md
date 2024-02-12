CREATE OR REPLACE EXTERNAL TABLE nyc_taxi_data.external_green_cab_data (
  vendorID INT64,
  lpep_pickup_datetime DATETIME,
  lpep_dropoff_datetime DATETIME,
  store_and_fwd_flag STRING,
  ratecodeID FLOAT64,
  PULocationID INT64,
  DOLocationID INT64,
  passenger_count FLOAT64,
  trip_distance FLOAT64,
  fare_amount FLOAT64,
  extra FLOAT64,
  mta_tax FLOAT64,
  tip_amount FLOAT64,
  tolls_amount FLOAT64,
  ehailFee FLOAT64,
  improvement_surcharge FLOAT64,
  total_amount FLOAT64,
  payment_type FLOAT64,
  trip_type FLOAT64,
  congestion_surcharge FLOAT64,
)
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-ricky-wong/green_cab_2022/*.parquet']
);


CREATE OR REPLACE TABLE nyc_taxi_data.green_cab_data (
  vendorID INT64,
  lpep_pickup_datetime DATETIME,
  lpep_dropoff_datetime DATETIME,
  store_and_fwd_flag STRING,
  ratecodeID FLOAT64,
  PULocationID INT64,
  DOLocationID INT64,
  passenger_count FLOAT64,
  trip_distance FLOAT64,
  fare_amount FLOAT64,
  extra FLOAT64,
  mta_tax FLOAT64,
  tip_amount FLOAT64,
  tolls_amount FLOAT64,
  ehailFee FLOAT64,
  improvement_surcharge FLOAT64,
  total_amount FLOAT64,
  payment_type FLOAT64,
  trip_type FLOAT64,
  congestion_surcharge FLOAT64,
);

LOAD DATA OVERWRITE nyc_taxi_data.green_cab_data
FROM FILES (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-ricky-wong/green_cab_2022/*.parquet']
);

SELECT COUNT(*) FROM `nyc_taxi_data.external_green_cab_data`;


SELECT COUNT(DISTINCT PULocationID) from nyc_taxi_data.green_cab_data;

SELECT COUNT(DISTINCT PULocationID) from nyc_taxi_data.external_green_cab_data;


SELECT COUNT(1) FROM `nyc_taxi_data.external_green_cab_data` WHERE fare_amount = 0;


SELECT DISTINCT PULocationID FROM nyc_taxi_data.green_cab_data WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30'; -- 12.82MB


CREATE TABLE nyc_taxi_data.green_cab_data_partitioned
PARTITION BY DATETIME_TRUNC(lpep_pickup_datetime, MONTH)
AS
SELECT * FROM nyc_taxi_data.green_cab_data;

SELECT DISTINCT PULocationID FROM nyc_taxi_data.green_cab_data_partitioned WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';
