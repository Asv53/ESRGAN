import cv2
from skimage.metrics import structural_similarity as ssim
import os

def calculate_psnr(img1, img2):
    mse = ((img1 - img2) ** 2).mean()
    max_val = img1.max()
    psnr = 10 * (max_val**2) / mse
    return psnr

def calculate_ssim(img1, img2):
    return ssim(img1, img2, multichannel=True)

def process_images(hr_folder, lr_folder):
    psnr_values = []
    ssim_values = []

    for filename in os.listdir(hr_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            hr_path = os.path.join(hr_folder, filename)
            lr_path = os.path.join(lr_folder, filename)

            hr_img = cv2.imread(hr_path)
            lr_img = cv2.imread(lr_path)

            psnr = calculate_psnr(hr_img, lr_img)
            ssim_score = calculate_ssim(hr_img, lr_img)

            psnr_values.append(psnr)
            ssim_values.append(ssim_score)

            print(f"Image: {filename}, PSNR: {psnr}, SSIM: {ssim_score}")

    avg_psnr = sum(psnr_values) / len(psnr_values)
    avg_ssim = sum(ssim_values) / len(ssim_values)

    print(f"\nAverage PSNR: {avg_psnr}")
    print(f"Average SSIM: {avg_ssim}")

# Example usage:
high_res_folder = 'D:/miniproject/BasicSR-master/datasets/custom/hr'
low_res_folder = 'D:/miniproject/BasicSR-master/results/21-36/21-36-10000/visualization/custom'

process_images(high_res_folder, low_res_folder)
