# K-Means clustering implementation in Python

"""K-means algorithm:

   - Ask user to enter input the data set they want to use
   - Ask user to input their desired number of clusters and iterations
   - For user-specified number of iterations do the following:
     * call nearest_centroid() function to find closest centroid to
       each data point and assign point to corresponding centroid's cluster
     * calculate updated mean of all data points in cluster
     * call cluster_scatterplot() function to plot centroids
     
   - Initialise final cluster data
   - Print the number of countries belonging to each cluster
   - Print the list of countries belonging to each cluster
   - Print the mean life expectancy and birth rate for each cluster

   REFERENCES

   Euclidean distance -
   https://www.delftstack.com/howto/numpy/calculate-euclidean-distance/

   Read CSV files - https://docs.python.org/2/library/csv.html

   Cluster scatterplot -
   https://www.askpython.com/python/examples/plot-k-means-clusters-python
   """

# LIBRARIES
# Import required packages
import csv
import numpy as np
import matplotlib.pyplot as plot
# ====

# FUNCTIONS
# Euclidean function that computes the distance between two data points
# Use np.sqrt(), np.sum() and np.square() functions to perform calculation

def euclidean_dist_calc(x, y):
    return np.sqrt(np.sum(np.square(x-y)))
# ====

# Function that reads data in from csv files

def read_csv(file):
    with open(file, 'r') as csv_file:
        read_data = csv.DictReader(csv_file, delimiter=',')
        file_data =[]
        for row in read_data:
            file_data.append(row) # Add file data to list
    values = [list(dictionary.values())[1:] for dictionary in file_data]
    # Convert data into float values
    values = [list(map(float, val)) for val in values]
    return values  # return values
# ====

# Function that finds the closest centroid to each point out of
# all the centroids

def nearest_centroid(data, centroids):
    # use dictionary to assign centroid to corresponding data points
    init_centroid = {}
    for j in range(len(centroids)):
        init_centroid[j]= []
    for i in data:
        dist =[]
        # call euclidean_dist_calc() function to
        # calculate distance to all centroids
        for j in centroids:
            dist.append(euclidean_dist_calc(np.array(i),np.array(j)))
        # find index of smallest value in dist array using np.argmin() function
        init_centroid[np.argmin(dist)].append(i)
    return init_centroid
#====

# Function to visualise the clusters.

def cluster_scatterplot(assigned_data, centroids, iter):
    # plot centroids
    plot.figure()
    plot.scatter(np.array(centroids)[:,0],np.array(centroids)[:,1], c='black')
    for x in range(len(centroids)):
        plot.scatter(np.array(assigned_data[x])[:,0],np.array(
            assigned_data[x])[:,1],alpha = 0.2)
    # Add labels for title, x and y-axis on graph
    plot.xlabel("Birth Rate")
    plot.ylabel("Life Expectancy")
    plot.title(f"Number of centroids and clusters in iteration {iter+1}")
    # save and display cluster scatterplot
    plot.savefig(f"Cluster scatterplot {iter}.jpg", bbox_inches='tight')
    plot.show()
#====
    
# INITIALISATION PROCEDURE
# Ask user to enter the name of the dataset they want to use

file = input("""\nPlease enter the file name you want to use:
                    data1953.csv
                    data2008.csv
                    dataBoth.csv \n""")
        
# Initialise number of clusters k and iterations
num_of_clusters=2
num_of_iters=6

# ask user to enter their desired number of clusters
while True:
    try:
        num_of_clusters = int(input("\nPlease enter the number of clusters you want: "))
        break
    except ValueError:
        print("Error. Please enter a valid number of clusters: ")
         
# ask user to enter their desired number of iterations
while True:
    try:
        num_of_iters = int(input("\nPlease enter the number of iterations you want: "))
        break
    except ValueError:
        print("Error. Please enter a valid number of clusters: ")

# Initialise random centroids from csv file and add to 'centroids' list
fd = read_csv(file)   
centroid_index = np.random.choice(len(fd), num_of_clusters)
centroids= []
for index in centroid_index:
    centroids.append(fd[index])      
#====
  
# IMPLEMENTATION OF K-means ALGORITHM
# Iterate through number of iterations
for i in range(num_of_iters):
    # find nearest centroid to each data point
    # assign the point to that centroid's cluster
    assigned_centroids = nearest_centroid(fd,centroids)
    # Calculate the new mean of all points in the cluster
    new_cent_mean =[np.mean(assigned_centroids[centroid],axis=0)
                    for centroid in assigned_centroids.keys()]
    # Visualisation of cluster after each iteration
    cluster_scatterplot(nearest_centroid(fd,new_cent_mean),new_cent_mean,i)
    centroids = new_cent_mean
# ====

# FINAL CLUSTER DATA
fin_data = nearest_centroid(fd,centroids)

# PRINT RESULTS

#1.) Display the number of countries belonging to each cluster
for i in range(len(centroids)):
    print(f"\nNumber of countries in cluster with centroid {centroids[i]} = {len(fin_data[i])}")

# Get birth rate and life expectancy data for each country
cty_data = []

with open(file, 'r') as csv_file:
    read_data = csv.DictReader(csv_file, delimiter = ',')
    for row in read_data:
        cty_data.append(list(row.values())) #append data to cty_data list

#2.) Display the list of countries belonging to each cluster
for i in range(len(centroids)):
    print(f"\nCountries in cluster with centroid {centroids[i]}\n")
    for j in fin_data[i]:
        cty = [values[0] for values in cty_data if values[1]==str(j[0])
               and values[2] == str(j[1])]
        if len(cty)>0:
            print(cty[0])
            
#3.) Display the mean life expectancy and birth rate for each cluster
for i in range(len(centroids)):
    print(f"""\nThe mean life expectancy and birth rate for cluster with centroid {centroids[i]} =
{round(np.mean(fin_data[i],axis=0)[1],3)},{round(np.mean(fin_data[i],axis=0)[0],3)}""")

# End Program
