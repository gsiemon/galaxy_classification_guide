# Galaxy Classification for Next-Generation Astronomical Surveys

## Data Science Capstone Project

### Project Overview

This capstone project addresses one of the most pressing challenges in modern astronomy: developing scalable galaxy classification systems for next-generation astronomical surveys. Traditional galaxy classification methods relied on visual inspection and Principal Component Analysis (PCA), approaches that are fundamentally incompatible with the unprecedented data volumes of current and future surveys.

### The Big Data Challenge

Modern astronomical surveys are generating data at an extraordinary scale that dwarfs all previous efforts:

- **DESI (Dark Energy Spectroscopic Instrument)** recently observed over 131,000 galaxies in a single night, equivalent to the entire 6dF Galaxy Survey that took 10 years to complete
- **LSST (Legacy Survey of Space and Time)** and **4MOST Hemisphere Survey** will generate similar data volumes nightly
- Combined, these surveys will observe more galaxies per night than all previous surveys combined over decades

This exponential increase in data volume makes traditional classification approaches obsolete and demands innovative machine learning solutions.

### Project Objectives

**Primary Goal:** Develop the most accurate and efficient galaxy classification system using multi-modal astronomical data to handle the scale of modern surveys.

**Secondary Goal:** Provide comprehensive training in industry-relevant data science techniques through real-world application on multi-hundred-million-dollar scientific experiments.

### Technical Approach

#### Data Sources

- **Photometric Data:** Galaxy images
- **Spectroscopic Data:** Galaxy spectra
- **Tabulated Data:** Pre-processed measurements and derived parameters

#### Methodology

We will implement and compare multiple machine learning paradigms:

**Supervised vs. Unsupervised Learning:**
- Supervised models using labelled galaxy classifications
- Unsupervised clustering and dimensionality reduction techniques
- Semi-supervised approaches for leveraging limited labelled data

**Model Architectures:**
- **Tree-based Models:** Random Forests, Gradient Boosting, XGBoost
- **Deep Learning Models:** Convolutional Neural Networks (CNNs) for images, Recurrent Neural Networks (RNNs) for spectra, Multi-layer Perceptrons (MLPs) for tabulated data
- **Manifold Learning:** Advanced dimensionality reduction techniques

#### Technical Stack

- **Data Management:** SQL for querying large astronomical databases
- **Core Analysis:** Python, Pandas, NumPy, Scikit-learn
- **Deep Learning:** PyTorch/TensorFlow for neural network implementation
- **Specialised Techniques:** Manifold learning algorithms for high-dimensional data exploration

### Industry Applications & Transferable Skills

This project provides direct preparation for industry challenges through analogous data types:

#### Computer Vision Applications

- Galaxy image classification → MNIST digit recognition, ImageNet object classification
- Morphological analysis → Medical imaging, satellite imagery analysis

#### Time Series & Signal Processing

- Spectroscopic data analysis → Electroencephalography (EEG) classification for harmful brain activity detection
- Signal pattern recognition → Audio processing, sensor data analysis

#### Structured Data Analysis

- Tabulated astronomical parameters → Financial fraud detection in credit card transactions
- Multi-dimensional feature analysis → Customer segmentation, risk assessment

### Learning Outcomes

Upon completion, students will have:

- Hands-on experience with real scientific data from cutting-edge astronomical surveys
- Proficiency in the complete machine learning pipeline from data extraction to model deployment
- Expertise in both traditional ML and deep learning approaches
- Understanding of scalability challenges in big data applications
- Portfolio of techniques directly applicable to high-value industry problems

### Impact

This project bridges the gap between academic research and industry application, using astronomical big data as a training ground for developing the analytical skills essential in today's data-driven economy. Students will contribute to solving genuine scientific challenges while building expertise that directly translates to roles in technology, finance, healthcare, and other data-intensive industries.