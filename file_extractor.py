from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, UnstructuredPowerPointLoader, UnstructuredExcelLoader

def extract_text_from_document(file_path):

    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'pdf':
        loader = PyPDFLoader(file_path)
    elif file_extension == 'docx':
        loader = UnstructuredWordDocumentLoader(file_path)
    elif file_extension == 'pptx':
        loader = UnstructuredPowerPointLoader(file_path)
    elif file_extension == 'xlsx':
        loader = UnstructuredExcelLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    docs = loader.load()
    return docs
