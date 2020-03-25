# Heat Map
Python package which can be used to generate and overlay a heat map on the given image.

# Reqruirements

- Python 3.7 (recomended, otherwise any version 3.x should work)
* OpenCV
    ```
    $ pip install opencv-python
    ```
- Numpy
    ```
    $ pip install numpy
    ```

# Usage
- **original_image**: Original image on which to overlay heatmap
- **heat_map_2d_array**: 2d numpy array with intensity values
- **kernel_size**: Size of the area in which heat of the specific location will be spread with Gaussian Kernel
- **opacity**: Opacity specifies the opacity level of the heat map
- **cmap**: Cmap is the color distribution for the heatmap. Any value from these can be used: https://docs.opencv.org/master/d3/d50/group__imgproc__colormap.html
- **save_path**: Path of the directory where to save generated heatmap

# Example

An example python code is available in example directory. To execute this code change directory to example and run following command:
    ```
    $ python example.py
    ```.

Then a resulting image named **heatmap.jpg** will be created in the same directory. 

<img width=20% src='https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/heatmap.jpg'>

Reference image (interior-top-view.jpg) in the samples folder used in this example is taken from freepik.com provided by MarySan2000. Link to the image is: https://www.freepik.com/premium-vector/apartment-design-with-furniture-top-view-architectural-plan-kitchen-bathroom-bedroom-living-room_7283209.htm

# Samples

### Using different Sigma Values

<img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Sigma_5_heatmap.jpg" > | <img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Sigma_25_heatmap.jpg"> | <img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Sigma_55_heatmap.jpg"> |<img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Sigma_85_heatmap.jpg"> 
:---:|:---:|:---:|:---:
Sigma=5 | Sigma=25 | Sigma=55 | Sigma=85

### Using different Alpha Values

<img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Opacity_0.1_heatmap.jpg" > | <img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Opacity_0.3_heatmap.jpg"> | <img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Opacity_0.5_heatmap.jpg"> |<img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Opacity_0.7_heatmap.jpg"> |<img width=90% src="https://github.com/Bilal-Yousaf/heatmap/blob/master/samples/Opacity_0.9_heatmap.jpg"> 
:---:|:---:|:---:|:---:|:---:
Opacity=0.1 | Opacity=0.3 | Opacity=0.5 | Opacity=0.7 | Opacity=0.9


