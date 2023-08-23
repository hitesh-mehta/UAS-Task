# UAS-Task
# Search and Rescue 

# Overview
This GitHub repository contains the implementation for the Search and Rescue task. The task involves utilizing UAV-collected images of a civilian area affected by a fire outbreak to gather information about the locations of houses and buildings. The goal is to identify the burnt and green areas, count houses, calculate priorities, and determine rescue ratios.

# Summary of the Work
The goal of this challenge is to process a collection of photographs that a UAV took while flying over a burned-out neighborhood. In addition to residences with varied priority shown as blue and red triangles, the photos also display burned and green areas.

The following results are anticipated for each image:

An output image highlighting the difference between burnt and green areas.

The count of houses on burnt and green areas.

The total priority of houses on burnt and green areas.

A rescue ratio based on the calculated priorities.

A list of image names sorted by their rescue ratios.

# Implementation Steps

Loading and Processing Images: Load the images and preprocess them for further analysis.

Identifying Burnt and Green Areas: Segment the images to differentiate burnt and green grass.

Detecting Houses and Priorities: Utilize object detection techniques to identify houses and assign priorities.

Calculating Counts and Priorities: Count the houses and calculate total priorities for burnt and green areas.

Calculating Rescue Ratios: Calculate rescue ratios based on priority values.

Sorting Images: Sort the images based on their rescue ratios.

Generating Output: Generate output images and lists of counts, priorities, and ratios.

# Getting Started

Clone this repository: git clone https://github.com/hitesh-mehta/UAS-Task
Place your UAV-captured images in the repository's designated folder.
Modify the script to fit your image filenames, paths, and desired parameters.
Run the script.

# Requirements
Python 3.8

OpenCV

NumPy

# Results
The results will be displayed in the form of output images and calculated values for each input image.
