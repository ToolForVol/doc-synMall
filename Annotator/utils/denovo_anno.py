from util import _merge
import sys
sys.path.append('../_bkp/')


def _6_denovo(df, folder_name):
	print('=' * 30)
	print(f'[Info]开始注释 【6-新生变异信息】...')
	anno6_dir = '../../Homo Sapiens/6-Denovo_variant/'

	_merge('6.1 处理Gene4Denovo...', df, \
		f'{anno6_dir}Gene4Denovo.txt',\
	 	folder_name, '6.1_Gene4Denovo_Result.tsv')

	_merge('6.2 处理denovoDB...', df, \
		f'{anno6_dir}denovo-DB.txt',\
	 	folder_name, '6.2_denovo-DB_Result.tsv')
