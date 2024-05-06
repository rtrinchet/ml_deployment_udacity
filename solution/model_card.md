# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The selected model is a Logistic Regression classification model that predicts if a individual has salary above 50k$.

## Intended Use
This model is intended for educational purposes, as part of the Udacity Course for MLOPS.

## Data
Based on Census dataset, retrieved from here: https://archive.ics.uci.edu/dataset/20/census+income
### Training & Evaluation Data
We opted for a random split, having 80% of the data used as training and the remainder 20% used as evaluation

## Metrics
The metrics used are precision, recall and fbeta.
The results in this metrics were:
- Precision: 0.725
- Recall: 0.254
- Fbeta: 0.377

## Ethical Considerations

**Data Bias**: The census dataset may contain 
biases inherent in census data collection processes. These biases could stem from underrepresentation or misrepresentation of certain demographic groups due to factors such as non-response bias, sampling bias, or historical inequalities in census participation.

**Fairness in Predictions**: The model should be evaluated for fairness to ensure that its predictions do not disproportionately benefit or harm specific demographic groups. Fairness metrics, such as disparate impact analysis or fairness-aware evaluation, should be used to assess and mitigate potential biases in model predictions.
## Caveats and Recommendations

This is a very simple model, used for educational purposes. Please be aware of this when interpreting results.
