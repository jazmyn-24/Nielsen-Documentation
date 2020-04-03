# Nielsen-Documentation
Pre-requisites:
1. Python 3.5+
2. Python IDE
3. Mongochef Core 4.4 +

Libraries/Modules/Packages/Dependencies To be Installed/Used:
1. Pandas
2. Numpy
3. Pymongo
4. datetime
5. xlsxwriter
6. tld
7. json
8. MongoClient
9. re
10. unicodedata
11. time
12. http.client
13. urllib.parse


Flow of Code:

1. Raw Nielsen File is formatted in two parts: 
   a. GTC Countries
   b. Local Countries ( Non - GTC)
2. For GTC Countries: 
   In GTC_Formatting.py, raw file of 22 countries is formatted under the function gtc_common(). The formatting is done as per the instruction file. The formatted output is stored in a single sheet for all 22 countries in gtc-output.xlsx file.
   
   For China, UK, Mexico: Each country has seperate raw file which is formatted separately as column names and format maybe different from one another. 
                          Each country has it's own function: gtc_china(), gtc_uk(), gtc_mexico(). The formatted output for each country is stored in seperate sheets in gtc-output.xlsx file.
   
   
   For India: Raw Data for India comes in 6 different excel files. The files - Energy India, Juice India & SSD India have same format and are concatenated in one dataframe and formatted. Same steps are followed for files - RTD Tea, Sports & Water.
              Formatted Data is stored in a single sheet - "India" in gtc-output.xlsx file.
   
   For Kazakhstan: Raw Data for kazakhstan has different format and is processed in two files: 
                   a. re-index_kazakh: The index of the file is reset and new files are stored based on the month. 
                   b. Kazakhstan.py: In this file the columns and rows are interchanged using pivot method.
                   The output is then further formatted in GTC_Formatting.py under gtc_kazakhstan() function.
                   The formatted output is stored in a separate single sheet - "Kazakhstan" in gtc-output.xlsx file.


3. For Local Countries:
For Argentina, Chile, Peru, Bolivia: The data for these countries comes in a single file. The formatting for each country is different and needs to be done separately. After formatting, all 4 countries are concatenated in single dataframe under function acpb().
The formatted output for all 4 is stored in a single sheet - "ACPB" on output-local.xlsx file

For Brazil: Raw Data for Brazil is stored in single file and is formatted under the function brazil(). Formatted output is stored in sheet - "Brazil" on output-local.xlsx file.

For South Africa: Raw Data for South Africa comes in 6 different files, all of which are concatenated in a dataframe and formatted. Formatted output is stored in sheet - "South Africa" on output-local.csv file.

For Turkey: Raw Data for Turkey comes in 3 different files and each sheet in those files has different format and is formatted seperately. After formatting, all data is concatenated and stored in sheet - "Turkey" on output-local.xlsx file.

For USA: Raw Data comes in one file and is formatted according to instruction file and formatted output is stored in sheet - "USA" on output-local.xlsx file.

For South Korea: Same procedure as USA and Brazil.

4. Patch & Import: 
A patch is applied to both gtc-output.xlsx and output-local.xlsx files. The output is stored in a csv file which is imported to collection - 
NielsenData.

5. Cleaning:
In clean_nielsen.py, formatted output imported to NielsenData is checked wrt the following collections: 
a. Established Brands (Check for Brand & Manufacturer)
b. Brand Source ( Check for Brand & Country)
c. Brands ( Check for Brands)
New Brands are then inserted in clean_nielsen collection.

6. BingSearch:
In BingSearchNielsen.py, documents are imported from clean_nielsen.py and a search query is run for each brand, the returned URL results are stored in bing_search_nielsen collection.

7. BingSummary:
In BingSummaryNielsen.py The Results stored in bing_search_nielsen for each brand are aggregated and stored in collection - aidle_data. 






                   
