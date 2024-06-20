from util import _merge
import sys
sys.path.append('../_bkp/')


def _3_epigenetics(df, folder_name):
    print('=' * 30)
    print(f'[Info]开始注释 【3-表观遗传学信息】...')
    anno3_dir = '../../Homo Sapiens/3-Epigenetics/'
    
    _merge('3.1 处理ENCODE...', df, \
        f'{anno3_dir}ENCODE.txt',\
        folder_name, '3.1-ENCODE_Result.tsv')

    _merge('3.2 处理chromHMM...', df, \
        f'{anno3_dir}chromHMM.txt',\
        folder_name, '3.2-chromHMM_Result.tsv')

    _merge('3.3 处理GTEx...', df, \
        f'{anno3_dir}/GTEx_v8.txt',\
        folder_name, '3.3-GTEx_Result.tsv')

    _merge('3.4 处理DICE_eQTL...', df, \
        f'{anno3_dir}DICE_eQTL.txt',\
        folder_name, '3.4-DICE_Result.tsv')

    _merge('3.5 处理Gene Hancer...', df, \
        f'{anno3_dir}Gene_Hancer.txt',\
        folder_name, '3.5-gene_hancer_Result.tsv')

    _merge('3.6 处理CAGE Hancer...', df, \
        f'{anno3_dir}cage_enhancer_promoter.txt',\
        folder_name, '3.6-cage_enhancer_promoter_Result.tsv')

    _merge('3.7 处理super Hancer...', df, \
        f'{anno3_dir}Super_Enhancer.txt',\
        folder_name, '3.7-super_enhancer_Result.tsv')
    
    _merge('3.8 处理Geuvadis...', df, \
        f'{anno3_dir}Geuvadis.txt',\
        folder_name, '3.8-Geuvadis_Result.tsv')

    _merge('3.9 处理Transcription Factor...', df, \
        f'{anno3_dir}Transcription_Factor.txt',\
        folder_name, '3.9-Transcription_Factor_Result.tsv')

    _merge('3.10 处理ORegAnno...', df, \
        f'{anno3_dir}ORegAnno.txt',\
        folder_name, '3.10-ORegAnno.tsv')

    _merge('3.11 处理Enhancer Finder...', df, \
        f'{anno3_dir}Enhancer_Finder.txt',\
        folder_name, '3.11-Enhancer_Finder_Result.tsv')

    _merge('3.12 处理snoRNABase_miRBase...', df, \
        f'{anno3_dir}snoRNABase_miRBase.txt',\
        folder_name, '3.12-snoRNABase_miRBase_Result.tsv')

