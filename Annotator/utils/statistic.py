import pandas as pd
import os


def get_sum(df):
	non_null_counts = df.notna().sum()
	result_df = pd.DataFrame(non_null_counts, columns=['FieldName Count'])
	return result_df


def get_sum_snv(df):
	non_null_counts = (df == '-').sum()
	result_df = pd.DataFrame(non_null_counts, columns=['FieldName Count'])
	return result_df


ls = ['1-Computational_Prediction', '2-Conservation_Score',\
	  '3-Epigenetics', '4-Disease_Information', '5-Allele_Frequency',\
	  '6-Denovo_variant', '7-Other']

for item in ls:
	directory = '../database/' + item + '/'
	for root, dirs, files in os.walk(directory):
		for dir in dirs:
			for file in files:
				if file.endswith('txt'):
					path = root + '/' + file
					if not 'bkp' in path:
						print(f"Counting {path}...")
						df = pd.read_csv(f"{path}", sep='\t', low_memory=False)
						result_df = get_sum(df)
						print(result_df)
						result_df.to_csv(f'{root}{file.split(".txt")[0]}_statistic.tsv', sep='\t', index=False)

