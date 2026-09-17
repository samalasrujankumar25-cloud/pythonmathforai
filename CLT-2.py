import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats
dist_1 = pd.read_csv(r"C:\Users\Srujan kumar\Downloads\x_distribution.csv")
fig, ax = plt.subplots(2,2,figsize=(10,8))
population_mean= np.mean(dist_1["value"])
print("the population of mean is...", population_mean)
samples=[]
samples_means = []
for i in range(1000) :
    k = np.random.choice(dist_1["value"],50,replace = True) # check with differen sample sizes and observe in plots 
    samples.append(k)
    k_mean = np.mean(k)
    # print(k_mean)
    samples_means.append(k_mean)
samples=np.array(samples)
# sample_size = 
samples_mean = np.array(samples_means)
mean_of_sample_mean = np.mean(samples_mean)
print("the mean of sample means is ...",(mean_of_sample_mean))
size_samples = (samples.shape[1])
ax[0][0].hist(dist_1["value"],bins="auto")
ax[0][0].set_title("HIST OF POPULATION")
ax[0][1].hist(samples_mean,bins = "auto")
ax[0][1].set_title("HIST OF SAMPLES")
stats.probplot(dist_1["value"],dist=stats.norm,plot=ax[1][0])
ax[1][0].set_title("POPULATION")
stats.probplot(samples_mean,dist=stats.norm,plot=ax[1][1]) 
ax[1][1].set_title("SAMPLE_DISTRIBUTION")
plt.show()




