# image-to-desmos

Image-To-Desmos processes a standard color image and plots the outline onto the popular calculator app, Desmos. 

## Process
OpenCV was used to convert the image into a plottable format, through the following process as pictured below. 

![](image_processing.png)

The result of retrieving the minimum viable points necessary to construct an image and plotting it onto the Desmos API is the following. 

![](/Users/emily/Desktop/Screen Shot 2019-01-13 at 4.24.40 AM.png)

## Usage
Run `server.py` in a shell, then open `home.html` and upload an image. Please note that it is a slow process and it may take a considerable amount of time to finish. 

To only test the algorithm, open `image_line.py` and uncomment line 119. 

`/tests` contains images that were used in testing while creating this application, with the `leaf-identification.jpg` and `goat.jpg` most successful. 