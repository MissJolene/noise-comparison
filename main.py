import os
from numpy import ndarray
import skimage as ski
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

def main():
    image_directory = "./images"
    list_files = os.listdir(image_directory)
    subfolders : list[str] = []
    for filename in list_files:
        path = os.path.join(image_directory, filename)
        if os.path.isdir(path):
            subfolders.append(path)

    for folder in subfolders:
        print(f"Processing images in folder: {folder}")
        images : list[tuple[str, ndarray]]= []
        reference_image = None
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if filename.endswith('_denoised.png'):
                if reference_image is None:
                    reference_image = ski.io.imread(file_path)
                else:
                    print(f"A reference image already exists for folder {folder}. Ignoring additional reference image {filename}")
            elif filename.endswith('.png'):
                images.append((filename, ski.io.imread(file_path)))

        if reference_image is None:
            print(f"Reference image not found for folder {folder}")
            continue

        for (filename, image) in images:
            ssim_value = ssim(reference_image, image, data_range = image.max() - image.min(), channel_axis=2)
            psnr_value = psnr(reference_image, image, data_range = image.max() - image.min())
            print(f"{filename} - ssim: {ssim_value}, psnr: {psnr_value}")

if __name__ == "__main__":
    main()
