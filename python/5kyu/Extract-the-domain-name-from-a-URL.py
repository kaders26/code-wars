# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# my solution

def domain_name(url):
    if "://" in url:
        url = url.split("://",1)[1]
    if "www." in url:
        url = url.split("www.",1)[1]
    if "." in url:
        url = url.split(".",1)[0]
    return url