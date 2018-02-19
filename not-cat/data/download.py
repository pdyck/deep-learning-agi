import requests
import cv2
import os
from time import sleep
import numpy as np

def download(urls, categories):
    for url, category in zip(urls, categories):
        image_urls = get_image_list(url)
        dirname = 'images/category'
        create_dir_if_not_exist(dirname)
        for index, image_url in enumerate(image_urls):
            download_image(image_url, dirname + '/' + str(index) + '.jpg')
        check_images(dirname)

def get_image_list(url):
    text = requests.get(url).text
    return text.split('\r\n')

def create_dir_if_not_exist(dir):
    print(dir)
    if not os.path.exists(dir):
        os.makedirs(dir)

def download_image(url, path):
    f = open(path, 'wb')
    try:
        f.write(requests.get(url, timeout=5).content)
        print('downloaded', url)
    except:
        print('failed to download', url)
    f.close()

def check_images(dir):
    invalid = cv2.imread('invalid/flickr.jpg')
    for image_path in [dir + '/' + f for f in os.listdir(dir)]:
        delete = False
        try:
            image = cv2.imread(image_path)
            if image is None:
                delete = True
            if invalid.shape == image.shape and not(np.bitwise_xor(invalid, image).any()):
                delete = True
        except:
            delete = True
        if delete:
            print('deleting', image_path)
            os.remove(image_path)

def main():
    urls = [
        'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02121620'
    ]

    paths = ['cat']

    download(urls, paths)

if __name__ == '__main__':
    main()
