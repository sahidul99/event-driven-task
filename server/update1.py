import glob
import shutil
import os
import time

postFixes = [1,2,3]
source_path = '../source/*'

while True:  
    source_obj = glob.glob(source_path)
    # print(source_obj)
    if len(source_obj)>0:
        for obj in source_obj:
            name,format = obj.split('\\')[1].split('.')
            shutil.copy(obj,'.') 
            tmp_file = open(name+'.'+format,'r')
            content = tmp_file.readlines()
            # print(content)
            tmp_file.close()
            for postfix in postFixes:  
                new_file = open('../destination/'+name+'_'+str(postfix)+'.'+format, 'a+')
                # print(f'Creating file with postfix {postfix}')
                count_of_lines = postfix*10
                taking_lines = ''
                for line in range(count_of_lines):
                    # print(f'Creating content for postfix {postfix}')
                    taking_lines+=content[line]
                new_file.write(taking_lines)
                new_file.close()
            os.remove(obj)
            os.remove(name+'.'+format)
        print('Files are backed up and deleted sources')
    else:
        print('No new file')
    time.sleep(2)