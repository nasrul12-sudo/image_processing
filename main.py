from layouting import *
from histogram import *
import os.path
from PIL import Image
from processing_list import *

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "folder_images":
        folder = values["folder_images"]

        try:
            list_file = os.listdir(folder)
        except:
            list_file = []

        file_name = [
            f
            for f in list_file
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["list_image"].update(file_name)

    if event == "list_image":
        try:
            filename = os.path.join(values["folder_images"], values["list_image"][0])
            window["image_path"].update(filename)
            window["preview_input_image"].update(filename)
            window["type_processing"].update(filename)
            window["preview_output_image"].update(filename)

            input_image = Image.open(filename)
            image_width, image_height = input_image.size
            window["image_size"].update(
                "Image Size : " + str(image_width) + " x " + str(image_height)
            )

            mode_to_coldepth = {
                "1": 1,
                "L": 8,
                "P": 8,
                "RGB": 24,
                "RGBA": 32,
                "CMYK": 32,
                "YCbCr": 24,
                "LAB": 24,
                "HSV": 24,
                "I": 32,
                "F": 32,
            }
            color_depth = mode_to_coldepth[input_image.mode]
            window["image_color_depth"].update("Color Depth : " + str(color_depth))
        except:
            pass

    elif event == " ":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Thresholding")
            # Thresholding
            window["text_thresholding"].update(visible=True)
            window["slider_thresholding"].update(visible=True)
            window["submit_thresholding"].update(visible=True)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)

        except:
            pass

    elif event == "image_negative":
        try:
            window["cancel"].update(visible=True)
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)

            window["type_processing"].update("Image Negative")
            output_image = negative(input_image, color_depth)
            histogram = calculate_horizontal_histogram(image_input)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
            window['preview_output_histogram'].update('hallo')
        except:
            pass

    elif event == "image_brigtness":
        try:
            window["cancel"].update(visible=True)
            window["type_processing"].update("Image Brigtness")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=True)
            window["slider_brightness"].update(visible=True)
            window["submit_brightness"].update(visible=True)
        except:
            pass

    elif event == "equalization_greyscale":
        try:

            window["type_processing"].update("Equalization Greyscale")
           
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_thresholding":
        try:
            value = int(values["slider_thresholding"])
            output_image = thresholding(input_image, color_depth, value)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "submit_brightness":
        try:
            value = int(values["slider_brightness"])
            window["type_processing"].update("Image Brightness")
            output_image = brightness(input_image, color_depth, value)
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)
        except:
            pass

    elif event == "cancel":
        try:
            output_image = input_image
            output_image.save(filename_out)
            window["preview_output_image"].update(filename=filename_out)

            window["cancel"].update(visible=False)
            window["type_processing"].update("")
            # Thresholding
            window["text_thresholding"].update(visible=False)
            window["slider_thresholding"].update(visible=False)
            window["submit_thresholding"].update(visible=False)
            # Brigthness
            window["text_brightness"].update(visible=False)
            window["slider_brightness"].update(visible=False)
            window["submit_brightness"].update(visible=False)

        except:
            pass
