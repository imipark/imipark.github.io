#!/usr/bin/env python3
"""
PDF Page Extractor - Converts each page of a PDF into individual images
"""

import sys
from pdf2image import convert_from_path
from pathlib import Path

def extract_pages_as_images(pdf_path, output_dir="pdf_pages", dpi=200, image_format="PNG"):
    """
    Extract each page from a PDF and save as individual images.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the images (default: "pdf_pages")
        dpi: Resolution of output images (default: 200)
        image_format: Format for output images (PNG, JPEG, etc.)
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    print(f"Converting PDF: {pdf_path}")
    print(f"Output directory: {output_path.absolute()}")
    print(f"Resolution: {dpi} DPI")
    print(f"Format: {image_format}\n")
    
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=dpi)
        
        print(f"Found {len(images)} pages in the PDF\n")
        
        # Save each page as an image
        for i, image in enumerate(images, start=1):
            output_file = output_path / f"page_{i:03d}.{image_format.lower()}"
            image.save(output_file, image_format)
            print(f"✓ Saved: {output_file.name} ({image.size[0]}x{image.size[1]} pixels)")
        
        print(f"\n✅ Successfully extracted {len(images)} pages!")
        print(f"📁 Images saved to: {output_path.absolute()}")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_images.py <pdf_file> [output_dir] [dpi]")
        print("\nExample:")
        print("  python pdf_to_images.py myfile.pdf")
        print("  python pdf_to_images.py myfile.pdf output_folder 300")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "pdf_pages"
    dpi_setting = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    
    extract_pages_as_images(pdf_file, output_directory, dpi_setting)
