# onnxsim

```bash
  607  git checkout fa46ba5 -- networks/classifiers/inception-v3/onnx/inception_v3_i8.yaml
  608  ./generate -c networks/classifiers/inception-v3/onnx/inception_v3_i8.yaml
  609  clear
  610  python3 valid/jenkins/unit_tests_build.py all --help
  611  python3 valid/jenkins/unit_tests_build.py all -d i8 -i googlenet -b build
  612  python3 valid/jenkins/unit_tests_build.py -c all -d i8 -i googlenet -b build
  613  python3 valid/jenkins/unit_tests_build.py -c classifiers -d i8 -i googlenet -b build
  614  cat build
  615  python3 utils/scripts/onnx_get_model_info.py build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/optimized-model.onnx 
  616  netron -b build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/optimized-model.onnx &
  617  cat build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/network.dump.yaml
  618  cp /nfs/tools/software/common/kann-models-zoo/.kann_cache/models--Kalray--googlenet/snapshots/a774bf5b98240d1770ce142ffbed7228ba5b254f/googlenet-q.onnx .
  619  code build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/network.dump.yaml
  620  onnxsim googlenet-q.onnx googlenet-q.onnx --overwrite-input-shape 1,3,224,224
  621  kann generate build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/network.dump.yaml -d toto
  # delete extra data, then change onnx_model path to the onnxsim'd model with batch 1
  622  kann generate build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/network.dump.yaml -d toto
  623  python3 utils/scripts/onnx_get_model_info.py build/generated/classifiers/class-0000i8+googlenet+onnx+googlenet_i8/optimized-model.onnx 
  624  history
```

```bash
python3 valid/jenkins/unit_tests_build.py -c classifiers -d i8 -i <model> -b build
cp <nfs-path> .
onnxsim <model>.onnx <model>.onnx --overwrite-input-shape 1,3,224,224 # replace for real dims

python3 valid/jenkins/unit_tests_build.py -c classifiers -d i8 -i densenet-121 densenet-169 efficientnet-b0 efficientnet-b4 efficientnetlite-b4 mobilenet-v2 mobilenet-v3-large regnet-x-1.6g resnet101 resnet152 resnet34 resnet50 resnet50v1.5 resnext50 -b build
```

- [ ]  densenet-121
- [ ]  densenet-169
- [ ]  efficientnet-b0
- [ ]  efficientnet-b4 (1,3,380,380)
- [ ]  efficientnetlite-b4
- [ ]  googlenet
- [ ]  mobilenet-v2
- [ ]  mobilenet-v3-large
- [ ]  regnet-x-1.6g
- [ ]  resnet101
- [ ]  resnet152
- [ ]  resnet34
- [ ]  resnet50
- [ ]  resnet50v1.5
- [ ]  resnext50