<h1 align = "center"> Web Based Writing Application </h1>

_Main Contributors: Sior, Jim Becker, Christine Johnson
<br>This directory contains code for a web-based writing application. The application is being created as a web based application used to detect student misconceptions of electrical circuit concepts in a short answer question using NLP. The directory contains a `style` folder for css files, a `scripts` folder for javascript functionality, and an `image` folder containing a svg image file. Current plans to implement more functionality using Django/Flask and NLP library._

# Table of Contents
1. [Technologies Used](#Technologies)
2. [Running the Project](#Running)
3. [Unit Tests](#Testing)
4. [Citations](#Citations)

## Technologies used <a name="Technologies"></a>
<li>Python 3.10.0
<li>Web App library: Flask/Django
<li>HTML, CSS, and JavaScript are used to control presentation, formatting, and layout 
  
## How to Run the Project <a name="Running"></a>
After downloading source code from the github page, which will download as "Investment-App-main", open the folder within a running Python environment. To start the StockSmart Flask website, run the following three commands: (1) `export FLASK_APP=stockApp`, (2) `export FLASK_ENV=development`, and (3) `flask run`. Then click the resulting website link, or manually enter `http://127.0.0.1:5000/`, to see the website in action.

## Unit Testing the Flask Application <a name="Testing"></a>
We used the python built-in framework `unittest`, to write the unit tests for our Python flask application. The unit tests are contained in the file `test.py`.

## Citations