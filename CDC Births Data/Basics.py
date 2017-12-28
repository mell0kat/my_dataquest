
# coding: utf-8

# ## Calculating Number Births per Month

# In[1]:


file = open("US_births_1994-2003_CDC_NCHS.csv", "r")
file_contents = file.read()
file_lines = file_contents.split("\n")
file_lines[0:10]


# In[6]:


def read_csv(file_name):
    file = open(file_name, "r")
    file_contents = file.read()
    file_lines = file_contents.split("\n")
    string_list = file_lines[1: len(file_lines)]
    final_list = []
    for row in string_list:
        int_fields = []
        string_fields = row.split(",")
        for item in string_fields:
            int_fields.append(int(item))
        final_list.append(int_fields)
    return final_list
        


# In[5]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0: 10]


# In[7]:


def month_births(rows):
    births_per_month = {}
    for row in rows:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
             births_per_month[month] = births
                
    return births_per_month
    


# In[8]:


cdc_month_births = month_births(cdc_list)
cdc_month_births


# ## Calculating Number Births per Day of Week

# In[12]:


def dow_births(rows):
    births_per_week = {}
    for row in rows:
        week = row[3]
        births = row[4]
        if week in births_per_week:
            births_per_week[week] = births_per_week[week] + births
        else:
             births_per_week[week] = births
                
    return births_per_week


# In[14]:


cdc_dow_births = dow_births(cdc_list)
cdc_dow_births


# ## Writing a generic function to generate counts per specified column

# In[18]:


def calc_counts(data, column):
    births_per_column = {}
    for row in data:
        relevant_item = row[column]
        births = row[4]
        if relevant_item in births_per_column:
            births_per_column[relevant_item] = births_per_column[relevant_item] + births
        else:
             births_per_column[relevant_item] = births
                
    return births_per_column
    


# ## Births per year

# In[19]:


cdc_year_births = calc_counts(cdc_list, 0)
cdc_year_births


# ## Births per month

# In[23]:


cdc_month_births = calc_counts(cdc_list, 1)
cdc_month_births


# ## Births per day of month

# In[21]:


cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dom_births


# ## Births per day of week

# In[22]:


cdc_dow_births = calc_counts(cdc_list, 3)
cdc_dow_births

