from flask import Flask, render_template
import pandas as pd
import os
app = Flask(__name__)

index_data = pd.read_excel("static/data/data.xlsx",
                      sheet_name='index_page')

collection_list = pd.read_excel("static/data/data.xlsx",
                                sheet_name='collection_list')
collections_ = list(collection_list['Content'].values)
    
# need a repository for all the images

@app.route('/')
def homepage():
    return render_template('index.html', data=index_data.values.tolist())

@app.route('/index')
def index():
    return render_template('index.html',data=index_data.values.tolist())

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

# Collections pages
@app.route('/collections')
def collections():
    return render_template('collections.html',
                           collections=collections_)

@app.route('/collections/<collection_type_>')
def collection_type(collection_type_):
    if collection_type_ not in collections_:
        return "404 not found"
    
    product_df = pd.read_excel("static/data/data.xlsx",
                               sheet_name=collection_type_)  # [['outfit names','price']]
    
    # return str(product_df)
    # return product_df.values.tolist()
    return render_template('only_one_category_all_data.html',
                           data=product_df.values.tolist())

@app.route('/collections/<collection_type_>/<product>')
def product_type(collection_type_, product):
    if collection_type_ not in collections_:
        return collection_type_+product+"404 not found"

    product_df = pd.read_excel("static/data/data.xlsx",
                               sheet_name=collection_type_)
    products = list(product_df['outfit names'].values)

    if product not in products:
        return "404 not found"

    data_df = product_df[product_df['outfit names']==product].head(1)
    return render_template('about_one_particular_category.html',
                           collection_type=collection_type_,
                           data=data_df.values.tolist()[0])

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
