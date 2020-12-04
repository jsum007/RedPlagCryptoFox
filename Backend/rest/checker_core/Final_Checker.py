from .basic_checker1 import compare
#from checker_core.code2 import *
import os
import pandas as pd
import tarfile
import zipfile
import shutil

def folder_compare(dir_path):
	cppfiles=[]
	filenames=[]
	sim_mat=[]
	for file in os.listdir(dir_path):
		if file.endswith(".cpp"):
			cppfiles.append(os.path.join(dir_path, file))
			filenames.append(file)
	for file1 in cppfiles:
		temp=[]
		for file2 in cppfiles:
			temp.append(compare(file1,file2))
		sim_mat.append(temp)

	df = pd.DataFrame(sim_mat, index= filenames, columns=filenames)
	return df

#print(folder_compare('./samples'))


def saveres(inpath, outpath):
	folder_compare(inpath).to_csv(outpath)

#saveres('./samples','./sample/results/results.csv')

def extract_files(infile):
	if infile.endswith(".zip"):
		filename= os.path.splitext(os.path.basename(infile))[0]
	if infile.endswith(".tar"):
		filename= os.path.splitext(os.path.basename(infile))[0]
	if infile.endswith(".tar.gz"):
		filename= os.path.splitext(os.path.splitext(os.path.basename(infile))[0])[0]

	dirname1= os.path.dirname(infile)
	out_dir= os.path.join(dirname1, filename)

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
			saveres(files_dir, os.path.join(res_dir, 'results.csv'))
			return 'success' , res_dir
		except:
			return 'fail' , ''
	return 'fail', ''





#print(RunCheck('./samples.tar.gz'))

