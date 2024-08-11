from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import FAISS

texts = []

with open(r"C:\Users\TUF_12500H\Desktop\LawDiff\data\กฎกระทรวงยกเว้นค่าธรรมเนียมการใช้ยานยนตร์บนทางหลวงพิเศษหมายเลข 7 และทางหลวงพิเศษหมายเลข 9 ภายในระยะเวลาที่กำหนด พ.ศ. 2567.txt", "r", encoding="utf8") as f:
    text = f.read()
    texts.append(text)

with open(r"C:\Users\TUF_12500H\Desktop\LawDiff\data\พระราชบัญญัติ  กำหนดค่าธรรมเนียมการใช้ยานยนตร์บนทางหลวงและสะพาน  พ.ศ. ๒๔๙๗.txt", "r", encoding="utf8") as f:
    text = f.read()
    texts.append(text)

with open(r"C:\Users\TUF_12500H\Desktop\LawDiff\data\พระราชบัญญัติว่าด้วยการปรับเป็นพินัย พ.ศ. 2565.txt", "r", encoding="utf8") as f:
    text = f.read()
    texts.append(text)

embed_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=256, chunk_overlap=25, separators=["\n\n", "\n"]
)

for i in range(len(texts)):
    docs = []
    doc_splits = text_splitter.split_text(texts[i])
    
    for j in doc_splits:
        docs.append(Document(page_content=j))

    vectorstore = FAISS.from_documents(docs, embed_model)
    vectorstore.save_local(f"C:\\Users\\TUF_12500H\\Desktop\\LawDiff\\applied\\vectordb{i}.bin")