#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename


testingrooms = ['A','B','C'] #You have three testing rooms
for room in testingrooms:
    path_testingroom = 'testingroom' + room + '\experimental_data.csv' #In the folder Testingroom, you have 3 experimentaldata.csv files
    path_rawdata = 'rawdata\experimental_data_' + room + '.csv' #In the folder rawdata, you have 3 experimentaldata.csv files
    shutil.copy= (path_testingroom, path_rawdata) #Copy files from testingroom folders to rawdata folder and rename files to include testing room letter in filename 
            
    


   
#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
data = np.empty((0,5)) #The top row for my dataframe 
for room in testingrooms: #For all the testing rooms
    new_path = 'rawdata/experiment_data_' + room + '.csv' #Create a new path that has raw data and all the experimentaldata.csv files in it
    tmp =  sp.loadtxt(new_path, delimiter=',') #Make a temporary array and load in what's inside the new path, create seperate columns
    data = np.vstack ([data, tmp]) #Stack all the data together
    
      
#%%
# calculate overall average accuracy and average median RT
#
acc_avg = ...   # 91.48%
mrt_avg = ...   # 477.3ms

#Make 5 columns with the names subject, stimulus, pairing, accuracy and median RT

subject_number = data [:,0] #Make the first column be subject number 
stimuli = data [:,1] #Make the second column be stimuli
pairing = data [:,2] #Make the third column be pairing 
accuracy = data [:,3] #Make the fourth column be accuracy
mrt = data [:, 4] #Make the fifth column be median RT

acc_avg = np.mean (accuracy*100) #The average accuracy = 91.48%
mrt_avg = np.mean (mrt) #The average median RT = 477.3ms

#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
...

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


sum1=0 #empty bin 
sum2=0 #empty bin
sum3=0 #empty bin
sum4=0 #emtpty bin

words=0 #empty bin
faces=0 #empty bin

for i in range (len(subject_number)): #Finding accuracy and mrt of the first stimuli: words, using a loop to loop through the data
    if stimuli [i]==1: 
        words += 1
        sum1 = sum1 + accuracy[i]
        sum2 = sum2 + mrt [i]
    else: #if it's not words, then it's the second stimuli, which is faces
        faces += 1
        sum3 = sum3 + accuracy[i]
        sum4 = sum4 + mrt[i]
    
wordsacc_avg = (sum1 / words) *100 #Calculating the word accuracy average = 88.6 
faceacc_avg = (sum3 / faces) * 100 #Calculating the face accuracy average = 94.4%
wordsavg_mrt = sum2 / words #Calculating the word median RT average = 489.4
facesavg_mrt = sum4 / faces #Calculating the face median RT average= 465.3ms

#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
acc_wp = ...  # 94.0%
acc_bp = ...  # 88.9%
mrt_wp = ...  # 469.6ms
mrt_bp = ...  # 485.1ms

wp1 = [] #empty bin
wp2 = [] #emptybin
bp1 = [] #emptybin
bp2 = [] #emptybin

for i in range(len(subject_number)): #Finding accuracy and mrt of white/pleasant
    if pairing[i] ==1:
        wp1.append(accuracy[i])
        wp2.append(mrt[i])
    else:
        bp1.append(accuracy[i]) #Finding accuracy and mrt of black/pleasant 
        bp2.append(mrt[i])
        
acc_wp =np.mean(wp1)*100 #Calculating the white/plesant accuracy= 94.0%
acc_bp = np.mean(bp1)*100 #Calculating the black/plesant accuracy= 88.9%
mrt_wp =np.mean(wp2) #Calculating the white/plesant mrt= 469.6ms
mrt_bp = np.mean(bp2) #Calculating the black/plesant mrt= 485.1ms 


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
...

# words - white/pleasant: 478.4ms
# words - black/pleasant: 500.3ms
# faces - white/pleasant: 460.8ms
# faces - black/pleasant: 469.9ms

wordswp = []
wordsbp = []
faceswp = []
facesbp = []

for i in range(len(subject_number)):
    if pairing[i] == 1 and stimuli[i] ==1: #words- white/plesant
        wordswp.append(mrt[i])
        
    elif pairing[i] == 2 and stimuli[i] == 1: #words- black/plesant
        wordsbp.append(mrt[i])
        
    elif pairing[i] ==1 and stimuli[i] ==2: #faces- white/plesant
        faceswp.append(mrt[i])
        
    elif pairing[i] ==2 and stimuli[i] ==2: #facse- black/plesant
        facesbp.append(mrt[i])
        
mrt_wordswp = np.mean(wordswp) #mrt for words- white/plesant
mrt_wordsbp = np.mean(wordsbp) #mrt for words- black/plesant

mrt_faceswp = np.mean(faceswp) #mrt for faces- white/plesant
mrt_facesbp = np.mean(facesbp) #mrt for faces-black/plesant



#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
...

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096

wordswp_array = np.asarray(wordswp) #You need to change input into an array
wordsbp_array = np.asarray(wordsbp)

faceswp_array = np.asarray(faceswp)
facesbp_array = np.asarray(facesbp)

t1 = scipy.stats.ttest_rel(wordswp_array,wordsbp_array) #Used scipy's paired-sample t-test: spicy.stats.ttest_rel() to do a t-test between words-white plesant and words-black plesant 
t2 = scipy.stats.ttest_rel(faceswp_array,facesbp_array) #Used scipy's paired-sample t-test: spicy.stats.ttest_rel() to do a t-test between faces-white plesant and faces-black plesant





#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...

print('\nOVERALL: {:.1f}%, {:.1f} ms'.format(acc_avg,mrt_avg)) #Print Overall accuracy average and mrt average
print('\nAvg_Stimulus: {:.1f}%, {:.1f}%, {:.1f} ms,{:.1f} ms'.format(wordsacc_avg,faceacc_avg,wordsavg_mrt,facesavg_mrt)) #Print 4 stimuli
print('\nAvg_Pairing: {:.1f}%, {:.1f}%, {:.1f} ms,{:.1f} ms'.format(acc_wp,acc_bp,mrt_wp,mrt_bp)) #Print 4 pairings
print('\nAvg_mrt: {:.1f}%, {:.1f}%, {:.1f} ms,{:.1f} ms'.format(mrt_wordswp,mrt_wordsbp,mrt_faceswp,mrt_facesbp)) #Print 4 average mrts

print("t-test [wordswp_array,wordsbp_array]",t1) #T-test 1 for words-white/plesant and words- black/plesant
print("t-test [faceswp_array,facesbp_array]",t2) #T-test 2 for faces-white/plesant and faces-black/plesant

