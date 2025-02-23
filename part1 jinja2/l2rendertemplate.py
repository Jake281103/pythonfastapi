from jinja2 import Template

template = Template("Hello {{name}}")
output = template.render(name="Hnin Mya")
print(output)   # Hello, Hnin Mya


# => Loops

template = Template("""
    Shopping List:
    {% for item in items %}
        {{item}}
    {% endfor %}

""")
output = template.render(items=["Mike","Redbull","Sponsor","Bread"])
print(output.strip())


template = Template("""
    <ul>
        {% for item in items %}
            <li>{{item}}</li>
        {% endfor %}
    </ul>

""")
output = template.render(items=["Red","Green","Blue"])
print(output.strip())


# => upper

template = Template("Uppercase = {{name | upper}}")
output = template.render(name="nyi nyi")
print(output)  # Uppercase = NYI NYI


# => lower

template = Template("Lowercase = {{name | lower}}")
output = template.render(name="MIN MIN")
print(output)  # Lowercase = min min



# => join()

template = Template("Colors = {{colors | join(', ')}}")
output = template.render(colors=["Red","Green","Blue"])
print(output)  # Colors = Red, Green, Blue




template = Template("""

Original Name = {{name}}
Uppercase     = {{name | upper}}
Lowercase     = {{name | lower}}
                    
Hobbies list  = {{hobbies}}
Joined  = {{hobbies | join(', ')}}
                    
String Number = {{age}}
Converted to Integer = {{age | int}}

""")



datas = {
    "name":"Htoo Htoo",
    "hobbies":["travelling","reading",'sport'],
    "age":"25"
}

output = template.render(datas)
print(output)



# => if/else statement

template = Template("""
    {% if age > 18 %}
        Welcome to our site.
    {% else %}
        Try again late.
    {% endif %}
""")
output = template.render(age=20)
print(output)  # Welcome to our site.


template = Template("""
    {% if score >= 90 %}
        Excellent
    {% elif score >= 75 %}
        Good
    {% elif score >= 60 %}
        Statifactory
    {% else %}
        Need to improvement
    {% endif %}
""")
output = template.render(score=95)
print(output)  # Welcome to our site.

# 22RD
