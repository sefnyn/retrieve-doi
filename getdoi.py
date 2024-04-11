"""

A wee script that gets all DataCite DOIs with one specific DOI prefix

Requires one parameter on command line:  DOI prefix
Output is one file:  one DOI per line

"""

import requests
DATACITE_API = "https://api.datacite.org/dois?prefix="
PAGE_NUMBER = "&page[size]=9999"
data = "data.json"
doi  = "doi"
fh   = open(doi, 'w')

def getdoi(prefix):
    try:
        print('Calling the DataCite API...')
        headers = {"accept": "application/vnd.api+json"}
        response = requests.get(DATACITE_API+prefix+PAGE_NUMBER, headers=headers)
        print('Response from API...')
        print(response.status_code)
#        print(response.text)
        return response

    except IndexError:
        print()


def printdoi(response):
    j = response.json()
    json_array = j['data']
    print('json_array')
#    print(json_array)
    for x in json_array:
        doi = x['id']
        fh.write(doi + '\n')

def main():
    try:
        r = getdoi(sys.argv[1])
        printdoi(r)

    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())




