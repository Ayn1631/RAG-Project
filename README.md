# RAG-Project

一个基于检索增强生成（Retrieval-Augmented Generation）的项目，支持多种召回策略和重排序机制，适用于构建智能问答系统和知识库检索应用。

## 项目架构
```markdown
RAG-Project/
├── RAG/                    # 核心模块
│   ├── Multi_Recall/      # 多路召回模块
│   │   ├── BM25.py        # BM25关键词召回
│   │   └── Cosine_Similarity.py  # 语义相似度召回
│   ├── Reranker/          # 重排序模块
│   │   ├── Reranker_API.py # API方式重排序
│   │   └── Reranker_Model.py # 模型方式重排序
│   ├── Retriever.py       # 检索器核心逻辑
│   └── __init__.py        # 包初始化文件
├── config.py              # 配置文件
└── README.md              # 项目说明文件
```

## 核心功能

### 1. 多路召回机制（Multi-Recall）
- **BM25召回**：基于关键词的传统信息检索算法，支持中英文分词
- **语义相似度召回**：基于向量嵌入的语义检索，支持余弦相似度计算(并保留召回上下文信息)
- 可灵活配置和扩展不同的召回策略

### 2. 嵌入模型支持
- **本地模型**：支持HuggingFace Transformers模型（如BAAI/bge系列）
- **API调用**：支持通过API方式调用嵌入服务
- 自动处理文本预处理和批处理推理

### 3. 重排序机制（Reranker）
- **模型重排序**：使用专用重排序模型提升检索结果相关性
- **API重排序**：支持通过API调用重排序服务
- 对初步检索结果进行精排，提高最终结果质量

### 4. 灵活配置
- 通过[config.py](file://d:\Mypower\Git\MyPython\MyProject\RAG-Project\config.py)统一管理所有配置项
- 支持本地模型和云端API两种部署方式
- 模块化设计，易于扩展新的召回和重排序方法

## 主要优点

### 1. 模块化设计
- 检索器（Retriever）和重排序器（Reranker）分离设计
- 召回策略可插拔，支持多种算法组合使用
- 易于扩展新的召回方法和重排序算法

### 2. 多策略融合
- 结合关键词检索和语义检索的优势
- 通过多路召回提高检索覆盖率
- 重排序机制进一步优化结果相关性

### 3. 灵活部署
- 支持本地模型部署（适合数据安全性要求高的场景）
- 支持API调用（适合快速部署和资源受限环境）
- 可根据需求灵活选择部署方式

### 4. 高性能处理
- 批处理优化，提高嵌入计算效率
- 支持GPU加速（CUDA）
- 向量化存储和检索，提高查询效率

### 5. 易用性
- 统一接口设计，简化使用流程
- 详细的配置说明和示例
- 完善的日志记录和错误处理

## 使用场景

- 智能问答系统
- 知识库检索
- 文档搜索
- 聊天机器人
- 企业知识管理

## 安装与配置

1. 安装依赖包：
```bash
pip install -r requests  # requests库用于API请求
```
以下为可选:
```python
torch transformers  # 当你使用 本地模型 时应该安装
rank_bm25 jieba  # 当你使用 BM25 时应该安装
```

2. 配置环境：
```bash
根据需要修改config.py中的配置项
```
3. 快速开始
```python
from RAG import RAG
from config import RAG_CONFIG

# 创建RAG实例
rag = RAG(RAG_CONFIG)

# 添加文档
rag.add(['文档1内容', '文档2内容', '文档3内容'])

# 查询
results = rag.req('查询问题', top_k=5)
print(results)
```

## 拓展
**如果你想添加新的召回算法**, 请详看以下内容
1.实现对应类
在RAG/Multi_Recall下构建一个*召回算法.py*文件
请实现一个类继承Multi_Recall.Retriever，保证类名与文件名一致. 并实现所有抽象方法, 保证输入与输出一致.

2.在config中注册
```python
RAG_CONFIG = {
    ## 多路召回选择
    "Multi_Recall":{
        'BM25': {
            'lan': 'zh'  # ['zh', 'en']  语言选择
        },
        "你的召回算法的文件名":{
            '你召回算法的类初始化需要的参数字典'
        }
    },
    'Reranker': {
        # 'reranker_func': 
        # 'reranker_kwds': 
    }
}
```

## PR
欢迎各位提交PR或lssues!