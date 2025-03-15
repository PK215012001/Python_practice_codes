with open('E:\\Codes\\Python_codes\\__pycache__\\sample.png', 'rb') as rf:
    with open('E:\\Codes\\Python_codes\\__pycache__\\copy.png', 'wb') as wf:
        chunk = 1024
        rf_chunk = rf.read(chunk)
        wf.write(rf_chunk)