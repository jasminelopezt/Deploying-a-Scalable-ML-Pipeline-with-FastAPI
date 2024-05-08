# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Name of Developer: Jasmine Lopez Torres
Model Date: 5/7/2024
Model Version:1.0
Model type: Classification

## Intended Use
The model uses training via a machine learning pipeline and FASTAPI. The model encodes categorical features and uses the file "train_model" to evaluate performance metrics on salary. The model selected is Random Forest Classification and will predict if an individual earns under or over 50k per year. 

## Training Data

Data: Census data.
The census data from 1994 contains demographic information on individuals such a occupation, sex, marital status, education, and age. The data was cleaned, and encoded in pre-processing. 80% of the data is reserved for training. 

## Evaluation Data
The evaluation data is the census data as well. 20% of this data was reserved for the evulation portion. 

## Metrics

PRECISION: 0.7419
RECALL: 0.6384
F1: 0.6863

## Ethical Considerations

There are some etical considerations when looking at the data. The data contains sensitiive information regarding individuals, but there is not identifiable information for individuals so there should be no issues with this type of information but the sensitivity of this data should be considered. Bias may be introduced since there may be some individuals that are overrepresented or underrepresented in our data. 

## Caveats and Recommendations

Investigating model bias needs to be kept in mind during the deployment of this ML pipeline. The feature of salary in this dataset may not encompass factors that affect income levels in individuals. Updating the data in the dataset is recommended. Regular evaluation and modification of this model is also recommended. 