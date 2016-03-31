#example script of creating tables
CREATE EXTERNAL TABLE uk_english_1grams (
 gram string,
 year int,
 occurrences bigint,
 pages bigint,
 books bigint
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS SEQUENCEFILE
LOCATION 's3://datasets.elasticmapreduce/ngrams/books/20090715/eng-gb-all/1gram/';

#example script of cleaning string data and write to new table
INSERT OVERWRITE TABLE uk_normalized_1gram
SELECT
 lower(gram),
 year,
 occurrences
FROM
 uk_english_1grams
WHERE
 gram REGEXP "^[A-Za-z+'-]+$"; 


CREATE TABLE uk_normalized_1gram (
 gram string,
 year int,
 occurrences bigint
);

INSERT OVERWRITE TABLE normalized_2gram
SELECT
 lower(gram),
 year,
 occurrences
FROM
 english_2grams
WHERE
 gram REGEXP "^[A-Za-z+'-]+\ [A-Za-z+'-]+$";


#filtering data into new tables
create TABLE regularity row format delimited fields terminated by ',' 
STORED as textfile
location 's3://msba6330-google-ngram/output/' AS
select * from normalized_1gram where gram in ("chid","chided","strived","strove","found","finded","got","geted","dwelt","dwelled","drived",
"drove","snuck","sneaked","stick","stucked","come","came");


#compare the occurrences of words by decades
create TABLE decade_data_wordnet row format delimited fields terminated by ',' 
STORED as textfile
location 's3://msba6330-google-ngram/output/' AS
SELECT
 a.gram,
 b.decade,
 sum(a.occurrences)
FROM
 normalized_2gram a
JOIN ( 
 SELECT 
  substr(year, 0, 3) as decade, 
  sum(occurrences) as total
 FROM 
  normalized_2gram
 GROUP BY 
  substr(year, 0, 3)
) b
ON
 substr(a.year, 0, 3) = b.decade
where gram like "data %" or gram like "% data"
or gram like "information %" or gram like "% informatino" or gram like "info %" or gram like "% info"
or gram like "entropy %" or gram like "% entropy" or gram like "randomness %" or gram like "% randomness"
or gram like "haphazard %" or gram like "% haphazard" or gram like "statistics %" or gram like "% statistics"
GROUP BY
 a.gram,
 b.decade;
