## Period #3 - CVAPPS 462

retinanet-resnet50 : `decode_util.py`, ligne 83 (et 65 aussi), variable `box_head`

with original kann-video-demo: [576, 4]

with new kann-video-demo: [9216, 4]

9216/576 = 16, un facteur de 16 de plus qui sort magiquement ?

soupçon problème d’alignement, var output_tensor in post_process

dans main:

```bash
[(1, 720, 64, 64), (1, 720, 32, 32), (1, 720, 16, 16), (1, 720, 8, 8), (1, 720, 4, 4), (1, 36, 64, 64), (1, 36, 32, 32), (1, 36, 16, 16), (1, 36, 8, 8), (1, 36, 4, 4)]
```

dans aci/dangulo/main:

```bash
[(1, 36, 8, 8), (1, 36, 16, 16), (1, 720, 8, 8), (1, 36, 4, 4), (1, 720, 16, 16), (1, 36, 32, 32), (1, 720, 4, 4), (1, 720, 32, 32), (1, 36, 64, 64), (1, 720, 64, 64)]
```

(de même pour les autres retinanets)

---

ssd1-mobilenet-v1-mlperf : just leave the io info in the yaml.

---

classifiers : rcnn (failed at generation)321135

```bash
2025-06-30 15:42:06,455 | [ERROR]: GEN rcnn            rcnn_f16.yaml - #ID class-0016f16 : > Command '['/work1/dangulo/kaf/kann-models-zoo/./generate', '-c', '/work1/dangulo/kaf/kann-models-zoo/networks/classifiers/rcnn/onnx/rcnn_f16.yaml', '--use-nfs', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/classifiers/class-0016f16+rcnn+onnx+rcnn_f16', '-f']' returned non-zero exit status 1. (kann_utils.py:38)
2025-06-30 15:42:06,455 | [ERROR]: GEN rcnn - #ID class-0016f16 : > ❌ FAIL (26.12 sec) >> 
***

 Generation:  42%|████████████▋                 | 55/130 [00:03<00:04, 16.83it/s]
 Traceback (most recent call last):
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 167, in <module>
     main(opt, other_opt)
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 124, in main
     subprocess.run(cmd_args, check=True)
   File "/usr/lib/python3.10/subprocess.py", line 526, in run
     raise CalledProcessError(retcode, process.args,
 subprocess.CalledProcessError: Command '['kann', 'generate', '/work1/dangulo/kaf/kann-models-zoo/networks/classifiers/rcnn/onnx/rcnn_f16.yaml', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/classifiers/class-0016f16+rcnn+onnx+rcnn_f16', '-f']' returned non-zero exit status 1.
***
 (kann_utils.py:42)
```

vision-transformers: vit-base-224 (generation)

```bash
2025-06-30 15:45:20,935 | [ERROR]: GEN vit-base-224    vit_base_f16.yaml - #ID visio-0034f16 : > Command '['/work1/dangulo/kaf/kann-models-zoo/./generate', '-c', '/work1/dangulo/kaf/kann-models-zoo/networks/vision-transformers/vit-base-224/onnx/vit_base_f16.yaml', '--use-nfs', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/vision-transformers/visio-0034f16+vit-base-224+onnx+vit_base_f16', '-f']' returned non-zero exit status 1. (kann_utils.py:38)
2025-06-30 15:45:20,935 | [ERROR]: GEN vit-base-224 - #ID visio-0034f16 : > ❌ FAIL (29.23 sec) >> 
***
>>> Error in Gather, node '/Gather':
 >>> node of type "Gather" is not supported yet
 Traceback (most recent call last):
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 167, in <module>
     main(opt, other_opt)
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 124, in main
     subprocess.run(cmd_args, check=True)
   File "/usr/lib/python3.10/subprocess.py", line 526, in run
     raise CalledProcessError(retcode, process.args,
 subprocess.CalledProcessError: Command '['kann', 'generate', '/work1/dangulo/kaf/kann-models-zoo/networks/vision-transformers/vit-base-224/onnx/vit_base_f16.yaml', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/vision-transformers/visio-0034f16+vit-base-224+onnx+vit_base_f16', '-f']' returned non-zero exit status 1.
***
 (kann_utils.py:42)
```

yolos (generation)

```bash
2025-06-30 15:47:07,222 | [ERROR]: GEN yolos           yolos_f16.yaml - #ID visio-0035f16 : > Command '['/work1/dangulo/kaf/kann-models-zoo/./generate', '-c', '/work1/dangulo/kaf/kann-models-zoo/networks/vision-transformers/yolos/onnx/yolos_f16.yaml', '--use-nfs', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/vision-transformers/visio-0035f16+yolos+onnx+yolos_f16', '-f']' returned non-zero exit status 1. (kann_utils.py:38)
2025-06-30 15:47:07,222 | [ERROR]: GEN yolos - #ID visio-0035f16 : > ❌ FAIL (106.29 sec) >> 
***
>>> Error in Concat, node '/vit/embeddings/Concat':
 >>> An image with name /vit/embeddings/Concat_output_0_img_copy_cst already exists
 Traceback (most recent call last):
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 167, in <module>
     main(opt, other_opt)
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 124, in main
     subprocess.run(cmd_args, check=True)
   File "/usr/lib/python3.10/subprocess.py", line 526, in run
     raise CalledProcessError(retcode, process.args,
 subprocess.CalledProcessError: Command '['kann', 'generate', '/work1/dangulo/kaf/kann-models-zoo/networks/vision-transformers/yolos/onnx/yolos_f16.yaml', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/vision-transformers/visio-0035f16+yolos+onnx+yolos_f16', '-f']' returned non-zero exit status 1.
***
 (kann_utils.py:42)
```

segformer (generation)

```bash
2025-06-30 15:55:58,174 | [ERROR]: GEN segformer       segformer_b2_f16.yaml - #ID visio-0033f16 : > Command '['/work1/dangulo/kaf/kann-models-zoo/./generate', '-c', '/work1/dangulo/kaf/kann-models-zoo/networks/vision-transformers/segformer/onnx/segformer_b2_f16.yaml', '--use-nfs', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/vision-transformers/visio-0033f16+segformer+onnx+segformer_b2_f16', '-f']' returned non-zero exit status 1. (kann_utils.py:38)
2025-06-30 15:55:58,178 | [ERROR]: GEN segformer - #ID visio-0033f16 : > ❌ FAIL (691.99 sec) >> 
***
    raise MemoryError("Not enough memory to allocate {} bytes required for {} as temporary buffer".format(alloc.length, str(layer)))
 MemoryError: Not enough memory to allocate 2818048 bytes required for Reshape /encoder/block.0.0/mlp/dwconv/Reshape_reshape as temporary buffer
 Traceback (most recent call last):
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 167, in <module>
     main(opt, other_opt)
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 124, in main
     subprocess.run(cmd_args, check=True)
   File "/usr/lib/python3.10/subprocess.py", line 526, in run
     raise CalledProcessError(retcode, process.args,
 subprocess.CalledProcessError: Command '['kann', 'generate', '/work1/dangulo/kaf/kann-models-zoo/networks/vision-transformers/segformer/onnx/segformer_b2_f16.yaml', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/vision-transformers/visio-0033f16+segformer+onnx+segformer_b2_f16', '-f']' returned non-zero exit status 1.
***
 (kann_utils.py:42)
```

deeplabv3plus-mobilenetv3 (generation)

```bash
2025-06-30 16:08:29,022 | [ERROR]: GEN deeplabv3plus-mobilenetv3 deeplabv3plus_mobilenetv3_f16.yaml - #ID segme-0078f16 : > Command '['/work1/dangulo/kaf/kann-models-zoo/./generate', '-c', '/work1/dangulo/kaf/kann-models-zoo/networks/segmentation/deeplabv3plus-mobilenetv3/onnx/deeplabv3plus_mobilenetv3_f16.yaml', '--use-nfs', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/segmentation/segme-0078f16+deeplabv3plus-mobilenetv3+onnx+deeplabv3plus_mobilenetv3_f16', '-f']' returned non-zero exit status 1. (kann_utils.py:38)
2025-06-30 16:08:29,023 | [ERROR]: GEN deeplabv3plus-mobilenetv3 - #ID segme-0078f16 : > ❌ FAIL (23.67 sec) >> 
***
    raise MemoryError("Not enough memory to allocate {} bytes required for {} as temporary buffer".format(alloc.length, str(layer)))
 MemoryError: Not enough memory to allocate 6117120 bytes required for ConvolutionCV2 /classifier/classifier.0/convs.2/convs.2.0/Conv_split_0 as temporary buffer
 Traceback (most recent call last):
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 167, in <module>
     main(opt, other_opt)
   File "/work1/dangulo/kaf/kann-models-zoo/utils/kann_generate.py", line 124, in main
     subprocess.run(cmd_args, check=True)
   File "/usr/lib/python3.10/subprocess.py", line 526, in run
     raise CalledProcessError(retcode, process.args,
 subprocess.CalledProcessError: Command '['kann', 'generate', '/work1/dangulo/kaf/kann-models-zoo/networks/segmentation/deeplabv3plus-mobilenetv3/onnx/deeplabv3plus_mobilenetv3_f16.yaml', '-d', '/work1/dangulo/kaf/kann-models-zoo/z/generated/segmentation/segme-0078f16+deeplabv3plus-mobilenetv3+onnx+deeplabv3plus_mobilenetv3_f16', '-f']' returned non-zero exit status 1.
***
 (kann_utils.py:42)
```
