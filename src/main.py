from haystack import Pipeline
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes.file_converter import PDFToTextConverter


def addPdfToDocumentStore(document_store, file_path):
    converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])

    indexing_pipeline = Pipeline()
    indexing_pipeline.add_node(component=converter, name="Converter", inputs=["File"])
    indexing_pipeline.add_node(
        component=document_store, name="DocumentStore", inputs=["Converter"]
    )

    indexing_pipeline.run(file_paths=[file_path])


document_store = ElasticsearchDocumentStore(host="localhost", port=9200)
addPdfToDocumentStore(document_store, "public/nerf.pdf")
