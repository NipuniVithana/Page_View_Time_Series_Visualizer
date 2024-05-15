
# Page View Time Series Visualizer

This project visualizes time series data from the freeCodeCamp.org forum, specifically the number of page views each day from May 2016 to December 2019. Using Pandas, Matplotlib, and Seaborn, it provides insights into the patterns of visits and identifies yearly and monthly growth.

## Dataset

The dataset used in this project is stored in the file `fcc-forum-pageviews.csv`. It contains daily page view data with the date column as the index.

## Data Cleaning

Before visualization, the data is cleaned by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.

## Functions

### `draw_line_plot()`

This function draws a line chart depicting the daily freeCodeCamp Forum page views from May 2016 to December 2019. The title of the chart is "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", and the x-axis label is "Date", while the y-axis label is "Page Views".

### `draw_bar_plot()`

This function draws a bar chart displaying the average daily page views for each month grouped by year. The legend shows month labels, and it has a title of "Months". The x-axis label is "Years", and the y-axis label is "Average Page Views".

### `draw_box_plot()`

This function draws two adjacent box plots using Seaborn. The first plot shows the distribution of page views within a given year (Year-wise Box Plot), while the second plot shows the distribution by month (Month-wise Box Plot). The month labels start from January, and the x and y axes are labeled correctly.


