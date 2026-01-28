from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()

# 1. 读取本地文档
documents = SimpleDirectoryReader("data").load_data()

# 2. 配置免费的嵌入模型（HuggingFace）
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# 3. 构建向量索引
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# 4. 配置免费的LLM（Ollama本地模型）
llm = Ollama(model="llama2", base_url="http://localhost:11434")

# 5. 创建查询引擎
query_engine = index.as_query_engine(llm=llm)

# 6. 提问
reponse = query_engine.query("yoalucn是谁")

print(reponse)