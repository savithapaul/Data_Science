*Big Data Deduplication using Siamese Neural Networks & DBSCAN*
Project Overview
Data deduplication is a critical task in big data systems where redundant or duplicate records reduce data quality, increase storage costs, and impact downstream analytics.

This project presents a hybrid deep learning and clustering approach for large-scale data deduplication using:

Siamese Neural Networks (SNNs) for learning record similarity

DBSCAN clustering for grouping similar records into duplicate clusters

The solution was developed as part of my MSc in Data Science and achieved a Distinction (90%+).

 Problem Statement
Large datasets (e.g., customer records, healthcare data, e-commerce transactions) often contain:

Slight spelling variations

Missing attributes

Formatting inconsistencies

Near-duplicate entries

Traditional rule-based matching fails when:

Data is noisy

Duplicates are non-exact matches

The dataset is large and high-dimensional

This project aims to:

Learn semantic similarity between records

Identify near-duplicates automatically

Scale to big data environments

 Methodology
1. Data Preprocessing
Data cleaning and normalization

Feature engineering

Text vectorization / numerical encoding

Pair generation for similarity learning

2️ Siamese Neural Network
Twin neural networks with shared weights

Learns similarity between record pairs

Contrastive loss function used for training

Outputs similarity score between 0 and 1

3️ Clustering with DBSCAN
Density-based clustering

Groups records based on similarity distance

Automatically detects outliers

No need to predefine number of clusters
