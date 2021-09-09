
      
      
# News-Application
   News-App
      - provides news from around the world. The applicatioin have different sections such as Headlines Page,
      Tech News Page, Region Section where users can find news based on region. 
  
  LogIn/SignUp 
     - In order to access the News-Application services, users are require to register and authenticate themselves. 
      
  Region Section News 
    - Provides different country news, each country have 6 different section where users can find news based 
    on thier intrest such as Genral, Entertainment, Sicence, Health & Sport. 
      
  Search bar 
    - News App also have Search bar, where users can search any article of their choice. 
    
    Heroku Server
     - News-Application is deployed on Heroku Server 
  Heroku Link 
   - https://capstone-news-application.herokuapp.com/



# TO use/run News App
    - Create a Project Folder in your Computer 
       CLONE News App GITHUT REPOSITORY TO YOUR Project Folder 
    - Create a virtul environment 
          python3 -m venv venv
    - Activate the virtul environment in your computer 
          source venv/bin/activate
    - INSTALL ALL THE DEPENDECIES from requirements.txt
         pip3 install -r requirements.txt
    - run server in development mode 
          FLASK_ENV=development flask run 
 
    
 # Walk Through
    - To access the Web-App services users need to register themselves, and every time user want to access
    the website he/she needs to authenticate themselves with the required cridentials. In the Search bar users
    can type any refference to the article of their choice and they will be provided with the articles regarding 
    their pass in input from different sources. users can access the Headlines, Tech News and Region News after 
    register/authenticate themselves. 
      

# Links to the APIs used for this Project. 
   News API
    - https://newsapi.org/
  Intro 
    - News API provides news from different sources such as BBC news, CNN, FOX news etc. News API allow 100 requests 
    per day for free accounts where developers can build applications for Projects, the website also provides paid 
    services where the requests to the webiste are vary as per package. 
    
# Technology stack used for News-app Project 
  Techologies stact used for this application are, 
  Front-End 
    HTML, CSS, JAVASCRIPT, BOOTSTRAP 
  Server 
    Python, Flask, WTForms
  Database 
    SQL, SQLALCHAMY
    
 # Requirments Installations to run News-App Project 
    requirments.txt
        - all the required packages are listed in the requirements.txt file. 
    To install packages from requirements.txt 
        - run pip install -r requirements.txt
      
      
      
      
      
      
