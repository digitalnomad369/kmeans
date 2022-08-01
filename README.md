# kmeans

# TABLE OF CONTENTS #

[System Objectives and Description](#System-Objectives-and-Description)

[System Requirements and Installation](#System-Requirements-and-Installation)

[Application components](#Application-components)

[Sample output](#Sample-output)

[References](#References)

[Contributors](#Contributors)

[License and Copyright](#License-and-Copyright)

# System Objectives and Description
		
kmeans is a program aimed at implementing the k-means clustering algorithm on predefined datasets. 

To assist in the implementation of the k-means algorithm, functions were written to achieve the following:
- finding the Euclidean distance between two data points
- reading csv files 
- find the nearest centroid to each data point of all the centroid 
- visualizing the clusters

The program should output the following:
1. The number of countries belonging to each cluster
2. The list of countries belonging to each cluster
3. The mean Life Expectancy and Birth Rate for each cluster

# System Requirements and Installation 

As the program is coded in Python, in order to run and test the code, the following IDE is required:

__- The Python IDE:__
To download the Python IDE, click on the following link to access the official Python website: 
*https://www.python.org/downloads/*

Alternatively, you can download Visual Studio Code which also supports compatibility for Python code
- To download the Visual Studio Code IDE including the Coding Pack for Python, click on the following link: 
*https://code.visualstudio.com/docs/python/coding-pack-python*

In order to perform machine learning algorithms, you will also be required to install the Python SciPy, 
NumPy, Matplotlib and Sci-Kit learn packages. 

To install these packages, do the following:

- Open the command prompt or terminal on your device
- To install SciPy, type “__pip install scipy__” and press Enter.
- To install NumPy, type “__pip install numpy__” and press Enter.
- To install Matplotlib, type “__pip install matplotlib__” and press Enter.
- To install Sci-Kit, type “__pip install sklearn__” and press Enter.

# Application components

To improve the structure and readability of the code, the __kmeans.py__
is comprised of the following code blocks:

- __K-means algorithm pseudocode__: this code block provides a bried, but concise 
  pseudocode of how the k-means algorithm will be implemented.
- __References__: in this block, links are provided as acknowledgement of external resources used
  for this program.
- __Libraries__: in this block all external packages (csv, numpy and matplotlib) are imported. 
- __Functions__: in these code blocks all required functions are declared. 
                 The following functions were used
		 1. __euclidean_dist_calc__ (this function computes the distance between two data points)
		 2. __read_csv__ (this function reads in data from csv files)
		 3. __nearest_centroid__ (this function finds the closest centroid to each point of all 
		   the centroids)
		 4.__cluster_scatterplot__ (this function helps to plot and visualize the clusters)

# References 

__Calculating Euclidean distance:__

*https://www.delftstack.com/howto/numpy/calculate-euclidean-distance/*

__Reading CSV files:__

*https://docs.python.org/2/library/csv.html/*

__Creating cluster scatterplots:_

*https://www.askpython.com/python/examples/plot-k-means-clusters-python*

# Contributors

Tammy-Lee Bastian

tammyleebastian@gmail.com

# License and Copyright

  © Tammy-Lee Bastian
  
   Licensed under the [MIT License](LICENSE)

  
  



