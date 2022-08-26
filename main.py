from flask import Flask, render_template, request, redirect , jsonify,url_for
import numpy as np
from scipy.special import comb
import time
import subprocess
import glob


def bernstein_poly(i, n, t):
    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i


def bezier_curve(points):
    nPoints = len(points)
    xPoints = np.array([p[0] for p in points]).astype(float)
    yPoints = np.array([p[1] for p in points]).astype(float)
    t = np.linspace(0.0, 1.0, 1000)
    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)   ])
    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
#
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save("static/images/"+uploaded_file.filename)
        time.sleep(0.5)
        #     from matplotlib import pyplot as plt
        #     img = Image.open("./static/images/"+uploaded_file.filename)

        return render_template('index_2.html',file_name=uploaded_file.filename)

    if request.method == "GET":
        return render_template('index.html')



@app.route('/process', methods=['POST','GET'])
def process():
    if request.method == 'POST':
        points_x = request.form.get('input_list_x')
        points_y = request.form.get('input_list_y')
        # points_x = points_x.split(", ")

        img_name = request.form.get('image_name')
        command = [
            "python",
            "untitled3.py",
            img_name,
            points_x,
            points_y
        ]
        subprocess.call(command)

        return redirect(url_for('process'))
    if request.method == "GET":


        x = {}
        i = 0
        y = glob.glob("static/images/*.*", recursive=True)
        for each in range(0, len(y)):
            x[each] = [y[each].split("\\")[1], False, None]

            if "_processed" in y[each]:
                x[each - 1] = [y[each - 1].split("\\")[1], True, y[each].split("\\")[1]]
                del (x[each])
            i += 1
        return render_template("result.html",data=x)


if __name__ == '__main__':
    app.run(debug=True)
