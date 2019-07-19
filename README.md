# opioid-web
County and City Reports for Opioid Project

---

## Data Generation

1. Copy any new EMS files in **E:\Data\Mi-EMSIS** and **E:\Data\Washtenaw EMS** to the **E:\alex\EMS\txt** folder and rename the file according to the file format of the other files. The other files do not need to be moved from their original locations

2. From the Start Menu, Open the **Anaconda Prompt** terminal

3. Change directory: `cd /d E:\opioid-utils`

4. Run batch script: `data_processing.bat`

5. The output of this script is written to `E:\opioid-web\static\data`. This should generate five updated **web_*.csv** files used by the Report Generation section.

---

## Report Generation

1. From Start Menu, Open the **Anaconda Prompt** terminal

2. Change directory: `cd /d E:\opioid-web`

3. Start program:`python application.py`

4. Open Chrome Browser. Navigate to **localhost:5000**  

[image of localhost](localhost5000.png)

This should bring you to the home page.

[image of landing page](mainpage.png)

5. Select **date range**, **data source**, and **county or city** from the map
    - **Date Range:** The default range is **2 weeks (14 days)** counting backwards from your access date

      **Custom Range:** select the start date, then the end date. **Click Apply** to use these dates.

    [image of date range](daterange.png)

    - **Data Source:** Toggle amongst 3 data sources: **EMS**, **ME**, and **ED**

    [image of data source](datasource.png)

    - **County or City:** There are two options for selecting a county or city — through the map and through the autocomplete search

        [example of hover and click](hoverandclick1.png)
        [example of hover and click](hoverandclick2.png)

        + **Hover and Click** on a City or County to select from the map.

        OR

        [example of type and select](typeandselect1.png)
        [example of type and select](typeandselect2.png)

        + **Type and Select** a name to select from the search bar. **Click the “Set Location” button to confirm your selection.** Successful selection changes the county/city’s color on the map (see below for example).

        [example of color changed on map](colorchanged.png)

6. Click the **“Generate Report”** button located at the bottom of the page to navigate to the report

[image of generate report](generatereport.png)
