import numpy as np
import cv2
import matplotlib.pyplot as plt

def calculate_horizontal_histogram(image_input):
    height, width = image_input.shape[:2]
    histogram = np.zeros(width, dtype=np.uint32)
    for y in range(height):
        for x in range(width):
            if image_input[y, x] > 0:
                histogram[x] += 1
                
    return histogram

def calculate_vertical_histogram(image_input):
    height, width = image_input.shape[:2]
    histogram = np.zeros(height, dtype=np.uint32)
    for y in range(height):
        for x in range(width):
            if image_input[y, x] > 0:
                histogram[y] += 1
    return histogram

# def draw_figure(canvas, figure):
#     figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#     figure_canvas_agg.draw()
#     figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
#     return figure_canvas_agg

# Load image
image_path = 'images/03.png'
image_input = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.plot(image_input[:3])
plt.show()
