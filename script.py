#!/usr/bin/env python
# -- coding: utf-8 --

import os
from extractor_module import Extractor
import pdb

bag_file = []
for file in os.listdir("."):
    if file.endswith(".bag"):
        print(os.path.join("/mydir", file))
	bag_file.append(os.path.join(file))

output_dir = "."
image_topic = "/camera/image_color"


extract_obj = Extractor(bag_file,output_dir,image_topic)
extract_obj.extract()
del extract_obj






