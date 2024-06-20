from util import _merge
import sys
sys.path.append('../_bkp/')

def _2_cons(df, folder_name):
	print('=' * 30)
	print(f'[Info]开始注释 【2-保守性分数】...')
	_merge('2 处理保守性分数...', df, \
		f'../../Homo Sapiens/2-Conservation_Score/PhastConsx3_PhyloPx3_bStatistic_Zoonomia_GERP++_FitCons_siPhy_hg38.txt',\
	 	folder_name, '2-保守性分数_Result.tsv')
