import pandas as pd 
import scipy.stats as stat
import numpy as np 
import matplotlib.pyplot as plt
fig , ax  = plt.subplots(2,2, figsize= (10,8)) 
normal_dist= pd.read_csv(r"C:\Users\Srujan kumar\Downloads\archive (2)\CompanyABCProfit.csv")
uniform_dist = pd.read_csv(r"C:\Users\Srujan kumar\Downloads\uniform_distribution_300.csv")
log_normal_dist = pd.read_csv(r"C:\Users\Srujan kumar\Downloads\log_normal_distribution_300.csv")
pareto_dist = pd.read_csv(r"C:\Users\Srujan kumar\Downloads\pareto_distribution_300.csv")
#two methods are there to know about the distributions of the data hence the 

# 1. histograms --------2.Q_Q plots

 
# >>(1.HISTOGRAM)
ax[0][0].hist(normal_dist.iloc[:, 1], bins="auto")
ax[0][0].set_title("NORMAL DISTRIBUTION")
ax[0][1].hist(uniform_dist.iloc[:, 1], bins="auto")
ax[0][1].set_title("UNIFORM DISTRIBUTION")
ax[1][0].hist(log_normal_dist.iloc[:, 1], bins="auto")
ax[1][0].set_title("LOGNORMAL DISTRIBUTION")
ax[1][1].hist(pareto_dist.iloc[:, 1], bins="auto")
ax[1][1].set_title("PARETO DISTRIBUTION")
plt.show()

#>>(Q-Qplots)


fig , ax = plt.subplots(2,2,figsize=(10,8))
# let us assume all the graphs are normal as so how the qq will be plot
# the real normal will only get aquire more points on the line 
stat.probplot(normal_dist.iloc[:,1],dist = stat.norm,plot = ax[0,1])
stat.probplot(uniform_dist.iloc[:,1],dist = stat.norm,plot = ax[1,1])
stat.probplot(log_normal_dist.iloc[:,1],dist = stat.norm,plot = ax[1,0])
stat.probplot(pareto_dist.iloc[:,1],dist = stat.norm,plot = ax[0,0])

fig , ax = plt.subplots(2,2,figsize=(10,8))
stat.probplot(normal_dist.iloc[:,1],dist = stat.norm,plot = ax[0,1])
stat.probplot(uniform_dist.iloc[:,1],dist =stat.uniform,plot = ax[1,1])
stat.probplot(np.log(log_normal_dist.iloc[:,1]),dist = stat.norm,plot = ax[1,0]) # here i used log of log_normal data which follows normal distribution
#then we can say that the distrubition is lognormal, if we need mean and std of the data
b, loc, scale = stat.pareto.fit(pareto_dist.iloc[:, 1])
# b is a patero shape parameter which controls the tail of the distribution
# loc loaction parameter 
# scale how much the distribution is scaled along the x-axis
stat.probplot(
    pareto_dist.iloc[:, 1],
    dist=stat.pareto,
    sparams=(b,),
    plot=ax[0, 0]
)
plt.show()
