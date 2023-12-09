IP_ADAPTER = "https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus-face_sd15.bin?download=true" #@param {type:"string"}
ppth = True

if IP_ADAPTER != "":
  pth2 = '/content/lite_colab/models/ControlNet/'
  if not ppth:
    modelname2="model.bin"
  else:
    modelname2="ip-adapter-plus-face_sd15.pth"
  dwnld2 = pth2 + modelname2
  print('[1;32mDownload ip adapter...')
  !gdown --fuzzy -O $dwnld2 "$IP_ADAPTER"
  clear_output()
  print('[1;32mDone!')
else:
  print('[1;31mPaste model link and try again!')
