
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# ## Step 2 Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[3]:


df = pd.read_csv("all_data.csv")


# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[4]:


# Chile, China, Germany, Mexico, the United States of America and Zimbabwa


# What years are represented in the data?

# In[5]:


# From 2000 to 2015, total 16 years


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[6]:


df.head()


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[7]:


df = df.rename(index=str, columns={
    "Life expectancy at birth (years)":"LEABY"
})


# Run `df.head()` again to check your new column name worked.

# In[8]:


df.head()


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[9]:


fig = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="Country", y="GDP")
plt.show()


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[10]:


fig = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="Country", y="LEABY")
plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[11]:


# Yes, a little bit similar. The country of the lowest GDP has the lowest life expectancy at birth, and vice versa.
# However, the rank of the countries in middle range of GDP is not simliar as the rank in life expectancy at birth.


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[12]:


fig = plt.subplots(figsize=(15, 10)) 
sns.violinplot(data=df, x="Country", y="LEABY")


# What do you notice about this distribution? Which country's life expectancy has changed the most?

# In[13]:


# The distribution shapes of the United States, Germany and Chile look similar.
# China and Mexico have different shapes of life expactancy distribution from foregoing three countries.
# However, Zimbabwe is the one whose life expectancy changed the most.


# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[14]:


f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data = df, x= "Country", y="GDP", hue="Year")
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.xticks(rotation=90)
plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[15]:


f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data = df, x= "Country", y="LEABY", hue="Year")
plt.xticks(rotation=90)
ax.set(ylabel="Life expectancy at birth in years")
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[16]:


# Zimbabwe's life expectancy at birth in years changed the most.
# From 2008-2010, Zimbabwe had the biggest changes.
# Zimbabewe has the least change in GDP and it is the lowest GDP among these countries.
# China and the United States had bigger changes in GDP, and the changes of GDP in Chile and Mexico were gentle.
# Through these two bar charts, I think low GDP results in bigger changes in life expectancy and high GDP leads to stable growth.
# The development of medical technology results in the growth of life expectancy in these countries. Moreover, financial aids to Zimbabwe may be the reason of the dramatically upward change in life expectancy. 


# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[18]:


# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter


# Uncomment the code below and fill in the blanks
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, height=2)
g = (g.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend())


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[19]:


# China moves the most to the right among the X axis, which means China's GDP grows fastest.
# Zimbabwe moves the most to the up among the Y axis.
# It's not surprising because I can notice that from foregoing charts.
# But I think these scatter plots are easier to catch the changes in charts. 


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[20]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


# Uncomment the code below and fill in the blanks
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

# In[21]:


# Zimbabwe's life expectancy changes the most.
# In the data, Zimbabwe had the biggest changes during 2007-2010.
# The United States has the least change.
# The countries of high and stable life expectancy have strong economics environment, because the citizens in these countries can afford proper medical service.
# But advanced medical technology has its limit to extend human life. So we can see the changes in the well-developed countries are moderate.
# It's worth noting that Zimbabewe had a curve that decline first then grows. The country may have experienced war and then have financial aids or medical aids from developed countries.  


# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[23]:


g4 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g4 = (g4.map(plt.plot, "Year", "GDP", color="c").add_legend())


# Which countries have the highest and lowest GDP?

# In[24]:


# The United States has the highest GDP, and Zimbabwe has the lowest one.


# Which countries have the highest and lowest life expectancy?

# In[25]:


# Germany has the highst life expectancy, and Zimbabewe has the lowest one.


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[26]:


# Select China data and create a dataframe
china_data = df[(df.Country == "China")]
Year = range(2000, 2016)
# Create a chart describing the growth of China's GDP
sns.set(style="darkgrid")
f, c = plt.subplots(figsize=(10, 5)) 
c = sns.lineplot(data=china_data, x="Year", y="GDP")
c.set_ylabel("GDP in Triilions of U.S. Dollars")
c.set_ylim(0, 1.2E+13)
c.set_xticks(Year, minor=False)
plt.title("The GDP of China in 2000-2015")


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??

# In[27]:


# Set all chart's style
sns.set(style="darkgrid", palette="Set3")

# 1: Violin plot of the life expectancy distribution by country
f, ax1 = plt.subplots(figsize=(15, 5)) 
ax1 = sns.violinplot(data=df, x="Country", y="LEABY", legend="full")
ax1.set_ylabel("Life Expectancy at Birth (Years)")
plt.title("Life Expectancy in Selected Six Countries", fontsize=15)
#plt.savefig("01_ViolinPlot_LEABY_Country.png")


# In[28]:


# 2: Facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
g2 = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=3, height=3)
g2.map(plt.scatter, "LEABY", "GDP")

axes = g2.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g2.set_axis_labels(x_var="Life Expectancy at Birth (Years)", y_var="GDP in Trillions of U.S. Dollars")
g2.fig.suptitle("GDP and Life Expectancy at Birth in Selected Six Countries", fontsize=15)
plt.subplots_adjust(top=0.88)
#plt.savefig("02_FacetGrid_GDPandLEATY_Country.png")


# In[29]:


# 3: Facet grid of line graphs mapping GDP by country
g3 = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=3, height=3)
g3.map(plt.plot, "Year", "GDP")

axes = g3.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g3.set_axis_labels(x_var="Year", y_var="GDP in Trillions of U.S. Dollars")
g3.fig.suptitle("GDP in Selected Six Countries, 2000-2015", fontsize=15)
plt.subplots_adjust(top=0.88)
#plt.savefig("03_FacetGrid_YearandGDP_Country.png")


# In[30]:


# 4: Facet grid of line graphs mapping Life Expectancy by country
g4 = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=3, height=3)
g4.map(plt.plot, "Year", "LEABY")

axes = g4.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g4.set_axis_labels(x_var="Year", y_var="Life Expectancy at Birth (Years)")
g4.fig.suptitle("Life Expectancy in Selected Six Countries, 2000-2015", fontsize=15)
plt.subplots_adjust(top=0.88)
#plt.savefig("04_FacetGrid_YearandLEABY_Country.png")


# In[31]:


# Calculate the difference of GDP and life expectancy in every year

df.set_index(["Country", "Year"], inplace=True)
df.sort_index(inplace=True)

df["GDP_diff"] = np.nan 
for idx in df.index.levels[0]:
    df.GDP_diff[idx] = df.GDP[idx].diff()
df["LEABY_diff"] = np.nan
for idx in df.index.levels[0]:
    df.LEABY_diff[idx] = df.LEABY[idx].diff()

# Calculate the percentage change of GDP and life expectancy in every year
df["GDP_pctchange"] = np.nan 
for idx in df.index.levels[0]:
    df.GDP_pctchange[idx] = df.GDP[idx].pct_change()
df["LEABY_pctchange"] = np.nan
for idx in df.index.levels[0]:
    df.LEABY_pctchange[idx] = df.LEABY[idx].pct_change()
df.head(35)    


# In[32]:


# Reset index for mapping graphs
df = df.reset_index()
df.head()


# In[33]:


# Overview of GDP and life expectancy difference by country
f, ax2 = plt.subplots(figsize=(15, 5)) 
ax2 = sns.lineplot(data=df,x="Year", y="GDP_diff", hue="Country", legend="full", marker=".")

f, ax3 = plt.subplots(figsize=(15, 5)) 
ax3 = sns.lineplot(data=df,x="Year", y="LEABY_diff", hue="Country", legend="full", marker=".")

f, ax4 = plt.subplots(figsize=(15, 5))
ax4 = sns.lineplot(data=df, x="GDP", y="LEABY_pctchange", hue="Country", legend="full", marker="o")
ax4.set_xlabel("GDP (Trillion USD$)")
ax4.set_ylabel("Life Expectancy % Change")
ax4.set_title("GDP and Life Expectancy Percentage Change, 2000-2015", fontsize=15)
#plt.savefig("05_lineplot_GDP_LEABYpctchange.png")


# In[34]:


# Overview of all variables' relationships
g5 = sns.PairGrid(df, hue="Country")
g5.map(plt.scatter)


# In[37]:


# 6: Facet grid of scatter graphs mapping life expectancy difference as a function of GDP difference by country
g6 = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=3, height=3, aspect=1.8)
g6.map(plt.scatter, "GDP_diff", "LEABY_diff")
g6.fig.subplots_adjust(wspace=.02)

axes = g6.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g6.set_axis_labels(x_var="GDP Difference", y_var="Life Expectancy Difference")
g6.fig.suptitle("Returns of Life Expectancy and GDP in Selected Six Countries, 2000-2015", fontsize=15)
plt.subplots_adjust(top=0.88)
#plt.savefig("06_FacetGrid_diff_GDPandLEABY.png")


# In[35]:


# 7: Facet grid of liner model and scatter graph mapping life expectancy percentage change 
# as a function of GDP percentage change by country

g7 = sns.lmplot(data=df,x="GDP_pctchange", y="LEABY_pctchange", col="Country",hue="Country", legend="full",
                   scatter_kws={"marker": "S", "s": 100}, col_wrap=3, height=3, aspect=1.8)
g7.set_axis_labels("GDP % Change", "Life Expectancy % Change")
g7.set(xlim=(-0.25, 1.10), ylim=(-0.05, 0.075))
g7.fig.subplots_adjust(wspace=.02)

axes = g7.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g7.fig.suptitle("Percentage Change of GDP and Life Expectancy in Selected Six Countries, 2000-2015", fontsize=15)
plt.subplots_adjust(top=0.88)

#plt.savefig("07_lmplot_pctchange_GDPandLEABY.png")


# In[38]:


# 8: Facet grid of scatter graph mapping life expectancy percentage change 
# as a function of GDP percentage change by country
g8 = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=3, height=3, aspect=1.8)
#g8.map(plt.scatter, "GDP_pctchange", "LEABY_pctchange")
g8.map(plt.scatter, "GDP_pctchange", "LEABY_pctchange").fig.subplots_adjust(wspace=.02)

#g8.fig.subplots_adjust(wspace=.02)

axes = g8.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g8.set_axis_labels("GDP % Change", "Life Expectancy % Change")
g8.fig.suptitle("Percentage Change of GDP and Life Expectancy in Selected Six Countries, 2000-2015", fontsize=15)
plt.subplots_adjust(top=0.88)

#plt.savefig("08_FacetGrid_scatter_pctchange_GDPandLEATY.png")


# In[36]:


# 9: Facet grid of scatter graph mapping life expectancy percentage change 
# as a function of GDP by country
g9 = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=3, height=3, aspect=1.8)
g9.map(plt.scatter, "GDP", "LEABY_pctchange")
g9.fig.subplots_adjust(wspace=.02)

axes = g9.axes.flatten()
axes[0].set_title("Chile")
axes[1].set_title("China")
axes[2].set_title("Germany")
axes[3].set_title("Mexico")
axes[4].set_title("United States of America")
axes[5].set_title("Zimbabwe")
g9.set_axis_labels("GDP (Trillion USD$)", "Life Expectancy % Change")
g9.fig.suptitle("GDP and Percentage Change of Life Expectancy in Selected Six Countries, 2000-2015", fontsize=15)
plt.subplots_adjust(top=0.88)

#plt.savefig("09_FacetGrid_scatter_GDPandLEATYpctchange.png")

