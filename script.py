#!/usr/bin/env python
# -- coding: utf-8 --

import os
from extractor_module import Extractor
import pdb

""" To get a list of bag files with camera images in the current directory """
bag_file = []
for file in os.listdir("."):
    if file.endswith(".bag"):
        print(os.path.join("/mydir", file))
	bag_file.append(os.path.join(file))

#image_topic = "/camera/image_color"
#image_topic = "/camera/image_raw"
image_topic = "/darknet_ros/detection_image"


extract_obj = Extractor(bag_file,image_topic)
extract_obj.extract()
del extract_obj






