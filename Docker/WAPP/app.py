from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
    "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg",
   "https://picjumbo.com/wp-content/uploads/hero-image-autumn-leaves-on-flat-blue-background-2-free-photo-1080x720.jpg",
    "https://thumbs.dreamstime.com/b/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg",
   "https://st2.depositphotos.com/1000438/7457/i/450/depositphotos_74578561-stock-photo-young-girl-in-paris-on.jpg",
    "https://static.toiimg.com/thumb/msid-81926277,width-1070,height-580,imgsize-60116,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg",
   "https://i.ytimg.com/vi/ZBEUrj-dOLU/mqdefault.jpg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
