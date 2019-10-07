from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import pandas as pd
import numpy as np

def load_preproc_data():    
		
		def show_feature_set(fs):
			for (i, feature) in enumerate(fs, start=1):
				print (i, feature)
		
		#Step 1: Read the data file to get all the features
		filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wa_hmda_small.csv')

		try:
            #Input separator to used in the data file
			#i_data_separator = int(input("Enter the data separator used ? "))
			i_data_separator = ','
			#Input the value used for na_values in the data file
			#i_na_values = int(input("Enter value used for na_values ? "))
			i_na_values = '?'
			
			df = pd.read_csv(filepath, sep=i_data_separator, na_values=i_na_values)               
						
		except IOError as err:
			print("IOError: {}".format(err))
			print("\nand place them, as-is, in the folder:")
			import sys
			sys.exit(1)
		
		#Step 1: Read the first column of the data file for all the features
		# Iterating through the columns and adding to the feature list
		XD_features = []	
		for features in df.columns: 
			#print(features)
			XD_features.append(features)
		#Step 2: Display list of features with index for user to select 
		#print("Features in the data set: ")
		#show_feature_set(XD_features)
		return XD_features
def main():
		print("Hello, World!")
if __name__== "__main__" :
	print("Hello, World!\n")
	XD_features=[] #Use this list to populate the list in the UI
	XD_features=load_preproc_data() 
	#print(XD_features)
	main()