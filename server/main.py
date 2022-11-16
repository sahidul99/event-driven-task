'''
    Event driven Object processor
    author @sahidul islam
'''
import glob
import shutil
import os
import time

postFixes = [1,2,3]
source_path = '../source/*'

while True:  
    source_obj = glob.glob(source_path)
    if len(source_obj)>0:
        for obj in source_obj:
            name,format = obj.split('\\')[1].split('.')
            for postfix in postFixes:
                shutil.copy(obj,'../destination/'+name+'_'+str(postfix)+'.'+format)
            os.remove(obj)
        print('Files are backed up and deleted sources')
    else:
        print('No new file')
    time.sleep(10)





# source_path = '../source/*'
# source_path = '../source/*'
# destination_path = '../destination'

# postfix = [1, 2, 3]

# while True:
#     source_object = glob.glob(source_path)
#     # print(source_object)

#     if len(source_object) > 0:

#         object_path = source_object[0]
#         tmp = shutil.copy(object_path, '.')
#         content = open(tmp,'r').read()
        

#         name,format = object_path.split('\\')[-1].split('.')

#         for item in range(len(postfix)):
#             filename = name + '_' + str(item) + '.' + format
#             new_file = open(destination_path+'/'+filename, 'a+')
#             new_file.write(content)

#         os.remove(object_path)
#         os.remove(object_path.split('\\')[-1])
    

