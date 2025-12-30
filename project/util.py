import os
import config
import pymupdf.layout
import pymupdf4llm
from pathlib import Path
import glob

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def pdf_to_markdown(pdf_path, output_dir):
    """Convert PDF to Markdown using PyMuPDF4LLM."""
    doc = pymupdf.open(pdf_path)
    md = pymupdf4llm.to_markdown(doc, header=False, footer=False, page_separators=True, ignore_images=True, write_images=False, image_path=None)
    md_cleaned = md.encode('utf-8', errors='surrogatepass').decode('utf-8', errors='ignore')
    output_path = Path(output_dir) / Path(doc.name).stem
    Path(output_path).with_suffix(".md").write_bytes(md_cleaned.encode('utf-8'))

def pdfs_to_markdowns(path_pattern, overwrite: bool = False):
    """Convert multiple PDFs to Markdown."""
    output_dir = Path(config.MARKDOWN_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_path in map(Path, glob.glob(path_pattern)):
        md_path = (output_dir / pdf_path.stem).with_suffix(".md")
        if overwrite or not md_path.exists():
            pdf_to_markdown(pdf_path, output_dir)

def document_to_markdown(file_path, output_dir):
    """
    Convert various document formats to Markdown using Unstructured.
    Supports: PDF, DOCX, TXT, HTML, MD, and more.

    Args:
        file_path: Path to the document file
        output_dir: Directory to save the markdown output

    Returns:
        Path to the generated markdown file, or None if conversion fails
    """
    try:
        # Try using the new langchain-unstructured package first
        try:
            from langchain_unstructured import UnstructuredLoader
            loader = UnstructuredLoader(str(file_path))
        except ImportError:
            # Fall back to the old package if new one is not available
            from langchain_community.document_loaders import UnstructuredFileLoader
            loader = UnstructuredFileLoader(str(file_path))

        documents = loader.load()

        if not documents:
            print(f"⚠️  No content extracted from {file_path}")
            return None

        # Combine all document pages into a single markdown text
        markdown_content = ""
        for doc in documents:
            markdown_content += doc.page_content + "\n\n"

        # Clean markdown content
        markdown_content = markdown_content.encode('utf-8', errors='surrogatepass').decode('utf-8', errors='ignore')

        # Save as markdown
        file_path_obj = Path(file_path)
        output_path = Path(output_dir) / file_path_obj.stem
        final_path = Path(output_path).with_suffix(".md")
        final_path.write_bytes(markdown_content.encode('utf-8'))

        return final_path

    except Exception as e:
        print(f"❌ Error converting {file_path} to markdown: {e}")
        return None