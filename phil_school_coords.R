library(tidyverse)
library(readit)
library(ggmap)

# import the file
df <- readit('DepEDSchools with Missing GPS Data - Sheet1.csv')
# create a new column that contains the school name and address
df <- df %>% mutate(address = paste(school_name, municipality, province, sep = ', '))
# do some cleaning: 
# NHS -> National High School
# ES -> Elementary School
# HS -> High School
df$address <- str_replace(df$address, 'NHS', 'National High School')
df$address <- str_replace(df$address, 'ES', 'Elementary School')
df$address <- str_replace(df$address, ' HS', ' High School')

# Put df$address into the object place
place <- df$address

# Get the geo coordinates, limited to 2500 queries (rows) per day
codes <- geocode(place[1:2500])

names(df)
names(codes)

# replace the NA's with the matches in codes
df[1:2500,'latitude'] <- codes[,'lat']
df[1:2500,'longitude'] <- codes[,'lon']
df %>% select(latitude, longitude)

# write csv to file noLongLat.csv
write_csv(df, 'noLongLat.csv')

# get all rows with the remaining missing longitude and latitude
df2 <- df %>% filter(is.na(latitude))
# write csv to file updatedNoLongLat.csv
write_csv(df2, 'updatedNoLongLat.csv')

# Make sure to check the matches for impossible and wrong values (e.g. negative long and lat values)