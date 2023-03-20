# ASIN-extraction
"Extracting the ASINs of different products present on the given webpage"
### The final output of the assesment consists of a python code which:

1) Finds the number of ASINs in the given webpage

2) Finds all the ASINs in the webpage

3) Implements multiprocessing to speed up the process of finding al the ASINs

## Scrape Product Details from Product Page

 1) Add the required urls to a final names "urls.txt"
 
 2) Run  "asins.py"
 
 3) Get the output data in the file "output1.txt"

## Usage

## Input Data

The input is a text file which consists of all the webpage links given in the excel sheet.
Snapshot of the txt file: 
    ![image.png](attachment:image.png)
## Procedure

1) Open the "urls.txt" file in read mode.

    2) Go through each of the links one by one.

    3) For each link complete the following steps:

        1) Go through the enire webpage and scrape out all the amazon product links available in it.
    
        2) Store these links in a "output.txt" file.
    
        3) For each amazon link in the "output.txt" file find the ASIN number.
    
        4) Open a new "output1.txt" file in append format and append all the ASINs found in each page to this txt document.
    
    4) This process takes a long time if each webpage is searched one after the other. Hence lets implement multiprocessing.

    5) For implementing multiprocessing "n" number of threads are taken and ecah thread is assigned to one link in the "urls.txt" file. That is, the threads run parallelly for each of the links and get the ASINs for the products present in the webpage.

### Snapshot of example webpage:

![image.png](attachment:image.png)

    1) we can observe from the above screenshot that the website consists of amazon products with their respective links. 
     
    2) Hence, we need to scrape out these amazon links of the products to get the ASINs of the products. 
    
    3) For the process of scraping we will use the "BeautifulSoup" library.
    
### Snapshot of "Output.txt":

![Screenshot%202023-03-19%20at%2016.36.45.png](attachment:Screenshot%202023-03-19%20at%2016.36.45.png)

 The output.txt consists of all the amazon product links present in the website.
