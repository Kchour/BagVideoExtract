#!/usr/bin/env python
# -- coding: utf-8 --

# Copyright 2016 Massachusetts Institute of Technology

"""Extract images from a rosbag.
"""

import os
import argparse

import cv2

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import pdb

class Extractor(object):

	def __init__(self,bag_file,output_dir,image_topic):	
		#self.bag_file = bag_file
		#self.output_dir = output_dir
		#self.image_topic = image_topic
		self.list = [bag_file,output_dir,image_topic]
	
	def __del__(self):
		print "object instance is deleted"
		
	def extract(self):	
	  for i in range(len(self.list[0])):
		  """Extract a folder of images from a rosbag.
		  """
		  bag_file = self.list[0][i]
		  output_dir = self.list[1]
		  image_topic = self.list[2]
		   
 		  """ Using command line arguments, order matters
		  """

		  #parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
		  #parser.add_argument("bag_file", help="Input ROS bag.")
		  #parser.add_argument("./output/", help="Output directory.")
		  #parser.add_argument("image_topic", help="Image topic.")
		  #args = parser.parse_args()

		  print "Extract images from %s on topic %s into %s" % (bag_file,
		  		             image_topic, output_dir)

		  bag = rosbag.Bag(bag_file, "r")
		  bridge = CvBridge()
		  count = 0
		  for topic, msg, t in bag.read_messages(topics=[image_topic]):
		    cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

		    cv2.imwrite(os.path.join(output_dir, "frame%06i.png" % count), cv_img)
		    print "Wrote image %i" % count

		    count += 1

		  bag.close()

	  return

#if __name__ == '__main__':
#  	main()

