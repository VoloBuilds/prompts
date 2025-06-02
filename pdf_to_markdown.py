import io
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
import os

def convert_pdf_to_markdown(pdf_path, markdown_path):
    """
    Extracts text from a PDF file and saves it as a Markdown file.

    Args:
        pdf_path (str): The path to the input PDF file.
        markdown_path (str): The path to save the output Markdown file.
    
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return False

    try:
        output_string = io.StringIO()
        # Extract text from PDF
        with open(pdf_path, 'rb') as fin:
            extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='text', codec='')
        
        markdown_content = output_string.getvalue()
        output_string.close()

        # Write to Markdown file
        with open(markdown_path, 'w', encoding='utf-8') as fout:
            fout.write(markdown_content)
        
        print(f"Successfully converted '{pdf_path}' to '{markdown_path}'")
        return True
    except Exception as e:
        print(f"An error occurred during PDF to Markdown conversion: {e}")
        return False

if __name__ == "__main__":
    # --- Configuration ---
    # The PDF file is located in the 'Google-Prompts-Engineering' subdirectory
    pdf_subdirectory = "Google-Prompts-Engineering"
    pdf_filename = "gemini-for-google-workspace-prompting-guide-101.pdf"
    
    # The Markdown file will be saved in the same subdirectory
    markdown_filename = os.path.splitext(pdf_filename)[0] + ".md"

    # Construct full paths
    # Assumes the script is run from the workspace root '/Users/tonycai/workspace/prompts-remote'
    workspace_root = os.getcwd() # Get current working directory, should be workspace root
    
    pdf_full_path = os.path.join(workspace_root, pdf_subdirectory, pdf_filename)
    markdown_full_path = os.path.join(workspace_root, pdf_subdirectory, markdown_filename)
    # --- End Configuration ---

    print(f"Attempting to convert: {pdf_full_path}")
    print(f"Output Markdown will be: {markdown_full_path}")

    if os.path.exists(pdf_full_path):
        convert_pdf_to_markdown(pdf_full_path, markdown_full_path)
    else:
        print(f"Error: Could not find '{pdf_full_path}'.")
        print("Please ensure the PDF file exists at the specified location and the script is run from the workspace root.") 