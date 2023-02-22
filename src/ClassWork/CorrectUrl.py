from urllib.parse import urlparse, urlunparse


def right_url(url1, url2):
    parsed_url1 = urlparse(url1)
    if not parsed_url1.scheme and not parsed_url1.netloc:
        url1 = 'https://' + url1
    parsed_url1 = urlparse(url1)
    if parsed_url1.scheme != 'https':
        url1 = 'https' + url1[4:]
    parsed_url1 = urlparse(url1)
    domain_name = parsed_url1.netloc
    if domain_name.startswith('www.'):
        domain_name = domain_name[4:]

    # parse url2 and fill in missing components with url1
    parsed_url2 = urlparse(url2)
    if not parsed_url2.scheme:
        parsed_url2 = parsed_url2._replace(scheme=parsed_url1.scheme)
    if not parsed_url2.netloc:
        parsed_url2 = parsed_url2._replace(netloc=domain_name)

    # construct the full URL
    if parsed_url2.path.startswith('/'):
        path = parsed_url2.path
    else:
        path = '/' + parsed_url2.path
    return urlunparse(
        (parsed_url2.scheme, parsed_url2.netloc, path, parsed_url2.params, parsed_url2.query, parsed_url2.fragment))


# Input URLs
url1 = "www.tekwerks.com/"
url2 = "contact-us"
print(right_url(url1, url2))
