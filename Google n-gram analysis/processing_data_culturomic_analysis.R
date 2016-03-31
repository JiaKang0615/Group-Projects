usdata<-read.csv("C:/Users/Kang/OneDrive/UMN/6330 big data/group/us_t.csv")
ukdata<-read.csv("C:/Users/Kang/OneDrive/UMN/6330 big data/group/uk_t.csv")

#processing usdata
usdata<-aggregate(usdata$occurancy,by=list(usdata$gram,usdata$year),sum)
colnames(usdata)<-c("gram","year","occurancy")
usdata<-arrange(usdata,usdata$gram)

us_ed<-usdata[grep(".*ed",usdata$gram),]
us_t<-usdata[grep(".*t",usdata$gram),]

us_ed$root<-substr(as.character(us_ed$gram),1,3)
us_t$root<-substr(as.character(us_t$gram),1,3)

us_all<-merge(x=us_t, y=us_ed, by=c("root","year"),all.x=T)
us_all_1800<-us_all[us_all$year>=1800,]
us_all_1800$occurancy.y[is.na(us_all_1800$occurancy.y)]<-0
us_all_1800$ratio<-us_all_1800$occurancy.y/us_all_1800$occurancy.x

us_ratio<-us_all_1800[,c(1,2,7)]
write.table(us_ratio,file="us_ratio")

#processing ukdata
ukdata<-aggregate(ukdata$occurancy,by=list(ukdata$gram,ukdata$year),sum)
colnames(ukdata)<-c("gram","year","occurancy")
ukdata<-arrange(ukdata,ukdata$gram)

uk_ed<-ukdata[grep(".*ed",ukdata$gram),]
uk_t<-ukdata[grep(".*t",ukdata$gram),]

uk_ed$root<-substr(as.character(uk_ed$gram),1,3)
uk_t$root<-substr(as.character(uk_t$gram),1,3)

uk_all<-merge(x=uk_t, y=uk_ed, by=c("root","year"))
uk_all_1800<-uk_all[uk_all$year>=1800,]
uk_all_1800$occurancy.y[is.na(uk_all_1800$occurancy.y)]<-0
uk_all_1800$ratio<-uk_all_1800$occurancy.y/uk_all_1800$occurancy.x

uk_ratio<-uk_all_1800[,c(1,2,7)]
write.table(uk_ratio,file="uk_ratio")

#year mean ratio by country
uk_yearmed<-aggregate(uk_ratio$ratio,by=list(uk_ratio$year),mean)
us_yearmed<-aggregate(us_ratio$ratio,by=list(us_ratio$year),mean)
yearmean<-merge(x=uk_yearmed, y=us_yearmed, by="Group.1")
colnames(yearmean)<-c("year","uk","us")
write.table(yearmean,file="yearmean.csv")
