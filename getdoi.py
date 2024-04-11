"""

A wee script that gets all DataCite DOIs with one specific DOI prefix

Requires one parameter on command line:  DOI prefix
Output is one file:  one DOI per line

"""

import requests
DATACITE_API = "https://api.datacite.org/dois"
PAGE_NUMBER = "&page[size]=9999"
data = "data.json"
doi  = "doi"
fh   = open(doi, 'w')

def getdoi(prefix):
    try:
        print('Calling the DataCite API...')
        headers = {"accept": "application/vnd.api+json"}
        full_prefix = "?prefix=" + prefix
        response = requests.get(DATACITE_API+full_prefix+PAGE_NUMBER, headers=headers)
        print('Response from API...')
        print(response.status_code)
#        print(response.text)
        return response, prefix

    except IndexError:
        print()


def printdoi(response, prefix):
    j = response.json()
    json_array = j['data']
    count = 0
    for x in json_array:
        doi = x['id']
        fh.write(doi + '\n')
        count += 1
    print(f"Found {count} DOIs with prefix={prefix}")

def main():
    try:
        r, p = getdoi(sys.argv[1])
        printdoi(r, p)

    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())




