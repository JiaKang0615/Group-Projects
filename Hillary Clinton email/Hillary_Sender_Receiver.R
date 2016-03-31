install.packages('RSQLite')
install.packages('circlize')
library(RSQLite)
library(circlize)
library(dplyr)
library(ggplot2)

# You can read in the SQLite datbase like this
db <- dbConnect(dbDriver("SQLite"), "C:/Users/Kang/OneDrive/UMN/6410 exploratory/group/output/database.sqlite")
freq_sender <- dbGetQuery(db, "
                     SELECT e.SenderPersonId Senderid,
                     p.Name Sendername, count(e.SenderPersonId) SenderNum
                     FROM Emails e
                     INNER JOIN Persons p ON e.SenderPersonId=p.Id
                    group by e.SenderPersonId
                    order by SenderNum DESC")

freq_receiver <- dbGetQuery(db, "
select r.PersonId, p.Name Receivername, count(r.PersonId) ReceiverNum
from EmailReceivers r
inner join Persons p on r.PersonId=p.Id
group by r.PersonId
order by ReceiverNum DESC")

To_from_id <- dbGetQuery(db, "
select e. SenderPersonId senderid, r.personid receiverid, count(*) Num
from Emails e 
inner join EmailReceivers r on e.id=r.EmailId
group by senderid,receiverid
order by Num DESC")

print (To_from_id)

#join the name to TO_From_id
persons <- read.csv("C:/Users/Kang/OneDrive/UMN/6410 exploratory/group/output/Persons.csv")

colnames(To_from_id)[1]<-"Id"#change the column name so that it matches the persons table
a1<-merge(x=To_from_id,y=persons,by="Id", all.x = TRUE)#left join
a1<-a1[order(-a1$Num),]
colnames(a1)[1]<-"senderid"#change back the name

colnames(a1)[2]<-"Id"
a1<-merge(x=a1,y=persons,by="Id", all.x = TRUE)
a1<-a1[order(-a1$Num),]

#create the table with sender name, receiver name and frequency
To_from <- data.frame(a1$Name.x,a1$Name.y,a1$Num)
colnames(To_from)<-c("SenderName","ReceiverName","Frequency")

#clean data
To_from$SenderName[To_from$SenderName=="valmorou@state.gov" | To_from$SenderName=="valmorou@state.gov."]<-"Lona Valmoro" 
To_from$ReceiverName[To_from$ReceiverName=="valmorou@state.gov" | To_from$SenderName=="valmorou@state.gov."]<-"Lona Valmoro"
To_from$SenderName[To_from$SenderName=="millscd@state.gov."]<-"Cheryl Mills"
To_from$ReceiverName[To_from$ReceiverName=="millscd@state.gov."]<-"Cheryl Mills"
To_from$SenderName[To_from$SenderName=="sullivanjj@state.gov."]<-"Jake Sullivan"
To_from$ReceiverName[To_from$ReceiverName=="sullivanjj@state.gov."]<-"Jake Sullivan" 
To_from$SenderName[To_from$SenderName=="jilotylc@state.gov."]<-"Lauren Jiloty"
To_from$ReceiverName[To_from$ReceiverName=="jilotylc@state.gov."]<-"Lauren Jiloty"
To_from$SenderName[To_from$SenderName=="sullivanij@state.gov"]<-"Jake Sullivan"
To_from$ReceiverName[To_from$ReceiverName=="sullivanij@state.gov"]<-"Jake Sullivan"
To_from$SenderName[To_from$SenderName=="abedinh@state.gov."]<-"Huma Abedin"
To_from$ReceiverName[To_from$ReceiverName=="abedinh@state.gov."]<-"Huma Abedin"
To_from$SenderName[To_from$SenderName=="cheryl.mills millscd@state.gov"]<-"Cheryl Mills"
To_from$ReceiverName[To_from$ReceiverName=="cheryl.mills millscd@state.gov"]<-"Cheryl Mills"

To_from$Frequency<-as.numeric(as.character(To_from$Frequency))
To_from$SenderName<-as.character(To_from$SenderName)
To_from$ReceiverName<-as.character(To_from$ReceiverName)

To_from<-aggregate(To_from$Frequency,To_from[,1:2],sum,na.rm=TRUE)
colnames(To_from)<-c("SenderName","ReceiverName","Frequency")
To_from<-arrange(To_from,desc(Frequency))

#create the chord giagram
freq_contact<-To_from[1:20,]
colnames(freq_contact)<-c("from","to","value")
chordDiagram (freq_contact, annotationTrack = "grid",preAllocateTracks = list(track.height = 0.3))

# now, the image with rotated labels
chordDiagram(freq_contact, annotationTrack = "grid", preAllocateTracks = 1, grid.col = grid.col)
circos.trackPlotRegion(track.index = 1, panel.fun = function(x, y) {
  xlim = get.cell.meta.data("xlim")
  ylim = get.cell.meta.data("ylim")
  sector.name = get.cell.meta.data("sector.index")
  circos.text(mean(xlim), ylim[1], sector.name, facing = "clockwise",
              niceFacing = TRUE, adj = c(0, 0.5))
}, bg.border = NA)

#freq sender
sender=To_from[To_from$ReceiverName == "Hillary Clinton",]
freq_sendertoH<-sender[1:10,]


#freq receiver from H
receiver=To_from[To_from$SenderName == "Hillary Clinton",]
freq_receiverfromH<-receiver[1:10,]