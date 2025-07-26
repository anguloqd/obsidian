# Period #2 - Exporting and importing with numpy

```bash
  521  mkdir test
  522  cd test
  525  cp -r ../generated/object-detection/yolov5s .
  528  cat yolov5s/onnx/network.dump.yaml 
  529  clear
  530  mkdir io
  531  dd if=/dev/zero of=io/images bs=4915200 count=1 # bs is 1*3*640*640
  532  ls io/
  533  ls -l io/
  534  python
  
  
  import numpy
  numpy.fromfile("io/images", dtype=numpy.float32)
  y = numpy.fromfile("io/images", dtype=numpy.float32)
  
  
  535  clear
  536  kann_opencl_cnn 
  537  kann_opencl_cnn yolov5s/onnx/e*.kann io
  538  kann_opencl_cnn yolov5s/onnx/*.kann io
  539  clear
  540  ll io
  541  ls io
  542  cat yolov5s/onnx/network.dump.yaml 
  543  clear
  544  ls -l io
  545  cat yolov5s/onnx/network.dump.yaml 
  546  clr
  547  clr
  548  clear
  549  python
  
  
  import numpy
  y = numpy.fromfile("io/326", dtype=numpy.float32)
  numpy.reshape(y, (80, 1,80, 255))
  y_ = numpy.reshape(y, (80, 1,80, 255))
  
  
  550  clear
  551  dd if=/dev/zero of=io/images bs=4915200 count=1000 # bs is 1*3*640*640
  552  ls -l io
  553  kann_opencl_cnn yolov5s/onnx/*.kann io
  554  ls -l io
  555  python
  
  
  import numpy
  y = numpy.fromfile("io/326", dtype=numpy.float32)
  y_ = numpy.reshape(y, (80, 1000,80, 255))
  y_ = y_.transpose((1, 0, 2, 3))
  y_.shape
  for x in y_:
    print(x.shape)
  for i, x in enumerate(y_):
	  print(i, x.shape)
	  z = postproc(x)
  
  
  556  ls
  557  ls io
  558  kann run --help
  559  kann run --preared-inputs=io
  560  kann run yolov5s/onnx/*.kann --prepared-inputs=io
  561  kann run --prepared-inputs=io yolov5s/onnx/*.kann
  562  kann run --prepared-inputs=io yolov5s/onnx/
```