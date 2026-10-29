lazy from urllib.parse import urlparse, parse_qs
lazy import pandas as pd
lazy import tldextract
lazy import re
lazy import ipaddress

lazy import requests
lazy import socket 
lazy import ssl

class PassiveAnalysis:
    def __init__(self):
        pass
    @staticmethod
    def check_host_type(host):
        try:
            ipaddress.ip_address(host)
            return "IP"
        except ValueError:
            return "Domain"
    @staticmethod    
    def get_port(url):
        url_w = url.strip("https:")
        DefaultPorts = dict.fromkeys(["http", "ws"],80) | dict.fromkeys(["https", "wss"],443) | dict.fromkeys(["ftp"],21)
        if ":" in url_w:
            return url_w.split(":")[-1].split("/")[0]
        else:
            parsed = urlparse(str(url))
            return DefaultPorts.get(parsed.scheme, "Unknown")
    @staticmethod
    def getShorteningService(url):
        knownServices = ['bit.ly', 'tinyurl.com', 'short.gy', 'dub.sh', 'cutt.ly', 't.ly', 'b.link']
        for service in knownServices:
            if service in url:
                return service
        return 'none'

class ActiveAnalysis(PassiveAnalysis):

    def __init__(self):
        pass 

    @staticmethod
    def SSLstate(url):
        tld = tldextract.extract(url)
        hostname = tld.fqdn
        if hostname:
            context = ssl.create_default_context()
            try:
                net_port = PassiveAnalysis.get_port(url)
                print(f"Creating socket connection to {url}...")
                with socket.create_connection((hostname,int(net_port) if net_port != "Unknown" else 80), timeout=1) as sock:
                        print("Success")
                        with context.wrap_socket(sock, server_hostname=hostname) as ssock: 
                            return "Verified"
            
            except ssl.SSLCertVerificationError:
                return "Self Signed" 
            
            except Exception:
                return "Failed"

        return "Failed"



def extract_url_features(url: str):
    parsed = urlparse(url)
    tld = tldextract.extract(url)

    hosttype = PassiveAnalysis.check_host_type(tld.domain)
    scheme = "Unknown" if not parsed.scheme else parsed.scheme
    port = PassiveAnalysis.get_port(url)
    SSLVerification = ActiveAnalysis.SSLstate(url)
    url_length = len(url)
    Subdomains = tld.subdomain.count('.')
    paths = parsed.path.count("/")
    Quries = len(parse_qs(parsed.query))
    fragment = '#' in url
    have_At_symbol = "@" in url
    double_slash = "//" in url
    shortening_service = PassiveAnalysis.getShorteningService(url)
    DomainhyphenCount = tld.domain.count('-')
    TotalHyphenCount = url.count('-')

    return pd.Series({
        "hosttype":hosttype, "scheme":scheme,
        "port":port, "url_length":url_length,
        "SSL Verification": SSLVerification,
        "Subdomains":Subdomains, "paths":paths,
        "Queries":Quries, "fragments":fragment,
        "Have At symbol": have_At_symbol,
        "Double Slash Redirection": double_slash,
        "Shortening Service": shortening_service,
        "Number of Hyphens in Domain":DomainhyphenCount,
        "Total Hyphen Count": TotalHyphenCount
    })
