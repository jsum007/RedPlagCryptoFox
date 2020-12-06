from .fingerprint import plagCheck
#from checker_core.code2 import *
import os
import pandas as pd
import tarfile
import zipfile
import shutil
import matplotlib.pyplot as plt
import numpy as np


def folder_compare(dir_path):
	kval=55
	cppfiles=[]
	filenames=[]
	sim_mat=[]
	for path, subdirs, files in os.walk(dir_path):
		for file in files:
			if file.endswith(".cpp"):
				cppfiles.append(os.path.join(path, file))
				filenames.append(file)
	for file1 in cppfiles:
		temp=[]
		for file2 in cppfiles:
			temp.append(plagCheck(file1,file2, kval))
		sim_mat.append(temp)

	return sim_mat, filenames

#print(folder_compare('./samples'))


def saveres(inpath, outpath):
	#folder_compare(inpath).to_csv(outpath)

	matres, filenames=folder_compare(inpath)
	extentt=np.arange(len(filenames)) + 0.5

	df = pd.DataFrame(matres, index= filenames, columns=filenames)

	df.to_csv(os.path.join(outpath, 'results.csv'))

	'''corr = df.corr()
	corr.style.background_gradient(cmap='coolwarm')'''



	fig, ax = plt.subplots(1,1)

	img = ax.imshow(matres,cmap='Reds', extent=[0, len(filenames), 0, len(filenames)])

	ax.set_xticks(extentt)
	ax.set_yticks(extentt)	

	ax.set_xticklabels(filenames, rotation= 60)
	ax.set_yticklabels(filenames[::-1])

	fig.colorbar(img)
	plt.tight_layout()
	plt.savefig(os.path.join(outpath, 'results.png'))

#saveres('./samples','./sample/results/results.csv')

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
	#temp1=os.listdir(dirname1)
	#print(out_dir)
	if infile.endswith(".zip"):
		with zipfile.ZipFile(infile, 'r') as zip_ref:
			zip_ref.extractall(os.path.join(out_dir, 'input_files'))

	if tarfile.is_tarfile(infile):
		tf=tarfile.open(infile)
		tf.extractall(os.path.join(out_dir, 'input_files'))
	temp=os.listdir(out_dir)
	temp_dir= temp[0]
	return out_dir, os.path.join(out_dir,temp_dir)



def RunCheck(infile):
	formats=(".tar", ".tar.gz", ".zip")

	if infile.endswith(formats):
		try:
			out_dir , files_dir = extract_files(infile)
			res_dir= os.path.join(out_dir, 'results')
			os.mkdir(res_dir)
			saveres(files_dir, res_dir)
			return 'success' , res_dir
		except:
			return 'fail' , ''
	return 'fail', ''





#print(RunCheck('./samples.tar.gz'))

