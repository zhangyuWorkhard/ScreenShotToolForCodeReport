#ScreenShot for CodeReport
#creat by zhangyu
#creat time 2019-5-14

from selenium import webdriver
import os
import time

# r: do not Data Link Escape
FILE_PATH = r"F:\work\python\..."

def take_screenShot():
    #path for windows
    #filePath = FILE_PATH.replace('\\', '/')
    #print (filePath)

    #init browser
    browser = webdriver.PhantomJS()
    for root,dirs,files in os.walk(FILE_PATH): 
        #list files
        for file in files: 
            #find html
            if (-1 != file.find("html")):
                if (-1 == file.find("sort")):
                    print (file)
                    #file path
                    filePath = os.path.join(root, file) 
                    filePath = filePath.replace('\\', '/')
    
                    #image name
                    imageName = filePath.replace(FILE_PATH.replace('\\', '/') + "/", "") + ".png"
                    imageName = imageName.replace("/", "_")
                    #print imageName
    
                    filePath = "file:///" + filePath
                    #open html
                    browser.get(filePath)
                    #time.sleep(1)
                    #save image
                    browser.save_screenshot(imageName)
    #close browser
    browser.close()

if __name__ == "__main__":
    take_screenShot()
