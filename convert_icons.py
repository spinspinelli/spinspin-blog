#!/usr/bin/env python3
"""
SVG to PNG Converter for spinspin-blog icons
Converts SVG icons to high-quality PNG images
"""

from cairosvg import svg2png
import os

# Define the icons to convert
icons = [
    {
        'name': 'logo-dot',
        'sizes': [64, 128, 256, 512]
    },
    {
        'name': 'synth-knob',
        'sizes': [64, 128, 256, 512]
    },
    {
        'name': 'synth-knob-inactive',
        'sizes': [64, 128, 256, 512]
    }
]

def convert_svg_to_png(svg_path, png_path, size):
    """Convert SVG file to PNG with specified size"""
    try:
        with open(svg_path, 'rb') as svg_file:
            svg2png(
                file_obj=svg_file,
                write_to=png_path,
                output_width=size,
                output_height=size
            )
        print(f"✓ Created: {png_path} ({size}x{size}px)")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {str(e)}")
        return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, 'images')
    
    print("🎨 Converting SVG icons to PNG...\n")
    
    for icon in icons:
        svg_file = os.path.join(images_dir, f"{icon['name']}.svg")
        
        if not os.path.exists(svg_file):
            print(f"⚠ Warning: {svg_file} not found, skipping...")
            continue
        
        print(f"Processing: {icon['name']}.svg")
        
        for size in icon['sizes']:
            png_file = os.path.join(images_dir, f"{icon['name']}-{size}.png")
            convert_svg_to_png(svg_file, png_file, size)
        
        # Create default size (128px) without size suffix
        default_png = os.path.join(images_dir, f"{icon['name']}.png")
        convert_svg_to_png(svg_file, default_png, 128)
        
        print()
    
    print("✅ Conversion complete!")

if __name__ == '__main__':
    main()
