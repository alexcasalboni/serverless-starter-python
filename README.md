#Serverless Starter

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

A bare bones Serverless Framework project with examples for common use cases in Python.

##Install

Make sure you have the [Serverless Framework](http://www.serverless.com) installed and you're using Node.js v4.0+. 
```
npm install serverless -g
```

Install the project using Serverless:
```
serverless project install serverless-starter-python
```

Install project dependencies via npm:
```
npm install
```

Install Python dependencies via pip:
```
pip install -t restApi/vendored/ -r restApi/requirements.txt
```

or via virtualenv:
```
virtualenv myenv
source myenv/bin/activate
pip install -r restApi/requirements.txt
cp -R myenv/lib/python2.7/site-packages/* restApi/vendored/
```



Deploy your functions and endpoints:
```
serverless dash deploy
```

##Includes

This project contains the following:

* **Multi:** Multiple functions each containing a single endpoint
* **Single:** A single function that uses multiple endpoints.
* **Continent:** A real-world example with Python requirements and response mapping.
* **Templates:** Templates are used to reduce configuraton syntax
* **REST API Parameters:** The Multi/Show function endpoint gives an example of how to accept a path parameter
