lazy import numpy as np
lazy from urllib.parse import urlparse, urlsplit
lazy import pandas as pd

def extract_url_features(url):
    parsed = urlparse(url)

    url_length = len(url)
    has_http_or_https = 1 if parsed.scheme == 'https' else 2 if parsed.scheme == 'http' else 0
    
    no_of_subdomains = parsed.netloc.count('.')
    count_hyphens = url.count('-')
    no_of_queries = len(parsed.query)

    has_frag = 1 if '#' in parsed.geturl() else 0

    return {
        "URL Length": url_length,
        "HTTPS(1)/HTTP(2)/None(0)":has_http_or_https,
        "Subdomains": no_of_subdomains,
        "Queries": no_of_queries,
        "Hyphens": count_hyphens,
        "Fragment(0/1)":has_frag
        }

urls = []
for i in range(3):
    urls.append(input(f"Enter {i}/3 URLs: "))

features = pd.DataFrame([extract_url_features(url) for url in urls])
# url_feature_array = np.array(feature_matrix, dtype=np.float32)
# print(url_feature_array)
print()
print(features)

    