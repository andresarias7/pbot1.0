from langchain.document_loaders import PyPDFLoader 
from langchain.indexes import VectorstoreIndexCreator
from  dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("ejemplo.pdf")

index = VectorstoreIndexCreator().from_loaders([loader])

query ="hacer un resumen de los 5 puntos mas importantes"

print(index.query(query))