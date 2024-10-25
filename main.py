from PIL import Image
import os
import cv2

# Define the directories containing the images
directories = ['./Raw_Assets/Background','./Raw_Assets/Body', './Raw_Assets/Eyes', './Raw_Assets/Mouth', './Raw_Assets/Shirts', './Raw_Assets/Accessories']

# Output directory
output_directory = 'Krusty_Bear'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to get all PNG images from a directory
def get_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('.PNG'):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            images.append(img)
    return images

# Load images from each directory
all_images = [get_images_from_directory(directory) for directory in directories]

# Function to overlay images
def combine_images(images):
    overlay = Image.open('./Raw_Assets/overlay.PNG')
    base_image = images[0].copy()  # Start with the first image
    for img in images[1:]:  # Overlay remaining images
        base_image.paste(img, (0, 0), img)
        if img == images[1]:
            base_image.paste(overlay, (0, 0), overlay)
    return base_image

def make_some_picture():
    counter = 1
    for background in all_images[0]:
        for body in all_images[1]:
            for eyes in all_images[2]:
                for mouth in all_images[3]:
                    for shirts in all_images[4]:
                        for accessory in all_images[5]:
                            combined_image = combine_images([background, body, eyes, mouth, shirts, accessory])
                            combined_image.save(os.path.join(output_directory, f'Krusty_Bear_{counter}.png'))
                            print(f'Image {counter} has been saved.')
                            counter += 1
        print(f'All images have been combined and saved in {output_directory}.')

def make_a_movie():
    images = [img for img in sorted(os.listdir(output_directory)) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(output_directory, images[0]))
    height, width, layers = frame.shape

    video_name = 'output_video.mp4'
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(output_directory, image)))

    cv2.destroyAllWindows()
    video.release()

    print(f'Video has been created and saved as {video_name}.')
    

def main ():
    #make_some_picture()
    make_a_movie()


if __name__ == '__main__':
    main()
