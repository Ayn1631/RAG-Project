"""
应用配置文件
包含模型配置、提示词和其他应用设置
⚠警告：除非你知道自己在做什么，否则请不要修改这里的配置
"""
from dotenv import load_dotenv
load_dotenv()
import os

RAG_CONFIG = {
    ## 多路召回选择
    "Multi_Recall":{
        'BM25': {
            'lan': 'zh'  # ['zh', 'en']  语言选择
        },
        "Cosine_Similarity":{
            ## 嵌入选择('Model', 'API')选择其中一个!
            
            'embed_func': 'Model',
            'embed_kwds': {
                'emb_model_name_or_path': 'BAAI/bge-large-zh',  # 模型名称或路径
                'max_len': 512,  # 每段文本最大长度
                'bath_size': 64,  # 批量推理大小
                'device': 'cuda',  # ['cuda', 'cpu']  # 使用cuda或cpu进行推理
            },
            
            # 'embed_func': 'API',
            # 'embed_kwds': {
            #     'base_url': 'https://api.siliconflow.cn/v1',  # 嵌入模型的url地址
            #     'api_key': os.getenv('sil_key'),
            #     'model': 'BAAI/bge-m3'
            # },
            
            'vector_dim': 1024,  # 嵌入维度(必须和嵌入模型的输出维度一样! 默认bge是1024, 不用调!)
        }
    },
    'Reranker': {
        # 'reranker_func': 'Model',  # Choice ['Model', 'API']
        # 'reranker_kwds': {
        #     'rerank_model_name_or_path': 'BAAI/bge-reranker-large',
        #     'device': 'cuda'
        # }
        
        'reranker_func': 'API',
        'reranker_kwds': {
            'base_url': 'https://api.siliconflow.cn/v1/',
            'api_key': os.getenv('sil_key'),
            'model': 'netease-youdao/bce-reranker-base_v1'
        }
    }
    
}