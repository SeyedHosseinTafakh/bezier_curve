# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:20:54 2022

@author: hossein
"""
import numpy as np
from scipy.special import comb
from PIL import Image
import sys

image_name = sys.argv[1]
points_x = sys.argv[2].split(',')
points_y = sys.argv[3].split(',')

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


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    img = Image.open("./static/images/"+image_name)

    # points_x = [549,463,308,161]
    # points_y = [18,90,89,138]
    for each in range(0,len(points_x)):
        points_x[each] = int(points_x[each])
        # points_x[each] = int(each)

    for each in range(0,len(points_y)):
        points_y[each] = int(points_y[each])
    points = list(zip(points_x,points_y))
    # print(points)
    # print("printing points in main:" + points)
    xpoints = [p[0] for p in points]
    ypoints = [p[1] for p in points]
    xvals, yvals = bezier_curve(points)
    xpoints = []
    ypoints = []
    for each in points:
        xpoints.append(float(each[0]))
        ypoints.append(float(each[1]))
    fig,ax = plt.subplots()
    ax.imshow(img)
    plt.plot(xvals, yvals)
    plt.plot(xpoints, ypoints, "ro:")
    for nr in range(len(points)):
        plt.text(points[nr][0], points[nr][1], nr)

    img_name = image_name.split(".")
    img_name = img_name[0]+"_processed."+img_name[1]
    plt.savefig("./static/images/"+img_name)
    # plt.savefig('books_readxx.png')

    
    