
#Copyright (c) 2018 Copyright Holder All Rights Reserved.
Line_Count=0
path=r'C:\\Users\\apatkal\\Desktop\\Aflac\\DBO to Migrate _Migration.docx'
f=open(path,'r')
#with open(path,'r') as f:
for i in f:
        line_Count=line_Count+1
        print(line_Count)
