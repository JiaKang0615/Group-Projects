# Group & Personal Projects
These are some of the projects I worked in group during the MSBA program and some personal projects I finished earlier.

### 1. Exploratory Analysis on Hillary Clinton's Email
  The data set hosted by Keggle includes Hillary Clinton's released email contents and contacts. The exploration consists of three parts: a) Topic modeling and how topics trending overtime b)How sentiment of emails change on weekdays c)Frequent contacts of Hillary Clinton and network analysis.
  
  * As a result of [topic modeling](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary_LDA_Topic.py) using LDA, 7 topics were identified, and their trend overtime is plotted here.
  ![alt text](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary%20topic%20trending.PNG "Topic Trending")

  * To do sentiment analysis, [IBM's Waston API](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary_email_API.py) was called. It turns out that on Monday, emails tend to be more negative than positive whereas on Friday, positive emails increase.

  *  I detected the [most frequent contacts](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Hillary_Sender_Receiver.R) Hillary emailed with, and visualized the interactions with this chord gram.
   ![alt text](https://github.com/JiaKang0615/Group-Projects/blob/master/Hillary%20Clinton%20email/Chord%20gram_fin.jpg "Chord gram of Hillary and contacts' interaction")
