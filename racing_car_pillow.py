from PIL import Image, ImageDraw

# Create a blank image with a white background
img = Image.new('RGB', (500, 250), 'white')
draw = ImageDraw.Draw(img)

# Draw the body of the car
draw.rectangle([100, 120, 400, 170], fill='red', outline='black')

# Draw the roof of the car
draw.polygon([(150, 120), (250, 60), (350, 60), (400, 120)], fill='black', outline='black')

# Draw the windows
draw.rectangle([160, 70, 240, 120], fill='lightblue', outline='black')
draw.rectangle([260, 70, 320, 120], fill='lightblue', outline='black')

# Draw the front and rear bumpers
draw.rectangle([90, 130, 100, 160], fill='grey', outline='black')
draw.rectangle([400, 130, 410, 160], fill='grey', outline='black')

# Draw the wheels
draw.ellipse([120, 160, 180, 200], fill='black', outline='black')
draw.ellipse([320, 160, 380, 200], fill='black', outline='black')

# Draw wheel rims
draw.ellipse([140, 175, 160, 185], fill='grey', outline='black')
draw.ellipse([340, 175, 360, 185], fill='grey', outline='black')

# Draw headlights
draw.ellipse([90, 135, 110, 155], fill='yellow', outline='black')
draw.ellipse([400, 135, 420, 155], fill='yellow', outline='black')

# Draw a rear spoiler
draw.polygon([(100, 120), (140, 70), (180, 70), (180, 120)], fill='red', outline='black')

# Show the image
img.show()

# Save the image to a file
img.save("enhanced_racing_car.png")
