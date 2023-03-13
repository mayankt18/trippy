# Trippy

### Installation instructions
1. Make a python virutal environment
2. Install the required packages using 
```
pip install -r requirements.txt
```
3. Run the required migrations
```
python3 manage.py migrate
```

4. To start the development process you would need two terminals

I. In the first terminal run the tailwind css development server
```
python3 manage.py tailwind start
```

II. In the second terminal run the python development server
```
python3 manage.py runserver
```

5. To get tailwind styling in any page include the following tags in the head of the html document
```html
{% load static tailwind_tags %}
<head>
...
{% tailwind_css %}
...
</head>
```