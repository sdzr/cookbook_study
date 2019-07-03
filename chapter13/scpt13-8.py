# 创建和解包归档文件
# 人员.tar,.tgz,.zip
# 底层模块有tarfile,zipfile,gzip,bz2
# 但是只是解包和归档，则shutil就够了

import shutil
#shutil.make_archive('scpt13-7.py','zip')
#shutil.unpack_archive('scpt13-8.py.zip')

print(shutil.get_archive_formats(),shutil.get_unpack_formats())