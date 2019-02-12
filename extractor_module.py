#!/usr/bin/env python
# -- coding: utf-8 --

# Copyright 2016 Massachusetts Institute of Technology
# I changed a few things for myself - KennyC

"""Extract images from a rosbag. CHANGE FFMPEG SETTINGS BELOW. TO USE INTERPOLATION UPDATE YOUR FFMPEG
"""

import os
import errno
import argparse

import cv2

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import pdb
import subprocess

class Extractor(object):

	def __init__(self,bag_file,image_topic):	
		#self.bag_file = bag_file
		#self.output_dir = output_dir
		#self.image_topic = image_topic
		self.list = [bag_file,image_topic]
	
	def __del__(self):
		print "object instance is deleted"
		
	def extract(self):	
	  for i in range(len(self.list[0])):
		  """Extract a folder of images from a rosbag.
		  """
		  bag_file = self.list[0][i]
		  output_dir = "./"+bag_file[0:-4]+"/"
		  image_topic = self.list[1]
 		  """ Using command line arguments, order matters
		  """

		  #parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
		  #parser.add_argument("bag_file", help="Input ROS bag.")
		  #parser.add_argument("./output/", help="Output directory.")
		  #parser.add_argument("image_topic", help="Image topic.")
		  #args = parser.parse_args()

		  print "Extract images from %s on topic %s into %s" % (bag_file,
		  		             image_topic, output_dir)

		  """ Check if output dir exists, if it doesn't then create one"""
		  if not os.path.exists(output_dir):
		    try:
			os.makedirs(output_dir)
		    except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
			    raise

		  bag = rosbag.Bag(bag_file, "r")
		  bridge = CvBridge()
		  count = 0
		  for topic, msg, t in bag.read_messages(topics=[image_topic]):
		    cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

		    cv2.imwrite(os.path.join(output_dir, "frame%06i.png" % count), cv_img)
		    print "Wrote image %i" % count

		    count += 1
		 
		  bag.close()
		  print "Saving video..."
		  self.save(output_dir,bag_file)
		  print "DONE"
	  return

 	def save(self,output_dir,name):
		"""subprocess is not blocking!!!, so ensure it: Popen object has a .wait() method"""
		#image_dir = os.path.abspath(output_dir)
		#cmds = ['ffmpeg', '-r', '25', '-i', output_dir+'frame%06d.png', "-filter", "minterpolate='fps=25'", '-vcodec', 'mpeg4', '-y', name+".mp4"]
		cmds = ['ffmpeg', '-r', '15', '-i', output_dir+'frame%06d.png', '-vcodec', 'mpeg4', '-y', name+".mp4"]
		proc = subprocess.Popen(cmds)
		proc.wait()


#if __name__ == '__main__':
#  	main()

