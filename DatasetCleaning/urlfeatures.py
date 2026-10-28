lazy from urllib.parse import urlparse, parse_qs
lazy import pandas as pd
lazy import tldextract
lazy import re
lazy import ipaddress

def check_host_type(host):
    try:
        ipaddress.ip_address(host)
        return "IP"
    except ValueError:
        return "Domain"
    
def get_port(url):
    url_w = url.strip("https:")
    DefaultPorts = dict.fromkeys(["http", "ws"],80) | dict.fromkeys(["https", "wss"],443) | dict.fromkeys(["ftp"],21)
    if ":" in url_w:
        return url_w.split(":")[-1].split("/")[0]
    else:
        parsed = urlparse(str(url))
        return DefaultPorts.get(parsed.scheme, "Unknown")

def getShorteningService(url):
    knownServices = ['bit.ly', 'tinyurl.com', 'short.gy', 'dub.sh', 'cutt.ly', 't.ly', 'b.link']
    for service in knownServices:
        if service in url:
            return service
    return 'none'


def extract_url_features(url: str):
    parsed = urlparse(url)
    tld = tldextract.extract(url)

    hosttype = check_host_type(tld.domain)
    scheme = "Unknown" if not parsed.scheme else parsed.scheme
    port = get_port(url)
    url_length = len(url)
    Subdomains = tld.subdomain.count('.')
    paths = parsed.path.count("/")
    Quries = len(parse_qs(parsed.query))
    fragment = '#' in url
    have_At_symbol = "@" in url
    double_slash = "//" in url
    shortening_service = getShorteningService(url)
    hyphenCount = tld.domain.count('-')

    return pd.Series({
        "hosttype":hosttype, "scheme":scheme,
        "port":port, "url_length":url_length,
        "Subdomains":Subdomains, "paths":paths,
        "Quries":Quries, "fragments":fragment,
        "Have At symbol": have_At_symbol,
        "Double Slash Redirection": double_slash,
        "Shortening Service": shortening_service,
        "Number of Hyphens":hyphenCount
    })




