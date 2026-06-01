# Time Series Forecast Evaluation for Business Analytics Times Series has its own set of tools to measure the accuracy of a
forecast model that are different than traditional methods for...

### Time Series Forecast Evaluation for Business Analytics
Times Series has its own set of tools to measure the accuracy of a forecast model that are different than traditional methods for evaluating the performance of ML models. This post discusses key metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE), and provides Python implementations for evaluating forecast accuracy.


<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Joel Holland</a> on <a class="markup--anchor markup--figure-anchor"


#### Forecast Evaluation Metrics
Assessing the performance and accuracy of time series forecasts is a crucial step in the modeling process. This allows us to understand how well the model is capturing the underlying patterns in the data and to make informed decisions about model selection and refinement.

#### Mean Absolute Error (MAE)
The MAE is the average of the absolute differences between the actual and forecast values. It provides a measure of the average magnitude of the errors, without regard to their direction (like if the error is above or below the actual value). The formula for MAE is:


where y_t is the actual value at time t, ŷ_t is the forecast value at time t, and n is the number of observations.

The MAE is easy to interpret and is less sensitive to outliers than some other metrics. It provides a straightforward measure of the average forecast error.

#### Root Mean Squared Error (RMSE)
The RMSE is the square root of the mean of the squared differences between the actual and forecast values. It is calculated as:


The RMSE is more sensitive to large errors than the MAE, as the squared differences give more weight to larger errors. This can be useful for applications where large errors are particularly undesirable, such as in high-stakes decision-making.

#### Mean Absolute Percentage Error (MAPE)
The MAPE is the average of the absolute percentage differences between the actual and forecast values. The formula is:


The MAPE provides a relative measure of forecast accuracy, expressed as a percentage. This can be helpful for comparing the performance of a model across different time series with varying scales.

However, the MAPE can be problematic when the actual values include zeros or are close to zero, as this can lead to extremely large or undefined percentage errors.

#### Symmetric MAPE (sMAPE)
The symmetric MAPE is a variant of the MAPE that addresses the issue of division by zero. The sMAPE is bounded between 0 and 200%, making it more interpretable than the standard MAPE.

#### Coefficient of Determination (R-squared)
The R-squared statistic measures the proportion of the variance in the actual values that is explained by the forecast values. It ranges from 0 to 1, with higher values indicating better model fit.

R-squared can be useful for comparing the relative performance of different models, but it should be interpreted with caution as it can be influenced by the scale of the data and the number of predictors in the model.

These are some of the most commonly used metrics for evaluating time series forecast accuracy. The choice of metric(s) will depend on the specific requirements of the forecasting task, the characteristics of the data, and the preferences of the analyst or decision-maker.

#### Python Implementation for Evaluation
The \`sklearn.metrics\` module to calculate these forecast evaluation metrics in python.


This will output:


For the MAPE and sMAPE metrics, we can implement them ourselves:


This will output:


#### Reflection Questions
1\. What are the limitations of traditional forecast evaluation metrics?\ \ Traditional forecast evaluation metrics like MAE, RMSE, and MAPE have several limitations:

- Sensitivity to scale: These metrics are sensitive to the scale of the data, making it difficult to compare the performance of models across different time series with varying scales.
- Outlier sensitivity: Metrics like RMSE give disproportionate weight to large errors, which can be heavily influenced by outliers in the data.
- Interpretability: While metrics like MAPE provide a relative measure of accuracy, they can be difficult to interpret, especially when the actual values are close to zero.
- Assumption of symmetric errors: Metrics like MAPE and sMAPE assume that the distribution of errors is symmetric, which may not always be the case in real-world time series data.
- Lack of statistical significance: These metrics do not provide information about the statistical significance of the differences in forecast accuracy between models, making it difficult to determine if observed differences are meaningful.

2\. How can you address the challenges of evaluating time series forecasts in real-world scenarios?\ \ To address the limitations of traditional forecast evaluation metrics in real-world scenarios, you can consider the following approaches:

- Use multiple metrics: Instead of relying on a single metric, you can use a combination of metrics (e.g., MAE, RMSE, and sMAPE) to get a more comprehensive understanding of the forecast accuracy.
- Normalize or scale the metrics: Normalizing the metrics by the scale of the data or the mean of the actual values can help improve the interpretability and comparability of the results.
- Employ robust statistical methods: Techniques like rolling window evaluation, out-of-sample testing, and statistical hypothesis testing can provide more robust and reliable assessments of forecast accuracy, especially in the presence of outliers or structural breaks.
- Incorporate domain-specific knowledge: Consulting subject matter experts and considering the context-specific importance of different types of errors can help in the selection and interpretation of appropriate evaluation metrics.
- Assess economic or business impact: In some cases, it may be more relevant to evaluate the forecasts based on their impact on key business or economic decisions, rather than solely on statistical measures of accuracy.
- Explore alternative evaluation approaches: Newer evaluation methods, such as those based on loss functions or probabilistic forecasting, can provide a more nuanced and comprehensive assessment of forecast performance in real-world scenarios.

These approaches can help you address the limitations of traditional forecast evaluation metrics and ensure that the assessment of time series forecasts aligns with the specific requirements and constraints of your real-world application.


<h1 id="an-error-occurred." class="message">An error occurred.</h1>

Unable to execute JavaScript.

### Related Stories
- [[ARIMA Models and Time Series Forecasting for Business Analytics](https://medium.com/@kylejones_47003/arima-models-and-time-series-forecasting-for-business-analytics-97c5c870e9c6)]
- [[Using Trends in Time Series for Business Analysis](https://medium.com/@kylejones_47003/using-trends-in-time-series-for-business-analysis-0d79f4b93ca9)]
- [[What is a Time Series? An introduction for business analysts](https://medium.com/@kylejones_47003/what-is-a-time-series-an-introduction-for-business-analysts-303e8e1fedd8)]
