# exercise-1-modularity-WenjieLuo2333
It's a readme document for the architecture based on the design of Mohit.

## Simply run main.py

## Input Module
copyright @Kainan Liu, edited by @Wenjie Luo
### Input:
Bo, bp, pul are input from three txt files.
### Output:
Three double lists

## Storage Module
copyright @Gang Wei
### Input:
data from input module
### Output:
Save all the data.


## Alert Module
copyright @Wenjie Luo
### Input:
Get data from storage. format[float,int]
### Output:
Alert Flag sent to UI Module


## AI Module
copyright @Xiang Li
### Input:
Bo, bp, pul are three lists represent the value of blood oxygen, blood pressure and pulse which are defined as double.
bo, bp, pul: list [float value]
### Output:
Three double values for estimated health score

Data received from storage system is input to the unsupervised AI Module, and will generate the output which are three predicted values for patients’ future health condition estimation by using data as blood oxygen, blood pressure and pulse stored in storage system to make prediction.
