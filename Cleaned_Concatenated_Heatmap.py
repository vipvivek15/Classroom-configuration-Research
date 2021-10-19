#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


#df_green = pd.read_csv("resnetGreenResults.csv", header=None)
#df_STEM = pd.read_csv("resnetSTEMResults.csv", header=None)
import io
df_green = pd.read_csv('resnetGreenResults.csv', header=None)
df_STEM = pd.read_csv('resnetSTEMResults.csv', header=None)


# In[6]:


df_green.head()


# In[7]:


df_STEM.head()


# In[8]:


#getting full text path (value at row 0, column 0)
#10205 = course ID
#CENG 115 Civil Engineering Materials = course name
#Nilsson = teacher
#this is the timestamp: image14-10-17_11-44-59-94.jpg --> Oct 17 2014 (date) at 11:44:59:94 (time)
df_STEM.iloc[0,0]


# In[9]:


#getting full text path (value at row 0, column 0)
#36464 = course ID
# = course name
# = teacher
#this is the timestamp: image14-10-17_11-44-59-94.jpg --> Oct 17 2014 (date) at 11:44:59:94 (time)
df_green.iloc[0,0]


# ## df_STEM cleaning

# In[10]:


#splitting out into CourseID, CourseName, FacultyName, PhotoDate, PhotoTime
for row in df_STEM[0]:
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\photosSTEM\\', '')    .replace('__Artificial', ' Artificial')    .replace('__', '\\').replace('_', '\\').replace('\ ', ' ').replace('  ', ' ').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    print(row)


# In[12]:


#CourseID = row[0]
def getCourseID(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\photosSTEM\\', '')    .replace('__Artificial', ' Artificial')    .replace('__', '\\').replace('_', '\\').replace('\ ', ' ').replace('  ', ' ').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    CourseID = row[0]
    return CourseID


# In[13]:


df_STEM['CourseID'] = df_STEM[0].apply(getCourseID)


# In[14]:


#CourseName = row[1]
def getCourseName(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\photosSTEM\\', '')    .replace('__Artificial', ' Artificial')    .replace('__', '\\').replace('_', '\\').replace('\ ', ' ').replace('  ', ' ').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    CourseName = row[1]
    return CourseName


# In[15]:


df_STEM['CourseName'] = df_STEM[0].apply(getCourseName)


# In[16]:


def getFaculty(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\photosSTEM\\', '')    .replace('__Artificial', ' Artificial')    .replace('__', '\\').replace('_', '\\').replace('\ ', ' ').replace('  ', ' ').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    if len(row) == 5:
        Faculty = row[2]
        return Faculty
    else:
        return None


# In[17]:


df_STEM['FacultyName'] = df_STEM[0].apply(getFaculty)


# In[18]:


def getPhotoDate(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\photosSTEM\\', '')    .replace('__Artificial', ' Artificial')    .replace('__', '\\').replace('_', '\\').replace('\ ', ' ').replace('  ', ' ').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    if len(row) == 5:
        PhotoDate = '20' + row[3]
        return PhotoDate
    else:
        PhotoDate = '20' + row[2]
        return PhotoDate


# In[19]:


df_STEM['PhotoDate'] = df_STEM[0].apply(getPhotoDate)


# In[20]:


def getPhotoTime(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\photosSTEM\\', '')    .replace('__Artificial', ' Artificial')    .replace('__', '\\').replace('_', '\\').replace('\ ', ' ').replace('  ', ' ').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    if len(row) == 5:
        PhotoTimeDash = row[4]
        PhotoTime = PhotoTimeDash.replace('-', ':')
        return PhotoTime
    else:
        PhotoTimeDash = row[3]
        PhotoTime = PhotoTimeDash.replace('-', ':')
        return PhotoTime


# In[21]:


df_STEM['PhotoTime'] = df_STEM[0].apply(getPhotoTime)


# In[22]:


df_STEM.head()


# In[23]:


df_STEM.rename(columns={1: 'ActivityName'}, inplace=True)


# In[24]:


df_STEM.drop(columns={0}, inplace=True)


# In[25]:


df_STEM


# # df_Green Cleaning - Redone

# In[26]:


#splitting out into CourseID, CourseName, FacultyName, PhotoDate, PhotoTime
# 'C:\\Users\\acall\\Documents\\MATLAB\\36464_ENGR_334_Green__COMPLETE\\image16-05-05_17-07-58-95.jpg'
for row in df_green[0]:
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\', '')    .replace('_334', '')    .replace('ENGR', 'ENGR 334').replace('__COMPLETE', '').replace('_', '\\').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    print(row)


# In[27]:


#CourseID = row[0]
def getCourseIDg(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\', '')    .replace('_334', '')    .replace('ENGR', 'ENGR 334').replace('__COMPLETE', '').replace('_', '\\').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    CourseID = row[0]
    return CourseID


# In[28]:


df_green['CourseID'] = df_green[0].apply(getCourseIDg)


# In[29]:


#CourseName = row[1]
def getCourseNameg(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\', '')    .replace('_334', '')    .replace('ENGR', 'ENGR 334').replace('__COMPLETE', '').replace('_', '\\').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    CourseName = row[1]
    return CourseName


# In[30]:


df_green['CourseName'] = df_green[0].apply(getCourseNameg)


# In[31]:


def getFacultyg(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\', '')    .replace('_334', '')    .replace('ENGR', 'ENGR 334').replace('__COMPLETE', '').replace('_', '\\').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    Faculty = row[2]
    return Faculty


# In[32]:


df_green['FacultyName'] = df_green[0].apply(getFacultyg)


# In[33]:


def getPhotoDateg(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\', '')    .replace('_334', '')    .replace('ENGR', 'ENGR 334').replace('__COMPLETE', '').replace('_', '\\').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    PhotoDate = '20' + row[3]
    return PhotoDate


# In[34]:


df_green['PhotoDate'] = df_green[0].apply(getPhotoDateg)


# In[35]:


def getPhotoTimeg(row):
    row = row.replace('C:\\Users\\acall\\Documents\\MATLAB\\', '')    .replace('_334', '')    .replace('ENGR', 'ENGR 334').replace('__COMPLETE', '').replace('_', '\\').replace('image', '').replace('.jpg', '')
    row = row.split('\\')
    PhotoTimeDash = row[4]
    PhotoTime = PhotoTimeDash.replace('-', ':')
    return PhotoTime


# In[36]:


df_green['PhotoTime'] = df_green[0].apply(getPhotoTimeg)


# In[37]:


df_green.head()


# In[38]:


df_green.rename(columns={1: 'ActivityName'}, inplace=True)


# In[39]:


df_green.drop(columns={0}, inplace=True)


# In[40]:


df_green


# # Concatenating STEM and Green
# 

# In[41]:


#Attaching Green's course data to the bottom of the main dataframe by concatenating both dataframes
#Note: Index has also been reset - total of 16103 entries in this dataframe
df_combine = pd.concat([df_STEM, df_green], ignore_index=True)
df_combine


# # Heatmap

# In[42]:


df_combine['ActivityName'].unique()
#add a new column assigning IDs to ActivityNames
df_combine.replace({'ActivityName':{'Empty':0, 'Writing':1, 'Reading':2, 'Lecture':3, 'GroupWork':4, 'Discussion':5}})


# In[43]:


#taking out cross-listings for now so I can properly sum up some stuff
def getCourses(row):
    row = row.split('-')
    row = row[0]
    return(row)


# In[44]:


df_combine['CourseID'] = df_combine['CourseID'].apply(getCourses)


# In[45]:


df_combine


# In[46]:


test = df_combine.groupby(['CourseID', 'PhotoDate', 'ActivityName'])['ActivityName'].size()


# In[47]:


test


# In[53]:


test.unstack().fillna(0)


# In[54]:


course10205 = test.unstack().head(19)


# In[55]:


#heatmap for a single class (per teacher request) by date
sns.heatmap(course10205, annot=True)


# In[56]:


df_combine


# In[103]:


df_alternate = df_combine[::3]
df  = df_alternate.groupby(['CourseID', 'PhotoDate', 'PhotoTime'])['PhotoTime'].size()


# In[106]:


result = df.unstack()
result.dropna()


# In[107]:


sns.heatmap(result,annot=True)

