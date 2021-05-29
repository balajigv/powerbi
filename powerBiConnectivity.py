#!/usr/bin/env python
# coding: utf-8

# In[3]:


from powerbiclient import Report, models
from powerbiclient.authentication import MasterUserAuthentication
user_name = "Your PowerBI Username"
pwd = "Your PowerBI password"
auth = MasterUserAuthentication(username=user_name, password=pwd)

report = Report(group_id="7dba7cca-9d80-41a8-81af-3a50babc92f6", report_id="9aed5949-33a6-415a-82ff-ccd6888a5528", auth=auth)
report #embed report by calling this. This is critical and should not be ignored

#Get list of report pages
report_pages=report.get_pages()
for report_page in report_pages:
    print(f"Page_id: {report_page['name']}, Page_Name: {report_page['displayName']}")

#Access vizzes present in a specific report page
report_page_id = "ReportSectionf5832aa68571e3831034"
report_visuals=report.visuals_on_page(report_page_id)
for report_visual in report_visuals:
    #all vizes would not have title enabled, so wrap in a try except clause
    try:
        title = report_visual['title']
    except:
        title = None
        
    print(f"Visual ID: {report_visual['name']}, Visualization Type:{report_visual['type']}, Title: {title}")


#Export data in a Viz. Lets try for a sample Viz
visualization_id = "41d516df3a002d0e33c2"
viz_data=report.export_visual_data(report_page_id,visualization_id, rows=20)
print(viz_data)



