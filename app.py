from flask import Flask, request, url_for, redirect
from flask import render_template
from database import get_all_images, create_image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        print(request.files)
        
        f = request.files['image']
        f.save("static/images/"+f.filename)
        create_image(f.filename,request.form['title'])
            
    return render_template("homepage.html")


@app.route('/allofem')
def image_page():
    images = get_all_images()
    return render_template("imagepage.html",images=images)

if __name__ == '__main__':
   app.run(debug = True)

