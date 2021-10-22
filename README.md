# IndeedWebscraping-To-Excel

## Description
Web scraping Python project that extracts four pages of job data from a specified Indeed link and exports it to an excel file titled "internships.xlsx". The job data includes job title, company name, job location, salary, job summary, and the company's Indeed profile link. 

The website link: 
<br>
```htmlText = requests.get("https://www.indeed.com/jobs?q=intern&l=hampton&fromage=1&vjk=d6866bece2cc7d55").text  ``` 
<br>
can be swaped and customized using Indeed to change the parameters of the job search (job title, location, required experience, etc)

The for loop parameters:  ```for i in range(0,40,10)  ```  can be updated to include more Indeed pages to scrape. Page parameters start at 0 and are incremented by 10. 


## Requirements

* Install **Beautiful Soup**, **Pandas**, and **Requests** libraries

* Copy your computer's user agent into this dictionary: ```headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}```
