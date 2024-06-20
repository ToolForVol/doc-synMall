from util import _merge
import sys
sys.path.append('../_bkp/')


def _1_computation(df, folder_name):
	print('=' * 30)
	print(f'[Info]开始注释 【1-计算分数】...')
	anno1_dir = '../../Homo Sapiens/1-Computational_Prediction/'
	_merge('1.1 处理广谱性预测分数...', df, \
		f'{anno1_dir}pan_disease_prediction_integrated.txt',\
	 	folder_name, '1.1-广谱性致病分数_Result.tsv')
	_merge('1.2 处理同义突变特异性预测分数...', df, \
		f'{anno1_dir}sSNV_disease_prediction_integrated.txt',\
	 	folder_name, '1.2-同义突变特异性预测分数_Result.tsv')
	_merge('1.3 处理调控性或功能性预测分数...', df, \
		f'{anno1_dir}regulatory_or_functional_prediction_integrated.txt',\
	 	folder_name, '1.3-调控性或功能性预测分数_Result.tsv')
