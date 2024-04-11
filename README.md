# Retrieve all DOIs from DataCite with a specific prefix 🐄

## API endpoint: https://api.datacite.org/dois
## Parameters: ?prefix=XXXXXXX&page[size]=9999  

## Example usage:
python3 getdoi.py 10.15128  :memo: **Please enter DOI prefix here**

Calling the DataCite API...  
Response from API...  
200  
Found 461 DOIs with prefix=10.15128  


### Notes:  
The script creates one output file **doi** with the correct line endings for your OS.  If you need different line endings, you will need to use a tool such as [dos2unix](https://dos2unix.sourceforge.io/)

