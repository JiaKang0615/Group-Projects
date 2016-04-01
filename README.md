# Group & Personal Projects
These are some of the projects I worked in group during the MSBA program and some personal projects I finished earlier.

### 1. Exploratory Analysis on Hillary Clinton's Email
  The data set hosted by Keggle includes Hillary Clinton's released email contents and contacts. The exploration consists of three parts: a)Topic modeling and how topics trending overtime b)How sentiment of emails change on weekdays c)Frequent contacts of Hillary Clinton and network analysis.
  
  * As a result of [topic modeling](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary_LDA_Topic.py) using LDA, 7 topics were identified, and their trend overtime is plotted here.
  
  <img src="https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary%20topic%20trending.PNG" width="500">

  * To do sentiment analysis, [IBM's Waston API](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary_email_API.py) was called. It turns out that on Monday, emails tend to be more negative than positive whereas on Friday, positive emails increase.

  * I detected the [most frequent contacts](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary_Sender_Receiver.R) Hillary emailed with, and visualized the interactions with this chord gram.
  
   <img src="https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Chord%20gram_fin.jpg" width="380">

### 2. SEO strategy for AirFrance
  Using the data from AirFrance Case Study, the goal of this project was to optimize the bidding strategy on Search Engine. I built OLS models for each keyword on each advertisement platform to predict a reasonable rank as target position. The KPIs used to measure advertisement and bidding strategy effect include **Click Through Rate, Conversion Rate, Net Revenue and ROA**.

  * Tools used: Excel, JMP

### 3. Analysis of English Words Using Google N-Gram data
  Following the method in the research paper [*Quantitative Analysis of Culture Using Millions of Digitized Books*](http://www.librarian.net/wp-content/uploads/science-googlelabs.pdf), I extracted [Google n-gram data](https://github.com/JiaKang0615/Group-Projects/blob/master/Google%20n-gram%20analysis/Hive%20code%20for%20culturomic%20analysis.sql) on AWS public S3 bucket using Hive, to analyze the [linguistic change of English words](https://github.com/JiaKang0615/Group-Projects/blob/master/Google%20n-gram%20analysis/processing_data_culturomic_analysis.R). I came to the same conclusion as the research paper, that the process of English verb past tense regularity is ongoing. 

### 4. Using D3.js to Build a Data Visualization Page
  I built a [data visualization page](https://github.com/JiaKang0615/Group-Projects/blob/master/Chinese%20Tourism%20Industry.html) to show intuitivelly how the Chinese Tourism Industry developed over years (the contents is in Chinese). The charts were written using D3.js package while the main frame of the page was in HTML5 and CSS.

  <img src="https://github.com/JiaKang0615/Group-Projects/blob/master/D3js-chart.PNG" width="350">

### 5. Design Entity–Relationship Model for ESPN Cricket
  Using open source data, I concolidated 11 highly normalized data files into a data warehouse with star schema. After designing the ER Model, I created tables and their relationship, then performed data ETL task to load the data from source files to SQL Server. 

  <img src="https://github.com/JiaKang0615/Group-Projects/blob/master/Design%20ER%20Model.png" width="850">

### 6. Analysis of Unemployment Rate and Campus Crime Rate
  The project statistically evaluates the likelihood impact of unemployment rate on the campus crime rates. It adopted a probabilistic method and built hypothesis testings to measure the effect of unemployment rate of the community on campus crime rate. [The analysis](https://github.com/JiaKang0615/Group-Projects/blob/master/Unemployment%20vs.%20campus%20crime%20rate.py) was done using Python.