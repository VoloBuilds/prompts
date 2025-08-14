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
        with open(pdf_path, 'rb') as fin:
            extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='text', codec='')
        
        markdown_content = output_string.getvalue()
        output_string.close()

        with open(markdown_path, 'w', encoding='utf-8') as fout:
            fout.write(markdown_content)
        
        print(f"Successfully converted '{pdf_path}' to '{markdown_path}'")
        return True
    except Exception as e:
        print(f"An error occurred during PDF to Markdown conversion: {e}")
        return False

if __name__ == "__main__":
    # --- Configuration ---
    pdf_subdirectory = "Google-Prompts-Engineering"  # Directory containing the PDF
    actual_pdf_filename = "gemini-for-google-workspace-prompting-guide-101.pdf"  # Name of the PDF file
    actual_markdown_filename = os.path.splitext(actual_pdf_filename)[0] + ".md"

    # Determine workspace root based on the script's location
    # Assumes the script is in a subdirectory of the workspace root (e.g., utility-tools)
    script_path = os.path.abspath(__file__)  # Full path to this script
    script_dir = os.path.dirname(script_path)   # Directory containing this script (e.g., utility-tools)
    workspace_root = os.path.dirname(script_dir) # Assumed workspace root (one level up from script_dir)
    
    # Construct full paths for the PDF and output Markdown file
    pdf_full_path = os.path.join(workspace_root, pdf_subdirectory, actual_pdf_filename)
    markdown_full_path = os.path.join(workspace_root, pdf_subdirectory, actual_markdown_filename)
    # --- End Configuration ---

    print(f"Attempting to convert: {pdf_full_path}")

    if os.path.exists(pdf_full_path):
        convert_pdf_to_markdown(pdf_full_path, markdown_full_path)
    else:
        print(f"Error: Could not find '{pdf_full_path}'.")
        print("Please ensure the PDF file exists at the specified location and the script is run from the workspace root.")

    # Example usage if you want to specify paths directly:
    # pdf_input = "path/to/your/document.pdf"
    # md_output = "path/to/your/document.md"
    # convert_pdf_to_markdown(pdf_input, md_output) 