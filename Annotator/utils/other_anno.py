from util import _merge
import sys
sys.path.append('../_bkp/')


def _7_other(df, folder_name):
    print('=' * 30)
    print(f'[Info]开始注释 【7-其他信息】...')
    anno_dir="../../Homo Sapiens/7-Other/"
    _merge('7.1 处理Mappbility...', df, \
        f'{anno_dir}Mappability.txt',\
        folder_name, '7.1-Mappability_Result.tsv')
    _merge('7.2 处理Local_nuclear_diveristy...', df, \
        f'{anno_dir}Local_Nuclear_Diveristy.txt',\
        folder_name, '7.2-Local_nuclear_diveristy_Result.tsv')
    _merge('7.3 处理Mutation density...', df, \
        f'{anno_dir}Mutation_Density.txt',\
        folder_name, '7.3-Mutation_density_Result.tsv')

