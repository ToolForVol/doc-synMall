import sys
import os
import pandas as pd
import sys
sys.path.append('../_bkp/')
from util import _merge, retrieve_variant
from datetime import datetime


def _preprocess(args):
	print(f'[Info]正在读取文件...')
	df = pd.read_csv(f'{args.input}', sep='\t')
	print(f'[Info]识别文件{len(df)}行')
	df.drop_duplicates(inplace=True)
	print(f'[Info]去除（可能的）冗余数据，剩余{len(df)}行')


	print(f'[Info]正在导入synMall...')
	syn_df = pd.read_csv('../../Homo Sapiens/0-SNV/synMall_SNV_all.txt', sep='\t', usecols=['Variant19', 'Variant38'])
	try:
		df['vid'] = retrieve_variant(df, '#CHROM', 'POS', 'REF', 'ALT')
	except KeyError:
		print('[Error] 检测到不符合的键，请检查输入表头或文件格式')
		exit()

	if args.genome == 'hg38':
		vid_38 = syn_df['Variant38'].tolist()
		df = df[df['vid'].isin(vid_38)]
		print(f'[Info]输入文件共有{len(df)}记录匹配synMall')
		df.rename(columns={'vid': 'vid_38'}, inplace=True)
	else:
		df = df.merge(syn_df, how='left', left_on='vid', right_on='Variant19', suffixes=('', '_map'))
		v19_count = df['Variant19'].notna().sum()
		v38_count = df['Variant38'].notna().sum()
		print(f'[Info]输入文件共有{v19_count}记录匹配synMall')
		print(f'[Info]转为hg38后，剩余{v38_count}记录')
		df.drop('Variant19', axis=1, inplace=True)
		df = df[df['Variant38'].notna()]
		df.rename(columns={'vid': 'vid_19', 'Variant38': 'vid_38'}, inplace=True)
	print(f'[Info]预处理完毕')

	current_time = datetime.now().strftime("%Y%m%d_%H_%M")
	folder_name = f"user_output/{args.jobname}_{current_time}"
	os.makedirs(folder_name)
	print(f"[Attention]你的注释结果会存储在{folder_name}目录下")
	return df, folder_name

