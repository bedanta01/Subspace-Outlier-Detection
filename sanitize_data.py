"""
#
#	WAVEFORM dataset contains 3 classes 0, 1, 2
#	10% downsample the class 0 to treat them as outliers
#	class 1, 2 are treated as inliers
#
"""

from random import shuffle
import pandas as pd

class_0 = []
inlier_points = []
sanitized_waveform_data = []
downsampled_class_0 = []

with open("waveform.data", "r") as filestream:
	for line in filestream:
		#print line
		currentline = line.strip().split(",")
		if(int(currentline[21]) == 0):
			currentline = [float(i) for i in currentline]
			currentline[21] = int(currentline[21])
			class_0.append(currentline)
		else:     
			inlier_points.append(currentline)              ### class 1 and 2 are inliers

shuffle(class_0)

downsampled_class_0 = class_0[:166]                        ### get 10 percent of class 0 points as outliers
sanitized_waveform_data = inlier_points + downsampled_class_0

shuffle(sanitized_waveform_data)

data_frame = pd.DataFrame(sanitized_waveform_data)
data_frame.to_csv("sanitized_waveform.data", index = False, header = False)