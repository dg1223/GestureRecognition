# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 23:33:24 2015

@author: Shamir
"""

import pandas
import numpy as np
import os

class DataHandler(object):
    """It reads the data, combines columns that gave identical headings and writes the processed data to a CSV file.
       It also asks the user to specify the filepath where the datafiles or desired folders can be found.
    
    columns include:
        qr, qx, qy, qz and time
        qr: scalar element of the quaternion
        qx,qy,qz: vector elements of the quaternion
        time: timestamp (this class does not deal with timestamps)
    """
    
    def _init_(self):

    def sortbyColumns(self):
        gesture_path = 'C:\\Users\\Shamir\\Desktop\\Grad\\Gesture Stuff\\Data_Multisensor\\'    # use input() to make it interactive
        destination =  'C:\\Users\\Shamir\\Desktop\\broken down files\\'
        fileformat = '.csv'
        backslash = '\\'
        
        count = 1
        for i in range(len(os.listdir(gesture_path))):                                          # we have 6 files corresponding to 6 gestures
            gesture = os.listdir(gesture_path)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
            
            for j in range(len(os.listdir(gesture_path + gesture))):                            # we have 3 files corresponding to 3 datasets (train, cross-validation, test)
                dataset = os.listdir(gesture_path + gesture)[j]                                 # Train, Cross Validation, Test
                
                for k in range(len(os.listdir(gesture_path + gesture + backslash + dataset))):  # we have 5 sensors (15,16,17,18,19) 
                    file = os.listdir(gesture_path + gesture + backslash + dataset)[k]          # desired csv file in the folder           
                    csvfile = gesture_path + gesture + backslash + dataset + backslash + file   # full filepath
                    print csvfile
                    readFile = pandas.read_csv(csvfile, header = None)                          # read csv file
                    
                    qr = readFile.loc[:, range(0, readFile.shape[1], 5)]                            # qr columns only
                    qr.to_csv(destination + str(count) + fileformat, header = False, index = False)
                    count += 1
                    
                    qx = readFile.loc[:, range(1, readFile.shape[1], 5)]                            # qx columns only
                    qx.to_csv(destination + str(count) + fileformat, header = False, index = False)
                    count += 1
                    
                    qy = readFile.loc[:, range(2, readFile.shape[1], 5)]                            # qy columns only  
                    qy.to_csv(destination + str(count) + fileformat, header = False, index = False)
                    count += 1
                    
                    qz = readFile.loc[:, range(3, readFile.shape[1], 5)]                            # qz columns only
                    qz.to_csv(destination + str(count) + fileformat, header = False, index = False)
                    count += 1
                    
                    
    def linearInterpolation(self, prev_datapoint, target_datapoint, next_datapoint):
        denominator = next_datapoint - prev_datapoint
        numerator = ((target_datapoint - prev_datapoint) * (file.values[i, next_datapoint] - file.values[i, prev_datapoint]))
        interpolated_value = (numerator/denominator) + file.values[i, prev_datapoint]
        
        return interpolated_value
    
    
    def removeOutliers(self):
        
        
        