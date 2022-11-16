import glob
import shutil
import os
import time
from zipfile import ZipFile

postFixes = [1,2,3]
source_path = '../source/*'

while True:  
    source_obj = glob.glob(source_path)
    # print(source_obj)
    if len(source_obj)>0:
        
        for obj in source_obj:
            name,format = obj.split('\\')[1].split('.')
            zip_file = ZipFile('output.zip','w')
            shutil.copy(obj,'.') 
            tmp_file = open(name+'.'+format,'r')
            content = tmp_file.readlines()
            # print(content)
            tmp_file.close()
            for postfix in postFixes:
                output_tmp = open(name+'_'+str(postfix)+'.'+format, 'a+')  
                # new_file = open('../destination/'+name+'_'+str(postfix)+'.'+format, 'a+')
                # print(f'Creating file with postfix {postfix}')
                count_of_lines = postfix*10
                taking_lines = ''
                for line in range(count_of_lines):
                    # print(f'Creating content for postfix {postfix}')
                    taking_lines+=content[line]
                output_tmp.write(taking_lines)
                output_tmp.close()
                zip_file.write(name+'_'+str(postfix)+'.'+format)
                os.remove(name+'_'+str(postfix)+'.'+format)
            os.remove(obj)
            os.remove(name+'.'+format)
            zip_file.close()   
            output = shutil.copy('output.zip','../destination/')
            os.remove('output.zip')
            output_file = ZipFile(output,'r')
            output_file.extractall('../destination/')
            output_file.close()
            os.remove('../destination/output.zip')
        print('Files are backed up and deleted sources')
    else:
        print('No new file')
    time.sleep(2)