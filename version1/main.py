from PIL import Image
import numpy as np
import sys
import wfc

def main():
    assert len(sys.argv)>0
    path = sys.argv[1]

    try:
        img = Image.open(path)
    except Exception as e:
        print(e)
        return
    img = np.array(img)[:,:,0]//255

    wfc.wfc(img,12,7)

if __name__=='__main__':
    main()