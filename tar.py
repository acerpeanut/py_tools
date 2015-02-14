#!/usr/bin/env python

import os
import sys
import time

skip_file = ['tar_pack','tar.py','tarLog.txt','_config']
origin_dir = r"C:\Users\Administrator\Desktop"

os.chdir(origin_dir)
tar_dir = "tar_pack"
log_file_name = "tarLog.txt"

def log(*tmpstr):
	#return
	log_file = file(log_file_name,'a')
	for i in tmpstr:
		if str(type(i)) == str(list):
			print('list')
			for j in i:
				log_file.write(str(j))
		elif str(type(i)) == str(str):
			print('str')
			log_file.write(i)
		else:
			log_file.write(str(i))
		log_file.write('\n')
	log_file.close()

def ByPostfix(tmpstr):
        a = tmpstr.split(".")
        if len(a)>1:
                return a[-1]
        else:
                return ''




def main():
	print(ByPostfix("a"))

	cur_time = time.localtime()
	log('\n')
	log(['*'*10,cur_time.tm_year,'YY ',cur_time.tm_mon,'MM ',cur_time.tm_mday,'DD','*'*10])
	log('\n')
	if not os.path.exists(tar_dir):
		os.mkdir(tar_dir)
		log("mkdir %s" % tar_dir)


	all_file = os.listdir(".")
	log("all_file:", all_file)
	for i in all_file:
		if i not in skip_file:
			det = tar_dir + os.sep + i
			rename_flag = True
			log('rename: %s %s'%(i,tar_dir+os.sep+i))
			if os.path.exists(det):
				try:
					os.remove(det)
				except Exception:
					log("Error: something wrong when remove '%s'" % (det))
					rename_flag = False
			if rename_flag:
				try:
					if os.path.isfile(i) and ByPostfix(i):
						det = tar_dir+os.sep+"postfix"+os.sep+ByPostfix(i)
						if not os.path.exists(det):
							os.mkdir(det)
						det = det + os.sep + i
					os.rename(i,det)
				except Exception:
					log("Error: something wrong when move '%s' to '%s'" % (i, tar_dir+os.sep+i))


if __name__ == "__main__":
	main()
