# -*- coding: utf-8 -*-

"""
wget radar ref gif from CMA
@author: qzhang
"""
 
import os
import string
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_img(year_in,month_in,day_in,station_info,path_to_save):
	hr=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
	mi=["00","10","20","30","40","50"]
	se=["00"]
	if station_info[0]=="A":
		image_path="mosaic"
	if station_info[0]=="Z":
		image_path="image"
	for hr_cell in hr:
		hr_str=hr_cell
		for mi_cell in mi:
			mi_str=mi_cell
			for se_cell in se:
				se_str=se_cell
				url_path="http://www.moc.cma.gov.cn/mocimg/radar/"+image_path+"/"+station_info+"/QREF/"+year_in+"/"+month_in+"/"+day_in+"/"+station_info+\
									".QREF000."+year_in+month_in+day_in+"."+hr_str+mi_str+se_str+".GIF"
				save_path=path_to_save+station_info+"/"
				os.system("wget -P "+save_path+" "+url_path)
				flag=year_in+month_in+day_in+hr_str+mi_str
				print flag
	return 0

site_flag=open("/home1/hanbin/wget_radar_image/radar_site.ini","r")
path_to_save="/home1/hanbin/radar_img/"
site_info=site_flag.read().split("\n")
yesterday=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()-86400)).split("-")
record=[]
for site_cell in site_info[:-1]:
	station_info=site_cell
	flag=get_img(yesterday[0],yesterday[1],yesterday[2],station_info,path_to_save)
	if flag==0:
		record+=[station_info+" !!!success!!!"]
	else:
		record+=[station_info+"!!!fail!!!"]
if os.system("tar -cvf  ~/radar_img_"+yesterday[0]+yesterday[1]+yesterday[2]+".tar.gz "+path_to_save):
	record+=["tar file !!!success!!!"]
else:
	record+=["tar file !!!fail!!!"]
if os.system("rm -r "+path_to_save):
	record+=["rm file !!!success!!!"]
else:
	record+=["rm file !!!fail!!!"]
for cell in record:
	print cell
