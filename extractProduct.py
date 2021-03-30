import cv2
import requests
import io
import json

def ocr_file(file):

## Image reading
    img = cv2.imread(file)
    url_api = "https://api.ocr.space/parse/image"

    _, compressedimage = cv2.imencode(".png",img, [1, 90])
    file_bytes = io.BytesIO(compressedimage)
## Sending via POST to the API and its parameters    
    result = requests.post(url_api, 
                        files={file: file_bytes}, 
                        data={"apikey":"helloworld",
                        "language": "ger",
                        "OCREngine": 2})
    result = result.content.decode()
    result = json.loads(result)
## Returns the text extracted from the image
    return result.get("ParsedResults")[0].get("ParsedText")
    

test_file = ocr_file('ROI_1.png')
print(test_file)

