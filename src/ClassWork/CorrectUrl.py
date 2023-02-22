from urllib.parse import urlparse, urlunparse

# Input URLs
url1 = "http://tekwerks.com/"
url2 = "https://tekwerks.com/contact-us"


def right_url(url1, url2):
    parsed_url1 = urlparse('http://' + url1)

    if parsed_url1.netloc[:4] != 'www.':
        parsed_url1 = parsed_url1._replace(netloc='www.' + parsed_url1.netloc)

    parsed_url2 = urlparse(url2)
    if not parsed_url2.scheme:
        parsed_url2 = parsed_url2._replace(scheme=parsed_url1.scheme)
    if not parsed_url2.netloc:
        parsed_url2 = parsed_url2._replace(netloc=parsed_url1.netloc)

    final_url = urlunparse(parsed_url2)

    return final_url


print(right_url(url1, url2))
