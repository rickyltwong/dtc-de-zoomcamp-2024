-- Q1
CREATE MATERIALIZED VIEW trip_time_stat AS
with cte as (select (tpep_dropoff_datetime - tpep_pickup_datetime) as duration,
                    pulocationid,
                    dolocationid
             from trip_data),
     cte2 as (select c.pulocationid, c.dolocationid, max(c.duration), min(c.duration), avg(c.duration)
              from cte c
              group by c.pulocationid, c.dolocationid)
select c2.pulocationid, tz1.Zone as pickup_zone, c2.dolocationid, tz2.Zone as dropoff_zone, c2.avg, c2.max, c2.min
from cte2 c2
         join taxi_zone tz1 on c2.pulocationid = tz1.location_id
         join taxi_zone tz2 on c2.dolocationid = tz2.location_id;

select *
from trip_time_stat
order by avg desc;


-- Q2
select count(*)
from trip_data
where pulocationid = (select pulocationid from trip_time_stat order by avg desc limit 1)
  and dolocationid = (select dolocationid from trip_time_stat order by avg desc limit 1);


-- Q3

create materialized view top_3_busiest_zones as
WITH latest_time_t AS (SELECT MAX(tpep_pickup_datetime) AS latest_time
                       FROM trip_data),
     time_range AS (SELECT (latest_time - INTERVAL '17 HOUR') AS start_time,
                           latest_time
                    FROM latest_time_t),
    top_3_business_id as (
SELECT t.pulocationid,
       COUNT(*) AS cnt
FROM trip_data t
WHERE t.tpep_pickup_datetime > (select start_time from time_range limit 1) AND t.tpep_pickup_datetime < (select latest_time from time_range limit 1)
GROUP BY t.pulocationid
ORDER BY cnt DESC
limit 3)
select tz.Zone, t.cnt
    from top_3_business_id t join taxi_zone tz on t.pulocationid = tz.location_id;

select * from top_3_busiest_zones order by cnt desc;

drop materialized view  top_3_busiest_zones;
