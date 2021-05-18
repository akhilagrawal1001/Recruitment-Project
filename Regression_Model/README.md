Google Colab Link for the file :
	
	https://colab.research.google.com/drive/15pu6VZ9CUohoHZ23iWIjGrtgbr6lClYo?usp=sharing

Though I have uploaded the .py file of the colab here, the code is written in colab, so execution of code would be error-free if it is done on google colab. 


This model predicts the hourly energy output of a power plant(in mega watts), given input being :

	- Temperature (T) in the range 1.81°C and 37.11°C,
	- Ambient Pressure (AP) in the range 992.89-1033.30 milibar,
	- Relative Humidity (RH) in the range 25.56% to 100.16%
	- Exhaust Vacuum (V) in teh range 25.36-81.56 cm Hg

This is a regression problem, and the data for training the model is taken from "https://archive.ics.uci.edu/ml/datasets/Combined+Cycle+Power+Plant"

