1. Problem Definition- You have to write down you  
   * Aim
   * Objectives

2. Basic Domain Knowledge(like Financial, Aviation, Geospatial, Agriculture, Medical etc.)

3. Data Collections:
    * Stackeholder can provide you data
    * Public Sources [Data search Engine](https://datasetsearch.research.google.com/)
    * API(yfinance)
    * Social Media
    * Survey Forms
    * Web Scrapping(bs4, Selenium, [crawl4ai](https://github.com/unclecode/crawl4ai))

4. Data integration(ETL)- Data Lake
Structured, Unstructured, Semistructured  

5. Data Preprocessing and Feature engineering
Different procedure are there for tabular data, images data, audio data
**Tabular Data**
* Checking manually
* Loading data- pandas or pyspark(for large sized data)
* check for spelling errors in column names
* Look for data entry errors such as checking signs
* Checking for missing values, outliers, duplicate values
* Check for data imbalance
* Check for data skewness
* Check for multicollinearity(high correlation between different features)
* Check for cardinality b/w 2 categorical columns.
* Remove irrelevant features(feature selection)

6. Data versioning(using DVC)
7. Feature store(all the features will be stored in feature store for storing, servingm managing ML feautres)- so that we are getting upto date features

7. Dashboarding data(Data visualization)
8. Data splitting(train,test,validate)
9. Choosing appropriate ML/DL algorithms(We can also use Hybrid algorithms - training on different Algorithms and using them as ensemble)

10. Evaluating performance 
11. Hyperparameter tuning(optuna, gridsearch or randomizedsearchcv)

12. Test on validation dataset.
13. MLFlow- model versioning, tracking, plots, parameters performance
14. Model interpretability and Explainability(How reliable our model is?)- Explainable AI engineer
15.  Biasness and fairness checks(use IBM fairness check)
16. Create an API(create API using flask, use postman to test)
17. Select best model and deploy it in production:
* Use cloud platforms(Like AWS, GCP, Azure)
* Wrap it in a web application
* Then deploy it on website(use Deployment strategies)

18. CI/CD 
Every time we are adding features/updating model it should reflect in production use Docker/kubernetes
19. Model Monitoring(you'll get warning)
* Peformance Monitoring
* Data quality monitoring
* Use promethus+grafana
* Model governance
* Security and adversial ML