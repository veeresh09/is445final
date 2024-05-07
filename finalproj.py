# %% [markdown]
# # Final Project, Part 2
# 
# The purpose of this assignment is to create a 'Viz for Experts' with an interactive dashboard interface for exploring your data.
# 
# For this submission option, you will submit your work through this Workspace.
#     
# **Please see Homework Prompt in PrairieLearn interface for more details on the requirements for this assignment.**
# 
# A rough outline of elements of code and write-up is shown below:

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
import ipywidgets as widgets
import altair as alt
from urllib.request import urlopen
from plotly.offline import plot
import json
import plotly.express as px

# %%
df_1 = pd.read_csv("BEDS_Day_Enrollment.csv")
df_2 = pd.read_csv("BOCES_and_N_RC.csv")
df_3 = pd.read_csv("Demographic_Factors.csv")
df_4 = pd.read_csv("Institution_Grouping.csv")

# # %% [markdown]
# # ## Code:
# # 
# #  * An interactive dashboard within your Workspace that helps an expert explore your dataset thoroughly.
# #  * There should be a "dashboard" type aspect to this - i.e. a linked view exploring your dataset in an interactive way (like in Lab \#4) with [bqplot](https://bqplot.github.io/bqplot/).
# #  * Do not delete any cells, *just comment them out*. Show your work.
# # 
# # 

# # %% [markdown]
# # ## Prose:
# # 
# # * One paragraph explaining how to use the dashboard you created, to help someone who is not an expert understand your dataset.
# # * A list of 1 or more contextual datasets you have identified, links to where they reside, and a sentence about why they might be useful in telling the final story.
# #   * by "contextual dataset" here means a dataset that would add context to your chosen dataset. For example, if your dataset is the Champaign bus routes, some interesting contextual datasets could be the Chicago bus routes, or the Springfield bus routes, or the Amtrak routes in Champaign
# #   * you do not have to do anything with this dataset at the moment beyond writing a bit about why it would be useful. Looking forward, you will want to include "contextual visualizations" (which you may or may not generate on your own) in your Final Project, Part 3 and identifying a possibly useful dataset is a great way to start looking for contextual visualizations.
# # * If you have identified your dataset as a "large one" (i.e. larger than the GitHub file upload limit) comment on if you want to revise your plan for hosting this data or not. If this does not apply to your dataset please explicitly state this.
# # * Additionally, please note that as of writing, it is not possible to embed images within Starboard. Be sure to address how you plan on including your contextual dataset to add context to your main dataset given that you won't be able to directly embed images if you plan on using Starboard for Part 3.1 of the Final Project.
# # 

# # %% [markdown]
# # # Understanding this dashboard
# # The dashboard is designed to help non-experts explore the dataset interactively. Upon opening the dashboard, you'll find a series of visualizations and filtering widgets that provide different perspectives on the data. Use the dropdown menus, sliders, and other controls to select specific criteria like date ranges and geographic regions, which will instantly update the visualizations to reflect your selections. 
# # This dynamic linking makes it easy to understand relationships, trends, and outliers in the dataset. 

# # %% [markdown]
# # # Contextual Dataset
# # A valuable contextual dataset is the College Scorecard dataset, which can be accessed here - https://collegescorecard.ed.gov/data/ 
# # This dataset provides extensive information on institutions across the United States, covering aspects like graduation rates, average earnings of graduates, and student demographics. It offers a comprehensive view of higher education in the U.S. By adding this to our analysis, we could compare our dataset's insights with nationwide educational trends, revealing regional disparities, socioeconomic patterns, and institutional variations. This additional context can deepen the end user's understanding and help tell a more comprehensive story.

# # %% [markdown]
# # ## Plot Topic 1 - Demographic
# # 
# # ### 1.1 Gender & Race Distribution across Years

# # %% [markdown]
# # Our demographic analysis of the enrollment has 2 parts: gender and race. To create a plot showing the gender distribution across 3 years with interactivity, we first created a dropdown menu with the selection of 3 years and made the interactive plot using matplotlib and ipywidget packages.

# # %%
# df_3_year = df_3.groupby('YEAR').mean().reset_index()

# year_dropdown = widgets.Dropdown(
#     options = df_3_year['YEAR'].unique(),
#     value = df_3_year['YEAR'].min(),
#     description = 'Year:',
#     disabled = False
# )

# # %%
# # def update_plot(year):
# #     plt.figure(figsize = (12, 8))
# #     selected_data = df_3_year[df_3_year['YEAR'] == year]

# #     plt.bar(selected_data['YEAR'] - 0.2, selected_data['PER_FEMALE'], width = 0.1, label='% Female')
# #     plt.bar(selected_data['YEAR'] + 0.2, selected_data['PER_MALE'], width = 0.1, label='% Male')
# #     plt.xlabel('Year')
# #     plt.ylabel('Percentage')
# #     plt.title(f'Gender Distribution for {year}')
# #     plt.legend()
# #     plt.xticks([year])
# #     plt.ylim(48, 52)
# #     plt.grid(True)

# # plot_demo = widgets.interactive(update_plot, year=year_dropdown)
# # display(plot_demo)

# # %% [markdown]
# # Since the race distribution would be implemented via a similar approach, we integrated it into the gender plot and made them display together horizontally to use the page space efficiently.

# # %%
# # def update_plot(year):
# #     plt.figure(figsize = (12, 8))
# #     selected_data = df_3_year[df_3_year['YEAR'] == year]
    
# #     plt.subplot(1, 2, 1)
# #     plt.bar(selected_data['YEAR'] - 0.2, selected_data['PER_FEMALE'], width = 0.1, label='% Female')
# #     plt.bar(selected_data['YEAR'] + 0.2, selected_data['PER_MALE'], width = 0.1, label='% Male')
# #     plt.xlabel('Year')
# #     plt.ylabel('Percentage')
# #     plt.title(f'Gender Distribution for {year}')
# #     plt.legend()
# #     plt.xticks([year])
# #     plt.ylim(48, 52)
# #     plt.grid(True)
    
# #     plt.subplot(1, 2, 2)
# #     plt.bar(selected_data['YEAR'] - 0.35, selected_data['PER_AM_IND'], width = 0.1, label = '% American Indian or Alaska Native')
# #     plt.bar(selected_data['YEAR'] - 0.25, selected_data['PER_BLACK'], width = 0.1, label = '% Black or African American')
# #     plt.bar(selected_data['YEAR'] - 0.15, selected_data['PER_ASIAN'], width = 0.1, label = '% Asian or Native Hawaiian/Other Pacific Islander')
# #     plt.bar(selected_data['YEAR'] - 0.05, selected_data['PER_HISP'], width = 0.1, label = '% Hispanic or Latino')
# #     plt.bar(selected_data['YEAR'] + 0.05, selected_data['PER_WHITE'], width = 0.1, label = '% White')
# #     plt.bar(selected_data['YEAR'] + 0.15, selected_data['PER_Multi'], width = 0.1, label = '% Multiracial')
# #     plt.xlabel('Year')
# #     plt.ylabel('Percentage')
# #     plt.title(f'Race Distribution for {year}')
# #     plt.legend()
# #     plt.xticks([year])
# #     plt.ylim(0, 60)
# #     plt.grid(True)

# # plot_demo = widgets.interactive(update_plot, year=year_dropdown)
# # display(plot_demo)

# # %% [markdown]
# # Then, we wanted to export the interactive plot to JSON file and save for the Jekyll page. But we kept receiving errors with no `.save()` function. We guessed that this export function may need to correspond with the altair package taught in class rather than in matplotlib. So, we tried to translate our plot using altair language, with the interactivity still from ipywidgets.

# # %%
# # def update_plot(year):
# #     selected_data = df_3_year[df_3_year['YEAR'] == year]

# #     gender_chart = alt.Chart(selected_data).mark_bar().encode(
# #         x = alt.X('YEAR:O', title = 'Year'),
# #         y = alt.Y('value:Q', axis = alt.Axis(title = 'Percentage'), scale = alt.Scale(domain = (0, 100))),
# #         color = alt.Color('variable:N', legend = alt.Legend(title=None), scale=alt.Scale(domain=['PER_FEMALE', 'PER_MALE'])),
# #         column = alt.Column('variable:N', title=None)
# #     ).transform_fold(
# #         fold=['PER_FEMALE', 'PER_MALE'],
# #         as_=['variable', 'value']
# #     ).properties(
# #         width=100,
# #         height=400,
# #         title=f'Gender Distribution for {year}'
# #     )
    
# #     display(gender_chart)

# # widgets.interactive(update_plot, year=year_dropdown)

# # %% [markdown]
# # However, we found that the `.save()` function still didn't work for storing the interactivity built by ipywidgets. So, we then also translated the dropdown menu part using altair language, and we tried the gender distribution chart first.

# # %%
# # year_dropdown = alt.binding_select(options = df_3_year['YEAR'].unique(), name = "Year: ")
# # year_select = alt.selection_single(fields = ['YEAR'], bind = year_dropdown, name = "Select", value = 2021)

# # gender_chart = alt.Chart(df_3_year).mark_bar().encode(
# #     x = alt.X('Gender:N', title = 'Gender'),
# #     y = alt.Y('Percentage:Q', title = 'Percentage'),
# #     color ='Gender:N',
# #     size = alt.value(40)
# # ).transform_fold(
# #     fold = ['PER_FEMALE', 'PER_MALE'],
# #     as_ = ['Gender', 'Percentage']
# # ).add_selection(
# #     year_select
# # ).transform_filter(
# #     year_select
# # ).properties(
# #     width = 400,
# #     height = 400,
# #     title = 'Gender Distribution by Year'
# # )

# # gender_chart

# # %% [markdown]
# # The plot looked ok and was able to be saved now. Then, we did some refinement to the plot. Since the gap between females and males was tiny on a [0, 100] scale, we enlarged the y-coordinate to make the changes across years more distinctively. We also modified the legend and x-axis labels to be more clear.

# # %%
# # year_dropdown = alt.binding_select(options = df_3_year['YEAR'].unique(), name = "Year: ")
# # year_select = alt.selection_single(fields = ['YEAR'], bind = year_dropdown, name = "Select", value = 2021)

# # gender_chart = alt.Chart(df_3_year).transform_fold(
# #     fold = ['PER_FEMALE', 'PER_MALE'],
# #     as_ = ['Gender', 'Percentage']
# # ).transform_calculate(
# #     Gender_Label = "datum.Gender=='PER_FEMALE' ? 'Female' : 'Male'"
# # ).mark_bar(clip = True).encode(
# #     x = alt.X('Gender_Label:N', title = 'Gender'),
# #     y = alt.Y('Percentage:Q', title = 'Percentage', scale = alt.Scale(domain = (48, 52))),
# #     color = alt.Color('Gender:N', legend = alt.Legend(title = 'Gender', labelExpr = "datum.value=='PER_FEMALE' ? 'Female' : 'Male'"),
# #                       scale = alt.Scale(domain = ['PER_FEMALE', 'PER_MALE'])),
# #     size = alt.value(40)
# # ).add_selection(
# #     year_select
# # ).transform_filter(
# #     year_select
# # ).properties(
# #     width = 400,
# #     height = 400,
# #     title = 'Gender Distribution by Year'
# # )

# # gender_chart

# # %% [markdown]
# # The chart looked better. Finally, we added a hover effect to provide more details for the finalization of our interactive gender distribution plot. A similar approach was applied to build the interactive race distribution plot then.

# # %%
# year_dropdown = alt.binding_select(options = df_3_year['YEAR'].unique(), name = "Year: ")
# year_select = alt.selection_single(fields = ['YEAR'], bind = year_dropdown, name = "Select", value = 2021)

# gender_chart = alt.Chart(df_3_year).transform_fold(
#     fold = ['PER_FEMALE', 'PER_MALE'],
#     as_ = ['Gender', 'Percentage']
# ).transform_calculate(
#     Gender_Label = "datum.Gender=='PER_FEMALE' ? 'Female' : 'Male'"
# ).mark_bar(clip = True).encode(
#     x = alt.X('Gender_Label:N', title = 'Gender'),
#     y = alt.Y('Percentage:Q', title = 'Percentage', scale = alt.Scale(domain = (48, 52))),
#     color = alt.Color('Gender:N', legend = alt.Legend(title = 'Gender', labelExpr = "datum.value=='PER_FEMALE' ? 'Female' : 'Male'"),
#                       scale = alt.Scale(domain = ['PER_FEMALE', 'PER_MALE'])),
#     tooltip = [alt.Tooltip('Percentage:Q', format = '.2f')],
#     size = alt.value(40)
# ).add_selection(
#     year_select
# ).transform_filter(
#     year_select
# ).properties(
#     width = 400,
#     height = 400,
#     title = 'Gender Distribution by Year'
# )

# gender_chart.save('gender.json')

# # %%
# year_dropdown = alt.binding_select(options = df_3_year['YEAR'].unique(), name = "Year")
# year_select = alt.selection_single(fields = ['YEAR'], bind = year_dropdown, name = "Select", value = 2021)

# race_chart = alt.Chart(df_3_year).transform_fold(
#     fold = ['PER_BLACK', 'PER_ASIAN', 'PER_HISP', 'PER_WHITE', 'PER_Multi'],
#     as_ = ['Race', 'Percentage']
# ).transform_calculate(
#     Race_Label = "datum.Race=='PER_BLACK' ? 'Black or African American' : datum.Race=='PER_ASIAN' ? 'Asian or Native Hawaiian/Other Pacific Islander' : datum.Race=='PER_HISP' ? 'Hispanic or Latino' : datum.Race=='PER_WHITE' ? 'White' : 'Multiracial'"
# ).mark_bar().encode(
#     x = alt.X('Race_Label:N', title = 'Race', axis = alt.Axis(labelAngle = 45)),
#     y = alt.Y('Percentage:Q', axis = alt.Axis(title='Percentage')),
#     color = alt.Color('Race:N', legend = alt.Legend(title = 'Race',
#                       labelExpr = "datum.value=='PER_BLACK' ? 'Black or African American' : datum.value=='PER_ASIAN' ? 'Asian or Native Hawaiian/Other Pacific Islander' : datum.value=='PER_HISP' ? 'Hispanic or Latino' : datum.value=='PER_WHITE' ? 'White' : 'Multiracial'"),
#                       scale = alt.Scale(domain = ['PER_BLACK', 'PER_ASIAN', 'PER_HISP', 'PER_WHITE', 'PER_Multi'])),
#     tooltip = [alt.Tooltip('Percentage:Q', format = '.2f')],
#     size = alt.value(40)
# ).add_selection(
#     year_select
# ).transform_filter(
#     year_select
# ).properties(
#     width = 400,
#     height = 400,
#     title = 'Race Distribution by Year'
# )

# race_chart.save('race.json')

# %% [markdown]
# The 2 interactive plots above provide insights into the distribution of genders and races by year from 2021 to 2023. The x-axis of the 2 bar charts is the gender or race type, the y-axis is both the percentage of that gender or race. Both charts are embedded with a dropdown selection of years in the bottom left corner. Viewers can choose a year to see the percentage distribution of students with different genders or races enrolled in that year. If hovering on the bar, detailed percentage data will show. By switching among years, viewers can also see the changes between different years of the gender or race distribution.

# %% [markdown]
# ### 1.2 Race Distribution by New York State Counties

# %%
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][1]
filtered_features = [feature for feature in counties['features'] if feature['properties']['STATE'] == '36']

filtered_geojson = {
    'type': 'FeatureCollection',
    'features': filtered_features
}

state_to_id_mapping = {}
for feature in filtered_features:
    state_to_id_mapping[feature['properties']['NAME'].lower()] = feature['id']

df_2_counts = df_2["COUNTY_NAME"].value_counts().reset_index()
df_2_counts.columns = ['county_name', 'school_count']
df_2_counts['county_name'] = df_2_counts['county_name'].str.lower()
county_to_id_mapping = {}
for feature in filtered_features:
    county_to_id_mapping[feature['properties']['NAME'].lower()] = feature['id']

df_2_counts['id'] = df_2_counts['county_name'].apply(lambda x: county_to_id_mapping.get(x, -1))

if 'nyc central office' in df_2_counts['county_name'].values:
    df_2_counts.loc[df_2_counts['county_name'] == 'nyc central office', 'id'] = '36061'

if 'saint lawrence' in df_2_counts['county_name'].values:
    df_2_counts.loc[df_2_counts['county_name'] == 'saint lawrence', 'id'] = '36089'
max_value = df_2_counts['school_count'].max()

# %%
year_wise_enrollment_data = pd.read_csv('BEDS_Day_Enrollment.csv') #df_1
demographic_data = pd.read_csv('Demographic_Factors.csv')
institutegroupingData = pd.read_csv('Institution_Grouping.csv')
unique_df_2 = df_2[['SCHOOL_NAME', 'COUNTY_NAME']].drop_duplicates()
unique_df_2['SCHOOL_NAME'] = unique_df_2['SCHOOL_NAME'].str.lower()
unique_df_2['COUNTY_NAME'] = unique_df_2['COUNTY_NAME'].str.lower()
year_wise_enrollment_data['ENTITY_NAME'] = year_wise_enrollment_data['ENTITY_NAME'].str.lower()
beds_day_enrollment_df = pd.read_csv('BEDS_Day_Enrollment.csv')
boces_and_n_rc_df = pd.read_csv('BOCES_and_N_RC.csv')

combined_df = pd.merge(beds_day_enrollment_df, boces_and_n_rc_df, on=['ENTITY_CD', 'YEAR'])
combined_demo_df = pd.merge(demographic_data, boces_and_n_rc_df[['ENTITY_CD', 'YEAR', 'COUNTY_NAME']], on=['ENTITY_CD', 'YEAR'])
sum_by_county_df = combined_demo_df.groupby('COUNTY_NAME')[['NUM_ASIAN','NUM_HISP','NUM_WHITE','NUM_BLACK','NUM_SWD']].sum().reset_index()
sum_by_county_df['id'] = sum_by_county_df['COUNTY_NAME'].apply(lambda x: county_to_id_mapping.get(x.lower(), -1))

# %%
for column in sum_by_county_df.columns:
    if column not in ['id', 'COUNTY_NAME']:
        sum_by_county_df[f'log_{column}'] = np.log(sum_by_county_df[column] + 1)  # Adding 1 to avoid log(0) issue

# %%
import plotly.io as pio
pio.renderers.default = 'iframe'

# %% [markdown]
# We aim to create a geographical choropleth map using the Plotly Express (px) library. The map displays aggregated data about the population of white students in different counties in New York State, color-coding them based on the logarithmic value of the number of white students (log_NUM_WHITE).

# %%
fig = px.choropleth(sum_by_county_df, geojson=filtered_geojson, locations='id', color='log_NUM_WHITE',
                    color_continuous_scale="Viridis",
                    range_color=(0, sum_by_county_df['log_NUM_WHITE'].max()),
                    scope="usa",
                    hover_name="COUNTY_NAME",
                    hover_data = "NUM_WHITE"
                   )
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
fig.update_geos(fitbounds="locations")
fig.show()
plot(fig, filename='log_NUM_WHITE.html', auto_open=False)


# %% [markdown]
# We recreate this for black students and asian students as well.

# %%
fig = px.choropleth(sum_by_county_df, geojson=filtered_geojson, locations='id', color='log_NUM_BLACK',
                    color_continuous_scale="Viridis",
                    range_color=(0, sum_by_county_df['log_NUM_BLACK'].max()),
                    scope="usa",
                    hover_name="COUNTY_NAME",
                    hover_data = "NUM_BLACK"
                   )
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
fig.update_geos(fitbounds="locations")
fig.show()
plot(fig, filename='log_NUM_BLACK.html', auto_open=False)

# %%
fig = px.choropleth(sum_by_county_df, geojson=filtered_geojson, locations='id', color='log_NUM_ASIAN',
                    color_continuous_scale="Viridis",
                    range_color=(0, sum_by_county_df['log_NUM_ASIAN'].max()),
                    scope="usa",
                    hover_name="COUNTY_NAME",
                    hover_data = "NUM_ASIAN"
                   )
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
fig.update_geos(fitbounds="locations")
fig.show()
plot(fig, filename='log_NUM_ASIAN.html', auto_open=False)

# %% [markdown]
# The above codes generated us three different plots. So to simplify further and make it more intuitive, we combined this into a function, the parameter to which would we the demography selected from a dropdown given along with the map. The map will be repopulated using the selected demography.

# %%
# import ipywidgets
# def make_plot(selected_type):
#     print(selected_type)
#     fig = None
#     if (selected_type == "NONE"):
#         return
#     fig = px.choropleth(sum_by_county_df, geojson=filtered_geojson, locations='id', color=selected_type,
#                         color_continuous_scale="Viridis",
#                         range_color=(0, sum_by_county_df[selected_type].max()),
#                         scope="usa",
#                         hover_name="COUNTY_NAME",
#                         hover_data = selected_type
#                     )
#     fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
#     fig.update_geos(fitbounds="locations")
#     fig.show()
# density_types = ["NONE","log_NUM_HISP","log_NUM_ASIAN","log_NUM_WHITE"]
# selector = ipywidgets.Select(options=density_types , description='Select Demography')
# ipywidgets.interact(make_plot, selected_type=selector)

# %% [markdown]
# ## Plot Topic 2 - Enrollment

# %% [markdown]
# ### 2.1 Enrollment by County across Years

# %%
# combined_df = pd.merge(df_1, df_2, on=['ENTITY_CD', 'YEAR'])
# grades = [str(g) for g in range(1, 13)]
# melted = combined_df.melt(id_vars=['COUNTY_NAME', 'YEAR'], value_vars=grades, var_name='Grade', value_name='Students')
# aggregated_df = melted.groupby(['COUNTY_NAME', 'YEAR', 'Grade'], as_index=False)['Students'].sum()
# aggregated_df['CountyYear'] = aggregated_df['COUNTY_NAME'] + ' - ' + aggregated_df['YEAR'].astype(str)
# aggregated_df['Grade'] = aggregated_df['Grade'].astype(int)
# aggregated_df = aggregated_df.sort_values(by='Grade')

# # Disable the max rows limit for Altair
# alt.data_transformers.disable_max_rows()

# county_year_dropdown = alt.binding_select(options=sorted(aggregated_df['CountyYear'].unique()), name='Select County and Year: ')
# county_year_select = alt.selection_single(fields=['CountyYear'], bind=county_year_dropdown, value=sorted(aggregated_df['CountyYear'].unique())[0])

# # Bar chart visualization for total enrollment by grade, filtered by the combined county-year selection
# line_chart = alt.Chart(aggregated_df).mark_line(point=True).encode(
#     x=alt.X('YEAR:O', title='Year'), 
#     y=alt.Y('sum(Students):Q', title='Total Enrollment', aggregate='sum'),  
#     color=alt.Color('Grade:N', scale=alt.Scale(scheme='tableau20')), 
#     tooltip=['CountyYear', 'Grade', 'sum(Students):Q'] 
# ).properties(
#     width=800,
#     height=400,
#     title='Enrollment Trends by Grade in Selected County-Year'
# ).add_params(
#     county_year_select
# ).transform_filter(
#     county_year_select
# )

# line_chart

# %% [markdown]
# This interactive line chart is created to visualize enrollment trends across grades for a selected county and year. A dropdown filter allows users to select a specific county-year combination to adjust the chart dynamically. The line chart displays changes in student enrollment per grade over time, enabling users to quickly identify trends and patterns by grade level. But we ended up with a line chart filled with dots instead of lines, so did not convey what we wanted to convey.

# %%
# combined_df = pd.merge(df_1, df_2, on=['ENTITY_CD', 'YEAR'])
# grades = [str(g) for g in range(1, 13)]
# melted = combined_df.melt(id_vars=['COUNTY_NAME', 'YEAR'], value_vars=grades, var_name='Grade', value_name='Students')
# aggregated_df = melted.groupby(['COUNTY_NAME', 'YEAR', 'Grade'], as_index=False)['Students'].sum()
# aggregated_df['CountyYear'] = aggregated_df['COUNTY_NAME'] + ' - ' + aggregated_df['YEAR'].astype(str)
# aggregated_df['Grade'] = aggregated_df['Grade'].astype(int)
# aggregated_df = aggregated_df.sort_values(by='Grade')

# # Disable the max rows limit for Altair
# alt.data_transformers.disable_max_rows()

# county_year_dropdown = alt.binding_select(options=sorted(aggregated_df['CountyYear'].unique()), name='Select County and Year: ')
# county_year_select = alt.selection_single(fields=['CountyYear'], bind=county_year_dropdown, value=sorted(aggregated_df['CountyYear'].unique())[0])

# # Bar chart visualization for total enrollment by grade, filtered by the combined county-year selection
# bar_chart = alt.Chart(aggregated_df).mark_bar().encode(
#     x=alt.X('Grade:O', title='Grade', sort='ascending'), 
#     y=alt.Y('sum(Students):Q', title='Total Enrollment', aggregate='sum'),
#     color=alt.Color('Grade:N', scale=alt.Scale(scheme='tableau20')),
#     tooltip=['CountyYear', 'Grade', 'sum(Students):Q']
# ).properties(
#     width=800,
#     height=400,
#     title='Enrollment Trends by Grade in Selected County-Year'
# ).add_params(
#     county_year_select
# ).transform_filter(
#     county_year_select
# )

# bar_chart.save('enrollment_trends_by_grade.json')

# # %% [markdown]
# # This bar chart visualizes total student enrollment across grades. It provides a dropdown menu to filter the data by a specific county and year, which dynamically adjusts the chart to reflect the selection. The bar chart organizes student enrollment totals per grade level, enabling users to identify grade-wise trends in enrollment for a particular county and year. The tooltip feature provides additional details about the selected data, helping users delve deeper into specific trends.

# # %%


# # %% [markdown]
# # 

# # %%


# # %% [markdown]
# # ## Plot Topic 3 - School Distribution
# # 
# # ### 3.1 School Distribution Across Counties in New York State (NYS) in 2023
# # 
# # We would also like to explore the relationship of school distribution across different NYS counties. From pre-examination, the school counts for each county are quite similar across the 3 years, so we decided to take 2023 as the example to proceed our plot.

# # %%
# df_2_2023 = df_2[df_2['YEAR'] == 2023]

# alt.data_transformers.enable('default', max_rows = None)
# selection = alt.selection_single(encodings = ['x'], empty = 'none')

# chart_ori = alt.Chart(df_2_2023).mark_bar().encode(
#     x = alt.X('COUNTY_NAME', title = 'County Name', axis=alt.Axis(labelAngle=45)),
#     y = alt.Y('count()', title = 'School Count'),
#     color = alt.condition(selection, alt.value('steelblue'), alt.value('lightgray'))
#     ).properties(
#     title = 'YEAR 2023: School Count by New York State (NYS) County',
#     width = 1100,
#     height = 300
# ).add_selection(
#     selection
# )

# text = chart_ori.mark_text(
#     align = 'center',
#     baseline = 'middle',
#     dx = 0,
#     dy = -5
# ).encode(
#     text = alt.condition(selection, 'count()', alt.value(''))
# )

# plot_school = chart_ori + text
# plot_school.save('school_count.json')

# # %% [markdown]
# # The plot above presents the overall distribution of schools by each counties in NYS. The x-axis is the list of NYS counties in alphabetical order, the y-axis is the school count. The default display of all bars are fade out. By clicking on 1 certain bar representing a county's school count, the selected bar will be highlighted as blue and the exact amount of schools in that county will show. This interaction gives more details for the school distribution across NYS counties in 2023.

# # %% [markdown]
# # Beyond the school count display by counties, we also tried to elaborate the interactivity to range selection.

# # %%
# school_counts_per_county = df_2_2023.groupby('COUNTY_NAME')['SCHOOL_NAME'].nunique().reset_index(name='NUM_SCHOOLS')

# select_school_count = alt.selection_interval(encodings=['x'])

# transparent_bar = alt.Chart(pd.DataFrame({'y': [0]})).mark_rect(color='transparent').encode(
#     x=alt.X('NUM_SCHOOLS:Q', scale=alt.Scale(domain=[school_counts_per_county['NUM_SCHOOLS'].min(), school_counts_per_county['NUM_SCHOOLS'].max()])),
#     y=alt.Y('y:Q', scale=alt.Scale(domain=[-0.5, 0.5]))
# ).properties(
#     width=800,
#     height=20
# ).add_selection(
#     select_school_count
# )

# slider = alt.Chart(pd.DataFrame({'y': [0]})).mark_rule(size=5).encode(
#     y='y:Q',
# ).properties(
#     width=800,
#     height=20
# )

# detail_chart = alt.Chart(school_counts_per_county).mark_bar().encode(
#     x='COUNTY_NAME:N',
#     y='NUM_SCHOOLS:Q',
#     color='COUNTY_NAME:N',
#     tooltip=['COUNTY_NAME', 'NUM_SCHOOLS']
# ).properties(
#     width=800,
#     height=300
# ).transform_filter(
#     select_school_count
# )

# combined_slider = alt.layer(transparent_bar, slider)

# detail_chart & combined_slider

# # %% [markdown]
# # This visualization project presents the distribution of schools across counties in New York State (NYS) for the year 2023 and features an interactive slider that allows users to select a specific range of school counts. The main component is a detailed bar chart that displays the number of schools in each county along the x-axis and the counties along the y-axis, with each county distinguished by a unique color for better visual differentiation.
# # 
# # If dragging to create a rectangular on the slider that covers a certain range of school numbers, only counties have schools within that range will be displayed on the plot.

# # %% [markdown]
# # ## Plot Summary
# # 
# # **Summarize the characteristics of the dataset in words: what does it represent, what are the fields/columns/rows, what data types are they, etc.**

# # %% [markdown]
# # The package "Enrollment Dataset" contains 4 datasets inside, with each focuses on an aspect of the enrollment or school and can be joined by corresponding keys. The detailed content of each dataset is listed below (all data type indicated here are raw type from the original datasets):
# #     
# # * "BEDS_Day_Enrollment.csv" - enrollment numbers by grades in each school for 3 years:
# #     
# #     Its sample columns are `ENTITY_NAME` (The name of the entity (district or school)) - object, `YEAR` - int64, `PK` (Total pre-kindergarten enrollment) - int64, `1` (Total enrollment in grade 1) - int64;
# #     
# # * "BOCES_and_N_RC.csv" - category and location information for each school for 3 years:
# #     
# #     Its sample columns are `ENTITY_CD` (12-digit code for public schools) - int64, `DISTRICT_CD` (8-digit code of school district) - int64, `COUNTY_NAME` (The name of the county) - object, `NEEDS_INDEX` (Need to Resource Capacity Category) - int64;
# #     
# # * "Demographic_Factors.csv" - demographic information for each school for 3 years:
# #     
# #     Its sample columns are `NUM_FEMALE` (Number of female students (K-12)) - int64, `PER_MALE` (Percent of male students (K-12)) - int64, `NUM_WHITE` (Number of White students (K-12)) - int64, `PER_SWD` (Percent of students with disabilities (K-12)) - int64;
# #     
# # * "Institution_Grouping.csv" - group information for each school:
# #     
# #      Its sample columns are `GROUP_CODE` (Aggregation group code) - int64, `GROUP_NAME` (Aggregation group name) - object.


