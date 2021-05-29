
import os, time,shutil

trying = input('Enter days limit')
path = input('Enter the path of the file >>> ');
days = int(time.time_ns() * 2.7778e-13 * 0.0416667);




if os.path.exists(path):

   
    files = os.listdir(path);

    
    for docs in files:

        
        name, ext = os.path.splitext(docs)       
        path_of_doc = path + '/' + name + ext
        
        ctime = int(os.stat(path_of_doc).st_ctime_ns * 2.7778e-13 * 0.0416667);

        
        if days - ctime == trying or days > ctime:
            
            print('file name => ' + name, ext);
            print('The file is older than 30 days. do you want to delete it ??');
            print('If you want to delete then type - D');

            delete_input = input('>>> ');
            
            if delete_input == 'D' or delete_input == 'd':
                os.remove(path_of_doc);

            else:
                print('Sorry I could not understand ...');
        
        else:
            print('You have created this recently - ' + name + ext);
        
else:
    print('Please Enter valid path ');