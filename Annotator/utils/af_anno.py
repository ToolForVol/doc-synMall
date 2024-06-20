from util import _merge
import sys
sys.path.append('../_bkp/')


def _5_af(df, folder_name):
	print('=' * 30)
	print(f'[Info]开始注释 【5-等位基因信息】...')
	anno5_dir = '../../Homo Sapiens/5-Allele_Frequency/'

	_merge('5.1 处理GME_CG46_CG69_ABRAOM_HRC1_KAVIAR_ESP6500_NCI60_1000Gp3_BRAVO等位基因频率信息...', df, \
		f'{anno5_dir}GME_CG46_CG69_ABRAOM_HRC1_KAVIAR_ESP6500_NCI60_1000Gp3_BRAVO.txt',\
		folder_name, '5.1_GME_CG46_CG69_ABRAOM_HRC1_KAVIAR_ESP6500_NCI60_1000Gp3_BRAVO_Result.tsv')

	_merge('5.2 处理gnomAD v4外显子、基因组测序等位基因频率信息...', df, \
		f'{anno5_dir}gnomAD_v4.txt',\
	 	folder_name, '5.2_gnomAD_v4_Result.tsv')

	_merge('5.3 处理UK10K等位基因频率信息...', df, \
		f'{anno5_dir}UK10K.txt',\
	 	folder_name, '5.3_UK10K_Result.tsv')

	_merge('5.4 处理ExAC等位基因频率信息...', df, \
		f'{anno5_dir}ExAC.txt',\
	 	folder_name, '5.4_ExAC_Result.tsv')

	_merge('5.5 处理五种灵长类动物AF信息...', df, \
		f'{anno5_dir}Primate.txt',\
	 	folder_name, '5.5_Primate_Result.tsv')
