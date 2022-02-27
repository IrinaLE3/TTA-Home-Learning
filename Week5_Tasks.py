import pandas as pd
destinations = pd.read_csv("Week5_Destinations.csv")

## 1.How many rows and columns are there in your file?

print(destinations.shape)

## 2.Print row 3-8 (using iloc/loc)

print(destinations.iloc[2:8])

## 3.Find the mean number of all-inclusive hotels across all destinations.

print(destinations["All-inclusive hotels"].mean())

## 4.Find the lowest scoring destination.

min_score = destinations["Feedback score"].min()
myfilter = destinations["Feedback score"] == min_score
min_score_destinations = destinations[myfilter]
print(min_score_destinations)

## 5.Find the highest scoring destination. 

max_score = destinations["Feedback score"].max()
myfilter = destinations["Feedback score"] == max_score
max_score_destinations = destinations[myfilter]
print(max_score_destinations)

## 6. Find all the destinations where there are more than 90 all-inclusive hotels.

myfilter = destinations["All-inclusive hotels"] > 90
result = destinations[myfilter]
print(result)

## 7. Filter the data by score above 8.

myfilter = destinations["Feedback score"] > 8
result = destinations[myfilter]
print(result)

##8. Filter the data score below 2.

myfilter = destinations["Feedback score"] < 2
result = destinations[myfilter]
print(result)

