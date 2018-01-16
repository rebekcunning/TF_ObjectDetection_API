# This repo was forked from TensorFlow Object Detection API Tutorial found here https://github.com/wagonhelm/TF_ObjectDetection_API: 


## Required Packages
* [TensorFlow v1.3](http://www.tensorflow.org/)
* [Jupyter](http://jupyter.org/)
* [NumPy](http://www.numpy.org/)
* [Scipy](https://www.scipy.org/)
* [Matplotlib](http://matplotlib.org/)
* [Scikit-Image](http://scikit-image.org/)
* [Pandas](http://pandas.pydata.org/)
* [lxml](http://lxml.de/)
* [protobuf](https://github.com/google/protobuf)

See my blog post to learn about what I did: http://www.bekcunning.com/blog/car-back
    
### FILES

1. ApproachingCars.ipynb
Contains the steps required to run the car detector and construct a video from the results.

2. json_to_csv.py and xml_to_csv.py
Contain code to convert the image attribute files to csv which will be used to generate tfrecords

3. split_labels.ipynb
Creates test and training data from our complete set of images

4. generate_tfrecord.py
python code required to generate tfrecords used during training of the model

5. data/
this folder contains the moodel config and file for labelling the desired classes.
