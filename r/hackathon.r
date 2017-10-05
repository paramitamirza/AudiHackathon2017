data <- read.csv("ZP_6B_Export_Ano.csv")

# Load the libraries languageR, stringr, dplyr and tidyr.
library(languageR)
library(stringr)
library(dplyr)
library(tidyr)

# how many rows, how many columns does that data have?
nrow(data)
ncol(data)
# take a look at the structure of the data frame using "glimpse"
glimpse(data)
# view the first 20 rows, view the last 20 rows
head(data,n=20)
tail(data, n=20)

# Is there any missing data in any of the columns?
sum(is.na(data))

#group by car id
grouped_data_by_carid <- data %>% group_by(data$KNR)
nrow(grouped_data_by_carid)
ncol(grouped_data_by_carid)
# take a look at the structure of the data frame using "glimpse"
glimpse(grouped_data_by_carid)