# Mandelbrot-Generator

This is a Mandelbrot set generator/viewer. 

<b>Instructions:</b>

    Iteration depth:

Enter the number of iterations per pixel (time increases with size)

    Colors? y/n

Enter "y" for image with colors or "n" for black&white image (different options exist)

   <b><em>If "y"</em></b>

       Background color (red: 0-25 green: 40-100 blue: 150-170): 
   
   Enter the desired hue value for the background
   
       Lightness (0-255) :
   
   Enter the lightness value for the colors (smaller is darker)
   
       White glow (positive integer between 0-20 f.ex):
   
   Enter a value for a white glow effect around the boundaries. Increasing this value makes color shifts more visible. 
   To compensate this,  increase the iteration depth
   
    
   <b><em>If "n"</em></b>
     
       Options:
       -White outlines on black background (wout) 
       -Black outlines on white background (bout) 
       -Black on white background (b)
       -White on black background (w)

Chose the desired option with the respective command (without parentheses)
 
 
    Width of resolution (pixels): <em> Integer </em>
  
    Height of resolution (pixels): <em> Integer </em>
  
    Start value for X: <em> Float</em>
  
    End value for X: <em> Float > Start </em>
  
    Y value (= will be the middle of the screen): <em> Float </em>
 
Enter your image resolution aswell as the coordinates of the site to be rendered.

Coordinates for a full mandelbrot set (for reference):

    Width of resolution (pixels): <em> Integer </em>
  
    Height of resolution (pixels): <em> Integer </em>
  
    Start value for X: -2
  
    End value for X: 1
  
    Y value (= will be the middle of the screen): 0


The rendered image is saved to your desktop

