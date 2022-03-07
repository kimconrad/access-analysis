# access-analysis

## Question

Are there discernable patterns connecting Internet Access, Income, and Population Density?
- Selected Topic
  - US and Puerto Rico Internet Access per Household for 2018 by county
  - income/internet access
  - Income/presense of computing device
  - Urban vs. Rural (based off population)
- Reason why they selected their Topic and questions we hope to answer with the data
  - Internet access is a necessity today and can have detrimental effects in different facets of life. We wanted to see what patterns may exist between access, or lack therof, to internet and other factors such as income and population density.
- Description of the source Data
  - US Census data
  - Collected from American Community Survey

## Data
- [Presence of a Computer and Type of Internet Subscription in Household](https://data.census.gov/cedsci/table?q=internet%20access&g=0100000US%240500000&y=2018&d=ACS%201-Year%20Estimates%20Detailed%20Tables&tid=ACSDT1Y2018.B28003)
- [Ratio of Income to Poverty Level of Families in the Past 12 Months](https://data.census.gov/cedsci/table?q=income%20level&g=0100000US%240500000&y=2018&d=ACS%201-Year%20Estimates%20Detailed%20Tables)
- [Mean Income in the Past 12 Months (in 2018 Inflation-Adjusted Dollars)](https://data.census.gov/cedsci/table?q=average%20income&g=0100000US%240500000&y=2018&tid=ACSST1Y2018.S1902)
- [Oregon - Rural Definitions: State-Level Maps](https://www.ers.usda.gov/webdocs/DataFiles/53180/25592_OR.pdf?v=0) (Rural definition based on Office of Management and Budget metro counties)


## Technologies Used
### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Jupyter Notebook, python and Rstudio.

### Database Storage
Heroku is the database we intend to use, and we use Tableau to visualize our datasets.

### Machine Learning
- Jupyter Notebook is the ML library we'll be using to create a classifier. Our modeling setup is to viualize the correlation between variables. Differences between various incomes (under 10K to over 75k) using presence of a Computing device (desktop/laptop/smartphone/tablet/other) and internet supscription or no internet subsciption.
- Data preprocessing was done with cleaning the csv files downloaded from the Census buereau website. I used both Pandas and eyes-on scrolling in Excel to clean the data.  There were a few rows with null/other values creating float and object variables that were easier to just eliminate (two in total). This brought my data to fully Integer.  Also, the model did not care for 0 values, it popped an error with less than 2, so there were two values, that were zero that I changed to 2.
- Feature selection was based on the data that we have. I have spent a good bit of time learning that there is no way to correlate data with an unequal amount of variables, so that was somewhat limiting in feature selection I will discuss this further later on.
- The data was split into training and testing sets and errored out.  For logistic regression, the outcome seems to be binary, when I attempted to use ".(income)without internet access" as my y, it threw a value error and said "ValueError: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2." The lowest value was 18.
- I ended up using unsupervised learning, which was quite happy with the data and performed as expected. However, this data does not seem to allow confusion matrix and accuracy analysis like LR.  Therefore I will use PCA and covariance.

### Dashboard
In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. It will be hosted on Tableau.

## Model
- Unsupervised Learning- with K means - scatter and 3D plot analysis

## Communication Protocols
- Plan out weekly tasks and timelines during in class Zoom meeting
- Use Slack messages for additional questions during the week
- Use Issues feature in Git Hub to address "issues"
