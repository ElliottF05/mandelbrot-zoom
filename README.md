# Mandelbrot Zoom

This is a project set to allow users to dynamically explore the Mandelbrot set and generate images of the set.

## How to Use

Use mandelbrot_static.py to save static images of the Mandelbrot set to output.png.\
Edit the window settings and resolutions accordingly.\

Use mandelbrot_dynamic.py to launch an interactable user interface allowing the user to repeatedly zoom in wherever they want on the Mandelbrot set. 

### Controls for mandelbrot_dynamic

**On Click**: center image on position of click and zoom in by zoomPerClick (default 1.20x).

**Up/Down Arrow Keys**: increment/decrement zoomPerClick by 0.10x (min 0.50x, max 2.00x).

**Left/Right Arrow Keys**: increment/decrement depth (number of iterations) by 1.1x.

\
\
\
Do not run mandelbrot_engine.py on its own, it will not do anything and is only used by mandelbrot_static.py and mandelbrot_dynamic.py to do the math to generate the images.