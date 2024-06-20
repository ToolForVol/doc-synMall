from header import print_complex_header


def read_menu():
    menu = {
        'silico': ['CADD', 'DANN', 'Eigen', 'FATHMM-MKL', 'FATHMM-XF', 'CAPICE', 'TraP', 'PhD-SNPg', 'GPN-MSA', 'CScape-somatic', 'CScape',\
        'EnDSM', 'frDSM', 'PrDSM', 'usDSM', 'Syntool', 'SliVA', 'synVep', 'MACIE', 'ReMM', 'FunSeq', 'GenoCanyon', 'FIRE', 'CDTS', 'RegSeq',\
        'SpliceAI', 'ALoFT','LINSIGHT','MMSp', 'dbscSNV', 'TargetScan', 'mirSVR'],
        'cons': ['PhastCons', 'PhyloP', 'bStatistic', 'GERP++', 'Zoonomia', 'siPhy', 'FitCons'],
        'allele': ['gnomAD', 'ExAC', '1000G', 'ESP6500', 'UK10K', 'CG46', 'CG69', 'GME', 'AbraOM', 'NCI-60', 'HRC1', 'TOPMed BRAVO', 'Kaviar', 'Primate'],
        'disease': ['HGMD', 'ClinVar', 'COSMIC', 'DisGenet', 'VariSNP', 'dbDSM', 'GWAS-catalog', 'PharmGKB', 'GRASP'\
        'ClinGen'],
        'epigenetics':['ENCODE', 'chromHMM', 'GTEx_eQTL', 'DICE_eQTL', 'Gene Hancer', 'CAGE Hancer', 'Super Hancer', 'Enhancer Finder',\
        'Geuvadis', 'Transcription Factor', 'ORegAnno', 'miRBase_snoRNA'],
        'denovo':['Gene4Denovo', 'denovo-DB'],
        'other': ['Mappability', 'Local Nuclear Diversity', 'Mutation Density'],
    }
    for key,value in menu.items():
        print_complex_header(key, value)

