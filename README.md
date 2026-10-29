### Malicious URL Detection Classification Model
***A Classification Model trained on Kaggle's Malicious URL Dataset***

I created this Machine Learning Model to detect whether a URL is malicious or not using a Random Forest Classification Method (for now).
The project is made for practicing Machine Learning concepts on a beginner level. 
All code is written by human hands and AI has no contribution in writing the code, but has been used to learn a few things along the way.

Right now it is implemented using scikit-learn's RandomForestClassifier, by passing various (13 for now) URL features to the model.
The dataset is Malicious URLs dataset by Manu Siddhartha, uploaded 5 years ago. 
The dataset offers a URL and a class label telling if the URL type is benign, defacement, phishing or malware with most of them being phishing sites.

The [URL Feature Extraction](DatasetCleaning/urlfeatures.py) extracts 13(for now) features of the URL (both categorical, like scheme, port, Shortening service and numerical like Number of paths, subdomains, and etc ) and returns a labelled panda Series.
The [Encoding](DatasetCleaning/encoding.py) is done using OneHotEncoding by scikit-learn's preprocessing module for categorical values and StandardScalar for numerical values, returning both the encoded Training examples and Testing examples.
