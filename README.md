# exercise-1-modularity-WenjieLuo2333
It's a readme document for the architecture based on the design of Mohit.

## Simply run ```main.py``` to excute the process.<br/> And excute ```test.py``` to tun the test.
Threads are defined in ```Input_Thread.py```,```Process_Thread.py```,```UI_Thread.py```.<br/>
And the other modules are borrowed from team members(as the copyright).<br/>

## Input Module
copyright @Kainan Liu, edited by @Wenjie Luo<br/>
Input:<br/>
Bo, bp, pul are input from three txt files.<br/>
Output:<br/>
Three double lists<br/>

## Storage Module
copyright @Gang Wei<br/>
Input:<br/>
data from input module<br/>
Output:<br/>
Save all the data.<br/>


## Alert Module
copyright @Wenjie Luo<br/>
Input:<br/>
Get data from storage. format[float,int]<br/>
Output:<br/>
Alert Flag sent to UI Module<br/>


## AI Module
copyright @Xiang Li
Input:<br/>
Bo, bp, pul are three lists represent the value of blood oxygen, blood pressure and pulse which are defined as double.<br/>
bo, bp, pul: list [float value]<br/>
Output:<br/>
Three double values for estimated health score<br/>

Data received from storage system is input to the unsupervised AI Module, and will generate the output which are three predicted values for patients’ future health condition estimation by using data as blood oxygen, blood pressure and pulse stored in storage system to make prediction.
