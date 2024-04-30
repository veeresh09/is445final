---
layout: post
title:  "Final Project Presentation"
---

# Introduction

**Name:** Enrollment Database

**Source:** New York State Education Department (NYSED)

**Overview:** 4 datasets inside the package, each focuses on an aspect of the enrollment and can be joined by corresponding keys

**Time:** 2021 to 2023

**Details:**

- `BEDS Day Enrollment.csv` - enrollment numbers by grades in each school for 3 years;
- `BOCES and N:RC.csv` - category and location information for each school for 3 years;
- `Demographic Factors.csv` - demographic information for each school for 3 years;
- `Institution Grouping.csv` - group information for each school;

**Audience:** The potential audience could include education policymakers, school administrators, researchers, and analysts interested in understanding enrollment trends, demographic factors, and institutional groupings within New York State schools.


## Plot Topic 1 - Demographic

**Gender Dsitribution**

`Description`: Explore the distribution of genders by year via these interactive graphs. The bar chart is embedded with a dropdown selection of years, enabling the review of the proportion of male and female students enrolled in each year.
<iframe src="https://youpeng0630.github.io/445final/gender.html" width="100%" height="600"></iframe>


**Race Dsitribution**

`Description`: Explore the distribution of races by year via these interactive graphs.

**Plot 1**

`Description`：The bar chart is embedded with a dropdown selection of years, enabling the review of the proportion of students enrolled in different races in each year.
<iframe src="https://youpeng0630.github.io/445final/race.html" width="100%" height="600"></iframe>

**Plot 2**

`Description`：This plot provides a visual representation of the demographic distribution of students across various regions of the county. The data is segmented into several key demographic factors including age, ethnicity, and economic status. The visualization is designed to highlight areas with high concentrations of diverse populations and identify potential disparities in educational resource allocation.
<iframe src="https://youpeng0630.github.io/445final/log_NUM_BLACK.html" width="100%" height="600"></iframe>
<iframe src="https://youpeng0630.github.io/445final/log_NUM_ASIAN.html" width="100%" height="600"></iframe>
<iframe src="https://youpeng0630.github.io/445final/log_NUM_WHITE.html" width="100%" height="600"></iframe>


## Plot Topic 2 - Enrollment

**Enrollment by County across Years**

`Description`: This bar chart represents an interactive visualization detailing enrollment trends by grade across different counties and years. It utilizes Altair to create a bar chart that displays the total number of students enrolled in each grade from 1 to 12. Users can interact with the visualization through a dropdown menu that combines both county and year into a single filter, allowing for dynamic and specific querying of enrollment data. Each bar represents a grade, and its height indicates the total student enrollment for that grade, as filtered by the selected county-year combination.
<iframe src="https://youpeng0630.github.io/445final/enrollment_trends_by_grade.html" width="100%" height="600"></iframe>

## Plot Topic 3 - School Distribution

**School Distribution Across Counties in New York City**

`Description`: Explore the distribution of schools across various counties in New York City via these interactive graphs.

**Plot 1**

The plot presents the overall distribution of schools by each counties in New York State, By clicking, the selected bar (i.e. a county) will be highlighted and the exact amount of schools in that county will show. This interaction gives more details for the distribution.
<iframe src="https://youpeng0630.github.io/445final/school_count.html" width="160%" height="500"></iframe>

**Plot 2**

More specifically, the slider enables the selection of the desired number of schools to display, and only counties meeting that criteria will be highlighted on the map. Discover the concentration of educational institutions in different areas of the city at a glance.
<iframe src="https://youpeng0630.github.io/445final/youpeng.html" width="150%" height="600"></iframe>


[jekyll-docs]: https://jekyllrb.com/docs/home


---