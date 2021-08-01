#!usr/bin/env python

#DATE: 2021-08-01
#This script was used to extract the GWAS summary statistics from VCF file downloaded from the IEU GWAS database
#URL: https://gwas.mrcieu.ac.uk/datasets/ieu-b-94/


import os

os.getcwd()

#f1 = open("test_p_trans.txt","r+")
f1 = open("GWAS_oral_cancer_for_analysis.final","r+")
f2 = open("GWAS_oral_cancar_for_analysis_final_log_transtop.txt","w+")

#data =[]
for line in f1:
    dd = line.strip().split()
    x=float(dd[8])
    dd[8]=str(10**(-x))
    anno = "\t".join(dd)+"\n"
    f2.write(anno)
#f1=open("F:\\Desktop\\test_p_trans.txt",'r+')
#f2=open("F:\\Desktop\\test_p_trans_2.txt",'w+')
