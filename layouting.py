import PySimpleGUI as sg

sg.theme("DefaultNoMoreNagging")
file_list_column = [
    [sg.Text("Open Image Folder :")],
    [sg.In(size=(20, 1), enable_events=True, key="folder_images"),
     sg.FolderBrowse()],
    [sg.Text("Choose an images from list : ")],
    [sg.Listbox(values=[], size=(15, 10),
                key="list_image", enable_events=True)],

    [sg.Text("Image Information : ")],
    [sg.Text(size=(18, 1),
             key="image_size")],
    [sg.Text(size=(18, 1),
             key="image_color_depth")],
]

input_image_preview = [
    [sg.Text("Image Input :")],
    [sg.Text(size=(20, 1), key="image_path")],
    [sg.Image(key="preview_input_image")],
]

list_processing = [
    [sg.Text("Main Feature : ")],
    [sg.Button("Image Thresholding", size=(14, 1), key="image_thresholding")],
    [sg.Button("Image Negative", size=(14, 1), key="image_negative")],
    [sg.Button("Image Brightness", size=(14, 1), key="image_brigtness")],
    [sg.Button("Equalization Greyscale", size=(16, 1), key="equalization_greyscale")],
    [sg.Button("Equalization Color", size=(16, 1), key="equalizer_greyscale")],




  
    [
        # TEXT LABEL
        sg.Text("Image Thresholding : ",
                key="text_thresholding", visible=False),
        sg.Text("Image Brightness : ", key="text_brightness", visible=False),

      

        # Input
       

        # Slider
        sg.Slider(range=(0, 255), size=(9, 20),
                  orientation='h',
                  key="slider_thresholding",
                  default_value=0, visible=False),
        sg.Slider(range=(0, 255), size=(9, 20),
                  orientation='h',
                  key="slider_brightness",
                  default_value=0, visible=False),
      

        # Button
       
        sg.Button("Apply", size=(9, 1),
                  key="submit_thresholding", visible=False),
        sg.Button("Apply", size=(9, 1),
                  key="submit_brightness", visible=False),
       
    ],
    [sg.Button("Reset", size=(14, 1), key="cancel", visible=False)]
]

output_image_preview = [
    [sg.Text("Image Output:")],
    [sg.Text(size=(20, 1), key="type_processing")],
    [sg.Image(key="preview_output_image")],
]

output_histogram_preview = [
    [sg.Text("Histogram Output:")],
    [sg.Text(size=(20, 1), key="type_processing")],
    [sg.Image(key="preview_output_histogram")],
]


layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(input_image_preview),
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(output_image_preview),
        sg.VSeperator(),
        sg.Column(output_histogram_preview),

    ]
]

window = sg.Window("Mini Image Editor", layout)
filename_out = "output.png"
