# Sierpinski Tetrahedron Generator

A Blender add-on that generates a 3D Sierpinski Tetrahedron fractal using recursive subdivision.

## Features
- Adds a custom operator to `Add > Add Sierpinski Tetrahedron`.
- Configurable recursion level (0-5) to control fractal complexity.
- Built with Blender’s BMesh API for efficient geometry creation.

## Installation
To set up this add-on in Blender, follow these steps carefully. These instructions work for Blender 2.80 and later, including 4.2+ with the Extensions framework.

1. **Download or Clone the Repository**  
   - Download this repository as a `.zip` or clone it using Git. You’ll get a folder named `blender_sierpinski_addon` containing `__init__.py` and `README.md`.

2. **Prepare the Add-On**  
   - For best results, install it as a folder-based add-on:
     - Right-click the `blender_sierpinski_addon` folder and create a `.zip` file (e.g., on Windows: "Send to > Compressed (zipped) folder"; on macOS/Linux: `zip -r blender_sierpinski_addon.zip blender_sierpinski_addon`).
     - This preserves the folder structure (`blender_sierpinski_addon/__init__.py`), which is recommended for extensibility.

3. **Install in Blender**  
   - Open Blender (2.80 or later recommended; tested up to 4.2+).
   - Go to `Edit > Preferences`.
   - Select the **Add-ons** tab.
   - Select the drop-down menu (top-right) and click **Install from Disk…**.
   - In the file browser, select the `blender_sierpinski_addon.zip` file you created, then click **Install from Disk**.
   - Note: If the add-on doesn’t appear after installation, close and reopen Blender (the "Refresh Local" button may not work reliably).

4. **Enable the Add-On**  
   - In the Add-ons list, search for “Sierpinski” or scroll to find **“Sierpinski Tetrahedron Generator”**.
   - Check the box next to it to enable the add-on.
   - If it’s not visible in the list after enabling, restart Blender to ensure it loads properly.

5. **Verify Installation**  
   - In the 3D Viewport, press `Shift + A`, go to `Mesh`, and look for “Sierpinski Tetrahedron”. If it’s there, you’re set! If not, see the Troubleshooting section.

## Usage
1. In Blender’s 3D Viewport, press `Shift + A` to open the Add menu.
2. Navigate to `Add Sierpinski Tetrahedron` and click it.
3. In the Operator Panel (bottom-left), adjust the “Level” property (0–5) to set the recursion depth, then press Enter.
4. The fractal appears at the 3D Cursor’s location—use the mouse wheel to zoom and middle mouse button to rotate for a better view.

## Notes
- Higher recursion levels (e.g., 4 or 5) create more geometry and may slow down Blender. Start with 1 or 2 for quick testing.
- If the fractal doesn’t appear, ensure the 3D Cursor is in view (`Shift + S > Cursor to World Origin`).
- This add-on is a legacy add-on compatible with Blender 4.2+ Extensions—no `blender_manifest.toml` is required for local use.

## Troubleshooting
- **Add-On Not in Add-ons List**: Reinstall using the `.zip` file and restart Blender.
- **Not in `Shift + A > Mesh`**: Open `__init__.py` in Blender’s Text Editor (switch an editor type to “Text Editor”), click “Run Script” (play button in the header), and check again. If it works, reinstall and restart.
- **Errors**: Open `Window > Toggle System Console` (Windows) or run Blender from a terminal (macOS/Linux) to see error messages, then adjust accordingly.

## Author
- Andrew Chen
