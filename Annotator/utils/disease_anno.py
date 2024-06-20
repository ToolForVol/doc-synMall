from util import _merge



def _4_panthogenic(df, folder_name):
    print('=' * 30, )
    print(f'[Info]开始注释 【4-疾病信息】...')
    anno4_dir = '../../Homo Sapiens/4-Disease_Information/'
    
    _merge('4.1 处理HGMD-2023.3...', df, \
        f'{anno4_dir}HGMD.txt',\
        folder_name, '4.1-HGMD_Result.tsv')


    _merge('4.2 处理ClinVar-0611...', df, \
        f'{anno4_dir}ClinVar.txt',\
        folder_name, '4.2-ClinVar_Result.tsv')


    _merge('4.3 处理COSMICv100...', df, \
        f'{anno4_dir}COSMIC_v100.txt',\
        folder_name, '4.3-COSMICv100_Result.tsv')

    _merge('4.4 处理GWAS catalog...', df, \
        f'{anno4_dir}GWAS_catalogue.txt',\
        folder_name, '4.4-GWAS_Result.tsv')


    _merge('4.5 处理GRASPv2...', df, \
        f'{anno4_dir}GRASP_v2.txt',\
        folder_name, '4.5-GRASP_Result.tsv')


    _merge('4.6 处理DisGenet...', df, \
        f'{anno4_dir}DisGenet.txt',\
        folder_name, '4.6-DisGenet_Result.tsv')


    _merge('4.7 处理ClinGen...', df, \
        f'{anno4_dir}ClinGen.txt',\
        folder_name, '4.7-ClinGen_Result.tsv')

    _merge('4.8 处理VaiSNP...', df, \
        f'{anno4_dir}VariSNP.txt',\
        folder_name, '4.8-VariSNP_Result.tsv')

    _merge('4.9 处理dbDSM v2...', df, \
            f'{anno4_dir}dbDSM_v2.txt',\
            folder_name, '4.9-dbDSM_Result.tsv')

    _merge('4.10 处理PharmGKB_突变-药物-表型-功能分析...', df, \
        f'{anno4_dir}PharmGKB_Fa_Drug_Pheno.txt',\
        folder_name, '4.10-PharmGKB_Fa_Drug_Pheno_Result.tsv')
    
    _merge('4.11 处理PharmGKB_突变-基因-药物-疾病关联关系...', df, \
        f'{anno4_dir}PharmGKB_relationship.txt',\
        folder_name, '4.11-PharmGKB_relationship_Result.tsv')

    _merge('4.12 处理PharmGKB_突变-临床...', df, \
        f'{anno4_dir}PharmGKB_Clinical_Variant.txt',\
        folder_name, '4.12-PharmGKB_Clinical_Variant_Result.tsv')

    _merge('4.13 处理PharmGKB_突变...', df, \
        f'{anno4_dir}PharmGKB_Variant.txt',\
        folder_name, '4.13-PharmGKB_Variant_Result.tsv')


