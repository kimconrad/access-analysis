# access-analysis

1. Database stores static data for use during the project
  - Used pgAdmin to create four tables to use in the machine learning: comp_types, income_internet, inc_int_comp, inc_int_no_int
2. Database interfaces with the project in some format
  - Connected Heroku to pgAdmin, to make local database available in the cloud

  ![image](images/heroku_connection.PNG)
3. Includes at least two tables
  - Used pgAdmin and SQL to create tables with the cleaned raw data

  ![image](images/create_starter_tables.PNG)
  - Started with two tables: comp_types and income_internet

  ![image](images/comp_types.PNG)

  ![image](images/income_internet.PNG)
4. Includes at least one join using the database language
  - Used SQL to join tables

  ![image](images/join_tables.PNG)
  - Created inc_int_comp

  ![image](images/inc_int_comp.PNG)
5. Includes at least one connection string
  - Used SQLAlchemy in Jupyter Notebook to connect Heroku to Jupyter Notebook

  ![image](images/sqlalchemy_connection.PNG)
