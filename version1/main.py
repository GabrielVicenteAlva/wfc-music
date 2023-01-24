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
    img = 1-np.array(img)[:,:,0]//255

    output = wfc.wfc(img,4,7,48,12)
    
    outim = (1-output)*255
    outim = Image.fromarray(np.uint8(outim), 'L')
    outim.save('salida/out.png')

if __name__=='__main__':
    main()