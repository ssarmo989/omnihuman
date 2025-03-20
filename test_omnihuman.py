import omnihuman
import PIL.Image
import os

# Define the text prompt
text = "Raise both hands and clap overhead."

# Replace this with the path to an actual image on your computer
# For example: "C:\\Users\\SHAILENDRA\\Pictures\\person.jpg"
# 
# 
# 
image_path = r"C:\Users\SHAILENDRA\Downloads\setup-files\omnihuman\test_person.jpg"

# Check if image exists
if not os.path.exists(image_path):
    print(f"Error: Image not found at {image_path}")
    exit()

# Load the image
print("Loading image...")
frames = omnihuman.read_frames(image_path)
print(f"Image loaded: {frames.shape}")

# Initialize the model and generate the animation
print("Initializing model (this might take a minute)...")
model = omnihuman.OmniHuman()
frames = model.generate_video(text, frames)
print("Video generated!")

# Display the final frame
PIL.Image.fromarray(frames[-1].permute(1,2,0).numpy()).show()

# Optionally save all frames as a GIF
# frames_rgb = [PIL.Image.fromarray(frame.permute(1,2,0).numpy()) for frame in frames]
# frames_rgb[0].save("output.gif", save_all=True, append_images=frames_rgb[1:], duration=100, loop=0)