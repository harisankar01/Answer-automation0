# automation0

<h3>A new project on web bots with selenium</h3>
<h4>The goal of this project is to automate answering multiple choice question answering by scraping answers from other site</h4>
<h2> Requirmnets</h2>
  <h3> Have pip installed in your local machine and install the following packages by <code>pip install <package_name> </code> command</h3>
  
 The packages required are:
  
  - [Selenium for Web Automation](https://pypi.org/project/selenium/)
  - [Beautiful Soup for Web Scraping](https://pypi.org/project/BeautifulSoup/)
  - [Request for making Web Requests](https://pypi.org/project/requests/)
  
  <h4> We need latest version of Chrome Web Driver for Web automation and It can be found here</h4> 
  External Downloads:
  
  - [Web driver](https://chromedriver.chromium.org/downloads)

  Explaination to the code
  |Context |Explaination|
| --- | --- | 
| Scrape() upto line 39 | This function scrapes the solutions for multiple choice answers | 
| Scrape() other lines | Automating the job of finding correct option and clicking the multiple choice button | 
| Difficulty | Many websites use a random string for options which are not constant for all assignments(lines 77,87...) | 
| Remarks | The example site I have tested has many dropdowns which require different syntax (lines 60..) |
  
  ```mermaid
  flowchart LR
      A[Scrape the required website] --> B[Load the Web Driver]   
      B --> C[Automate for login and finding multiplechoice options]
      C --> D{answer is options}
      D -- Yes --> E(Click option)
      D --> |No| F(Dont Click)
  ```
  
  > This is a project to learn about bots and selnium and best use cases are for educational purposes
  
