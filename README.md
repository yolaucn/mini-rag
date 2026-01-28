# Mini RAG

一个基于 LlamaIndex 的轻量级检索增强生成（RAG）系统，支持本地文档查询和智能问答。

## 功能特性

- 📚 **本地文档处理**: 自动读取和索引本地文档
- 🔍 **智能检索**: 基于向量相似度的文档检索
- 🤖 **本地LLM支持**: 集成 Ollama 本地大语言模型
- 🆓 **免费嵌入模型**: 使用 HuggingFace 的免费嵌入模型
- ⚡ **轻量级设计**: 最小化依赖，快速部署

## 技术栈

- **LlamaIndex**: 核心RAG框架
- **Ollama**: 本地LLM服务
- **HuggingFace Embeddings**: 文档向量化
- **Python 3.13+**: 开发语言

## 快速开始

### 环境要求

- Python 3.13+
- Ollama (用于本地LLM)

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/yolaucn/mini-rag
   cd mini-rag
   ```

2. **安装依赖**
   ```bash
   # 使用 uv (推荐)
   uv sync
   
   # 或使用 pip
   pip install -r requirements.txt
   ```

3. **安装并配置 Ollama**
   ```bash
   # 安装 Ollama
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # 下载 llama2 模型
   ollama pull llama2
   
   # 启动 Ollama 服务
   ollama serve
   ```

4. **准备数据**
   
   将你的文档文件放入 `data/` 目录中。项目支持多种格式的文档。

5. **配置环境变量**
   
   复制 `.env.example` 到 `.env` 并配置必要的环境变量（如果需要）。

### 使用方法

**基础使用**:
```bash
python demo.py
```

**自定义查询**:
```python
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()

# 读取文档
documents = SimpleDirectoryReader("data").load_data()

# 配置嵌入模型
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# 构建索引
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# 配置LLM
llm = Ollama(model="llama2", base_url="http://localhost:11434")

# 创建查询引擎
query_engine = index.as_query_engine(llm=llm)

# 进行查询
response = query_engine.query("你的问题")
print(response)
```

## 项目结构

```
mini-rag/
├── data/                   # 文档数据目录
│   ├── 个人简介.txt        # 示例文档
│   └── intro.txt          # 示例文档
├── demo.py                # 演示脚本
├── main.py                # 主程序入口
├── pyproject.toml         # 项目配置
├── .env                   # 环境变量配置
└── README.md              # 项目说明
```

## 配置说明

### 嵌入模型

项目默认使用 `BAAI/bge-small-en-v1.5` 作为嵌入模型，这是一个免费且高效的模型。你也可以替换为其他模型：

```python
# 中文优化模型
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5")

# 多语言模型
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

### LLM 配置

支持多种 Ollama 模型：

```python
# 使用不同的模型
llm = Ollama(model="llama3", base_url="http://localhost:11434")
llm = Ollama(model="mistral", base_url="http://localhost:11434")
llm = Ollama(model="qwen", base_url="http://localhost:11434")
```

## 常见问题

**Q: Ollama 连接失败怎么办？**

A: 确保 Ollama 服务正在运行：
```bash
ollama serve
```

**Q: 如何添加新的文档？**

A: 直接将文档文件放入 `data/` 目录，重新运行程序即可自动索引。

**Q: 支持哪些文档格式？**

A: LlamaIndex 支持多种格式，包括 .txt, .pdf, .docx, .md 等。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 致谢

- [LlamaIndex](https://github.com/run-llama/llama_index) - 强大的RAG框架
- [Ollama](https://ollama.ai/) - 本地LLM解决方案
- [HuggingFace](https://huggingface.co/) - 免费的嵌入模型