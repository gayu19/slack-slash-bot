import tldextract

def is_root_domain(domain):
    extracted = tldextract.extract(domain)
    if (extracted.subdomain):
        return(f'{domain} : not root domain')
    else:
        return(f'{domain} : root domain')        
