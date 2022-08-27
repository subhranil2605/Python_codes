import os
import time
import win32com.client


PPT_TO_PDF = 32


def presentation_to_pdf(direc: str, delete_file: bool):
    for root, dirs, files in os.walk(direc):
        for f in files:
            if f.endswith(".pptx"):
                try:
                    print(f)
                    in_file=os.path.join(root, f)
                    time.sleep(2)
                    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                    deck = powerpoint.Presentations.Open(in_file)
                    deck.SaveAs(os.path.join(root,f[:-5]), PPT_TO_PDF) # formatType = 32 for ppt to pdf
                    deck.Close()
                    powerpoint.Quit()
                    print('done')
                    if delete_file:
                        os.remove(os.path.join(root,f))
                    pass
                except:
                    print('could not open')
                    os.remove(os.path.join(root,f))
            elif f.endswith(".ppt"):
                try:
                    print(f)
                    in_file=os.path.join(root, f)
                    time.sleep(2)
                    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                    deck = powerpoint.Presentations.Open(in_file)
                    deck.SaveAs(os.path.join(root,f[:-4]), PPT_TO_PDF) # formatType = 32 for ppt to pdf
                    deck.Close()
                    powerpoint.Quit()
                    print('done')
                    if delete_file:
                        os.remove(os.path.join(root, f))
                    pass
                except:
                    print('could not open')
                    os.remove(os.path.join(root, f))
            else:
                pass


if __name__ == "__main__":
    root_dirctory= r'C:\Users\imsub\Desktop\Cloud Computing ppt presentation(Data Science) ppt Copy'
    presentation_to_pdf(root_dirctory)
