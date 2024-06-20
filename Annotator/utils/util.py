import pandas as pd
import sys
sys.path.append('../_bkp/')



def _merge(anno_info, input_df, anno_path,folder_name, save_name):
	print(f'[Info]{anno_info}')
	print(f'[Info]加载数据集...')
	df_anno = pd.read_csv(anno_path, sep='\t', low_memory=False)
	df_anno_result = input_df.merge(df_anno, how='left', left_on='vid_38', right_on='Variant38', suffixes=('', '_map'))
	df_anno_result = df_anno_result.drop(right_on, axis=1)
	print(f'[Attention]处理完毕，保存结果到{folder_name}/{save_name}...')
	df_anno_result.to_csv(f'{folder_name}/{save_name}', sep='\t', index=False)


def retrieve_variant(df, chrom_col, pos_col, ref_col, alt_col, prefix=''):
    variant = [f'{prefix}{chro}_{pos}_{ref}/{alt}' for chro, pos, ref, alt in zip(df[chrom_col], df[pos_col], df[ref_col], df[alt_col])]
    return variant
