from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embed_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
)

vectorstores = []
for i in range(3):
    vcst = FAISS.load_local(f"C:\\Users\\TUF_12500H\\Desktop\\LawDiff\\applied\\vectordb{i}.bin", embed_model, allow_dangerous_deserialization=True)
    vectorstores.append(vcst)

legal_docs = ["กฎกระทรวงยกเว้นค่าธรรมเนียมการใช้ยานยนตร์บนทางหลวงพิเศษหมายเลข 7 และทางหลวงพิเศษหมายเลข 9 ภายในระยะเวลาที่กำหนด พ.ศ. 2567",
              "พระราชบัญญัติ  กำหนดค่าธรรมเนียมการใช้ยานยนตร์บนทางหลวงและสะพาน  พ.ศ. ๒๔๙๗",
              "พระราชบัญญัติว่าด้วยการปรับเป็นพินัย พ.ศ. 2565"]

def retrieve(question):
    response = []
    for i in range(len(vectorstores)):
        contents = []
        queries = vectorstores[i].similarity_search_with_relevance_scores(question, k=5)
        for query in queries:
            content, score = query
            if score > 0.25:
                contents.append(content.page_content)
        
        args = {
            "docs": legal_docs[i],
            "context": contents
        }

        response.append(args)
    
    return response
        