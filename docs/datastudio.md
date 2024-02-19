# DataStudio (Looker Studio) Integration README

## Overview

This README provides a step-by-step guide on integrating and using DataStudio (now known as Looker Studio) for visualizing data stored in BigQuery. Follow the instructions below to prepare your data, create a data source, design a dashboard, and save/share your work.

## Step 1: Prepare Data in BigQuery

Ensure your data is stored in BigQuery with the necessary transformations applied. Confirm the presence of columns like `time` and `traffic` in your dataset.

## Step 2: Create a Data Source in DataStudio

1. Open Google Data Studio.
2. Click on "Create" to start a new report.
3. In the left sidebar, click on "Create" under the "Data Sources" section.
4. Choose "BigQuery" as the connector.
5. Select your project and dataset.
6. Choose the appropriate table ( london_traffic_table).
7. Click on "Connect."

## Step 3: Design Your Dashboard

1. After connecting to the data source, you'll be redirected to the report editor.
2. Add a Time Series chart to the report.
3. Drag the "time" field to the "Date Range" dimension.
4. Drag the "traffic" field to the "Metric" dimension.
5. Customize your chart by adjusting the date range, formatting, and style options.

## Step 4: Save and Share Your Dashboard

1. Click on "File" in the top left corner.
2. Select "Save" to save your dashboard.
3. Optionally, click on "Share" to share your dashboard with others.

## Additional Information

- Make sure to review and adjust the chart properties, styles, and other settings based on your specific visualization needs.
- Explore other visualization options and components available in DataStudio (Looker Studio) to enhance your dashboard.
- Save your work periodically and consider versioning your dashboards if significant changes are made.
