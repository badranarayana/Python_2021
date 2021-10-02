import os
import sys

#help(os)

base_path = b"C:\Users\91901\Desktop\stock_feeds"
# path/location of resources
dir_name = b"\my_dir1"

full_path = base_path + dir_name

# another folder
dir_4_name = b"\my_dir_4"

full_path_my_dir_4 = full_path + dir_4_name

dir_5 = b"\my_dir_5_6\can_write"
os.makedirs(full_path_my_dir_4 + dir_5, exist_ok=True)
with open(full_path_my_dir_4 + dir_5 + b"/abc.txt", 'a+') as obj:
    pass

import stat
dir_6 = b"\my_dir_5_6\can_not_write_read_by_owner"
#os.makedirs(full_path_my_dir_4 + dir_6, mode=stat.S_IRUSR, exist_ok=True)

os.chmod(b'C:\Users\91901\Desktop\stock_feeds\my_dir1\my_dir_4\my_dir_5_6\can_not_write_read_by_owner', mode=0o777)
# delete it

os.remove(b'C:\Users\91901\Desktop\stock_feeds\my_dir1\my_dir_4\my_dir_5_6\can_not_write_read_by_owner')






# create dir/folder


# delete dir



# list dir/folder