# access-analysis

## Question

Are there discernable patterns connecting Internet Access, Income, and Population Density?
- Selected Topic
  - US and Puerto Rico Internet Access per Household
    - Broadband/Dial-up/No Access
  - Ratio of Income to Poverty Level
  - Urban vs. Rural (based off population)
- Reason why they selected their Topic and questions we hope to answer with the data
  - Internet access is a necessity today and can have detrimental effects in different facets of life. We wanted to see what patterns may exist between access, or lack therof, to internet and other factors such as income and population density.
- Description of the source Data
  - US Census data
  - Collected from American Community Survey

## Data
- Presence of a Computer and Type of Internet Subscription in Household
- Ratio of Income to Poverty Level of Families in the Past 12 Months
- Total Population

## Technologies Used
### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Jupyter Notebook and Python.

### Database Storage
PgAdmin is the database we intend to use, and we will integrate Flask to display the data.

### Machine Learning
Jupyter Notebook is the ML library we'll be using to create a classifier. Our training and testing setup is to test the correlation between variables. Visulize the difference of Ratio of Income to Poverty Level of Families in the Past 12 Months and Presence of a Computer and Type of Internet Subscription in Household,and the difference of  Total Population of a certain acrea and Presence of a Computer and Type of Internet Subscription in Household. 

Extra ML verbiage here.

### Dashboard
In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. It will be hosted on Tableau.

## Model
- Logistic Regression
- Unsupervised Learning

## Communication Protocols
- Plan out weekly tasks and timelines during in class Zoom meeting
- Use Slack messages for additional questions during the week
