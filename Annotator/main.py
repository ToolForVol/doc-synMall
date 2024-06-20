import pandas as pd
import argparse
import os
import sys
from datetime import datetime

sys.path.append('_bkp/')
sys.path.append('utils/')
from header import print_header, print_complex_header
from menu import read_menu

from preprocess import _preprocess
from silico_anno import _1_computation
from cons_anno import _2_cons
from epi_anno import _3_epigenetics
from disease_anno import _4_panthogenic
from af_anno import _5_af
from denovo_anno import _6_denovo
from other_anno import _7_other
from util import _merge, retrieve_variant


# 映射注释类型到对应的函数
annotation_functions = {
    'silico': _1_computation,
    'cons': _2_cons,
    'allele': _5_af,
    'disease': _4_panthogenic,
    'denovo': _6_denovo,
    'epigenetics': _3_epigenetics,
    'other': _7_other,
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='注释同义突变数据.')
    parser.add_argument('--genome', type=str, help='基因组版本[hg19/hg38]')
    parser.add_argument('--input', type=str, help='输入文件路径')
    parser.add_argument('--jobname', type=str, help='给该注释任务起个名称')
    parser.add_argument('--annotation', type=str, nargs='+', help='[all]/[c_pan]/[s_pan]/[cons]/[allele]/[disease]/[denovo]/[epigenetics]')
    parser.add_argument('--menu', action='store_true', help='展示注释菜单')
    args = parser.parse_args()

    if args.menu:
        read_menu()
        exit()

    if not os.path.isfile(args.input):
        print(f'[Warning] 无法找到 {args.input}，请提供正确的文件路径.')
        exit()

    print_header("synMall Annotator Interface(✿◡‿◡)")
    print('[注意]主程序的gnomADv4的数据只选用了外显子和基因组测序的不同种群、不同性别、以及整体（常用信息）的AF。完整字段（585列）数据需要71GB。')
    print('[注意]所有注释信息基于synVep、FAVOR、CADDv1.7、VEP生成的同义突变并集注释。')
    print('[注意]主程序接受的输入文件格式如下，请确保表头列名至少具有【#CHROM、POS、REF、ALT】且为【制表符分隔】，数据格式相同：')
    show_df = pd.read_csv('_bkp/input.txt', sep='\t')
    print(show_df.head())

    df, folder_name = _preprocess(args)

    if 'all' in args.annotation:
        for func in annotation_functions.values():
            func(df, folder_name)
    else:
        for annotation in args.annotation:
            if annotation in annotation_functions:
                annotation_functions[annotation](df, folder_name)
            else:
                print(f'[Error] 未知的注释类型: {annotation}, 目前只可选择大类，详见--help')

