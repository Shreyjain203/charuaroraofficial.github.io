from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

index = pd.read_excel("static/data/data.xlsx",
                      sheet_name='index')

collection_list = pd.read_excel("static/data/data.xlsx",
                                sheet_name='collection_list')
collections = list(collection_list['Content'].values)
    
# need a repository for all the images

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

# Collections pages
@app.route('/collections')
def collections():
    return render_template('collections.html',
                           collections=collections)

@app.route('/collections/<collection_type>')
def collection_type(collection_type):
    if collection_type not in collections:
        return "404 not found"
    product_df = pd.read_excel("static/data/data.xlsx",
                               sheet_name=collection_type)  # [['names','price']]

    return render_template('only_one_category_all_data.html',
                           data=product_df.values.tolist())

@app.route('/collections/<collection_type>/<product>')
def collection_type(collection_type, product):
    if collection_type not in collections:
        return "404 not found"

    product_df = pd.read_excel("static/data/data.xlsx",
                               sheet_name=collection_type)
    products = list(product_df['names'].values)

    if product not in products:
        return "404 not found"

    data_df = product_df[product_df['names']==product].head(1)
    return render_template('only_one_category_all_data.html',
                           collection_type=collection_type,
                           data=data_df.values.tolist())

# Celebrity Influencers page
@app.route('/celebrity_influencers')
def celebrity_influencers():
    return render_template('celebrity_influencers.html')

# Contact us Page
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

# __name__ code
if __name__ == '__main__':
    app.run(debug=True)


################################ Rough work ################################

# <!DOCTYPE html>
# <html>
# <head>
#     <title>Dynamic Content</title>
# </head>
# <body>
#     <h1>{{ heading }}</h1>
#     <img src="{{ url_for('static', filename='assets/' + lehengas_type + '/example.jpg') }}" alt="Example Image">
#     <a href="{{ url_for('content', content_type='about') }}">About</a>
#     <a href="{{ url_for('content', content_type='contact') }}">Contact</a>
# </body>
# </html>


# {% for item in items %}
# <article>
#     <header>
#         <!-- <span class="date">April 22, 2017</span> -->
#         <h2><a href="#">{{ item.title }}</a></h2>
#     </header>
#     <a href="#" class="image fit"><img src="{{ url_for('static', filename='images/' + item.image) }}" alt="" /></a>
#     <!-- <p>{{ item.description }}</p> -->
#     <ul class="actions special">
#         <li><a href="{{ item.whatsapp_link }}" class="button">shop on whatsapp</a></li>
#     </ul>
# </article>
# {% endfor %}