import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv("fcc-forum-pageviews.csv",parse_dates=["date"],index_col="date")

# Clean data
df = df[
    (df["value"]>=df["value"].quantile(0.025))&
    (df["value"]<=df["value"].quantile(0.975))
]


def draw_line_plot():
    fig,ax=plt.subplots(figsize=(10,5))
    ax.plot(df.index,df['value'],'r',linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page_Views')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["month"]=df.index.month
    df["year"]=df.index.year
    df_bar=df.groupby(["year","month"])["value"].mean()
    df_bar=df_bar.unstack()
    

    # Draw bar plot
    fig=df_bar.plot.bar(legend=True,figsize=(13,6),ylabel="Average Page Views",xlabel="Years").figure
    plt.legend(['January','February','March','April','May','June','July','August','September','Novemer','December'])

    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Convert 'value' column to float
    df_box['value'] = df_box['value'].astype(float)

    # Sort data by month
    df_box.sort_values(by='date', inplace=True)

    # Draw box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Trend)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig





