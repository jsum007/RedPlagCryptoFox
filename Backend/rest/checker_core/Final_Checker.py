#from .fingerprint import plagCheck
#from checker_core.code2 import *
import os
import pandas as pd
import tarfile
import zipfile
import shutil
import matplotlib.pyplot as plt
import numpy as np

from winnowing import winnow
import sys

from .checker_cpp import tokenize_cpp
from .checker_py import tokenize_py
from .checker_java import tokenize_jav
from .backup_checker import backup_tokenize


def plagCheck(fp1,fp2, boilfp=None):

	if boilfp != None:
		tempfp1=set(fp1).difference(boilfp)
		tempfp2 = set(fp2).difference(boilfp)
	else:
		tempfp1 = set(fp1)
		tempfp2 = set(fp2)
	comfpr=list(tempfp1 & tempfp2)	

	deno = min(len(tempfp1),len(tempfp2))

	if deno ==0:
		ratio =1.0
	else:
		ratio= len(comfpr)/deno

	return ratio

def folder_compare(dir_path, boil_path=None):
	kval=0
	cppfiles=[]
	filenames=[]
	sim_mat=[]
	files_fpr=[]
	boil_fpr=[]
	for path, subdirs, files in os.walk(dir_path):
		for file in files:
			if file.endswith((".cpp", ".py", ".java")) and not file.startswith('.'):
				cppfiles.append(os.path.join(path, file))
				filenames.append(file)

	for file in cppfiles:
		try:
			if file.endswith(".cpp"):
				data1 = tokenize_cpp(file)
			if file.endswith(".py"):
				data1 = tokenize_py(file)
			if file.endswith(".java"):
				data1= tokenize_jav(file)
		except:
			data1 = backup_tokenize(file)

		if file.endswith(".cpp"):
			kval = 20
		if file.endswith(".py"):
			kval = 10
		if file.endswith(".java"):
			kval = 15


		fpr_wpos=[]
		for fprs in winnow(data1, kval):
			fpr_wpos.append(fprs[1])
		files_fpr.append(fpr_wpos)

	if boil_path != None:
		try:
			if boil_path.endswith(".cpp"):
				data_b = tokenize_cpp(boil_path)
			if boil_path.endswith(".py"):
				data_b = tokenize_py(boil_path)
			if boil_path.endswith(".java"):
				data_b = tokenize_py(boil_path)
		except:
			data_b = backup_tokenize(boil_path)

		for fprs in winnow(data1, kval):
			boil_fpr.append(fprs[1])
	if boil_fpr:
		for fpr1 in files_fpr:
			temp=[]
			for fpr2 in files_fpr:
				temp.append(plagCheck(fpr1,fpr2, boil_fpr))
			sim_mat.append(temp)
	else:
		for fpr1 in files_fpr:
			temp=[]
			for fpr2 in files_fpr:
				temp.append(plagCheck(fpr1,fpr2))
			sim_mat.append(temp)

	res_mat = np.array(sim_mat)
	return res_mat, filenames


def saveres(inpath, outpath, boilpath=None):

	if boilpath==None:
		matres, filenames=folder_compare(inpath)
	else:
		matres, filenames=folder_compare(inpath, boilpath)

	extentt=np.arange(len(filenames)) + 0.5

	df = pd.DataFrame(matres, index= filenames, columns=filenames)

	df.to_csv(os.path.join(outpath, 'results.csv'))

	fig, ax = plt.subplots(1,1)

	img = ax.imshow(matres,cmap='Reds', vmin=0, vmax=1, extent=[0, len(filenames), 0, len(filenames)])

	ax.set_xticks(extentt)
	ax.set_yticks(extentt)	

	ax.set_xticklabels(filenames, rotation= 60)
	ax.set_yticklabels(filenames[::-1])

	fig.colorbar(img)
	plt.tight_layout()
	plt.savefig(os.path.join(outpath, 'results.png'))


def extract_files(infile):
	if infile.endswith(".zip"):
		filename= os.path.splitext(os.path.basename(infile))[0]
	if infile.endswith(".tar"):
		filename= os.path.splitext(os.path.basename(infile))[0]
	if infile.endswith(".tar.gz"):
		filename= os.path.splitext(os.path.splitext(os.path.basename(infile))[0])[0]

	dirname1= os.path.dirname(infile)
	out_dir= os.path.join(dirname1, 'comparisons')

	if os.path.exists(out_dir) and os.path.isdir(out_dir):
		shutil.rmtree(out_dir, ignore_errors = False)

	if infile.endswith(".zip"):
		with zipfile.ZipFile(infile, 'r') as zip_ref:
			zip_ref.extractall(os.path.join(out_dir, 'input_files'))

	if tarfile.is_tarfile(infile):
		tf=tarfile.open(infile)
		tf.extractall(os.path.join(out_dir, 'input_files'))
	temp=os.listdir(out_dir)
	temp_dir= temp[0]
	return out_dir, os.path.join(out_dir,temp_dir)



def RunCheck(infile, boilfile=None):
	formats=(".tar", ".tar.gz", ".zip")

	if infile.endswith(formats):
		out_dir , files_dir = extract_files(infile)
		res_dir= os.path.join(out_dir, 'results')
		os.mkdir(res_dir)
		if boilfile==None:
			saveres(files_dir, res_dir)
		else:
			saveres(files_dir, res_dir, boilfile)
		return 'success' , res_dir
		
	return 'fail', ''
