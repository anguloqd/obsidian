# Period #1 - KaNN Training

> [!tip] 💡
>
> Here, I want to take notes from the KaNN Training session, KaNN How-To pages from confluence, and my usage of KaNN in general.

# PPTX

[](https://kalray.atlassian.net/wiki/spaces/KANN/pages/569212956/KaNN+How+To)

[https://kalrayinc.sharepoint.com/sites/Embedded-ComputeApps/Shared%20Documents/Forms/AllItems.aspx?e=5%3A9e260ecbf525434a9f04bb14b4e1e586&sharingv2=true&fromShare=true&at=9&CT=1730284899731&OR=OWA%2DNT%2DMail&CID=fea87111%2Dfd76%2D3b96%2Dcc8b%2D3f0b9cc5b099&FolderCTID=0x0120006533E1ECD394894885D12A79DD4491D0&id=%2Fsites%2FEmbedded%2DComputeApps%2FShared%20Documents%2FCompute%20Apps%2FSDK%20Trainings%2FKaNN%20training&viewid=4b762c53%2D371c%2D4257%2Dada0%2D9dbe7533d763](https://kalrayinc.sharepoint.com/sites/Embedded-ComputeApps/Shared%20Documents/Forms/AllItems.aspx?e=5%3A9e260ecbf525434a9f04bb14b4e1e586&sharingv2=true&fromShare=true&at=9&CT=1730284899731&OR=OWA%2DNT%2DMail&CID=fea87111%2Dfd76%2D3b96%2Dcc8b%2D3f0b9cc5b099&FolderCTID=0x0120006533E1ECD394894885D12A79DD4491D0&id=%2Fsites%2FEmbedded%2DComputeApps%2FShared%20Documents%2FCompute%20Apps%2FSDK%20Trainings%2FKaNN%20training&viewid=4b762c53%2D371c%2D4257%2Dada0%2D9dbe7533d763)

# Notes from KaNN: How-To

> [!tip] 💡
>
> You first install the “kaf” module following the ACE training.

Running a neural network is a 4 step process:

1. Build the runtime (already done in ACE install)
2. Generate a NN using “`kann generate`”
3. Prepare the inputs for the NN
4. Actually run the NN

The confluence page will run the CNN algorithm “UNet” on two images. The test is created on a parallel directory to kaf, called “`test_unet`”. In general, your KaNN test should be outside of the kaf directory.

## Generate a NN using “`kann generate`”

Let’s look at “`kann generate -h`” (`-h` for help):

```bash
Usage: kann generate [OPTIONS] CONFIG_PATH

  Generate code from the description of an inference network.

  CONFIG_PATH is the path of a network configuration file in yaml.
```

An example usage is as follows:

```bash
# Generate MPPA binary
# Binary and logs are placed in generated_${arch}_${model name}_FP16_${framework}_${nb_of_clusters}_{quantization format}
# In this example: ./generated_kv3_2_UNet_FP16_tensorflow_5c_fp16

kann generate --arch=kv3-2 ../examples/networks/UNet2D_Tiny_Med/onnx/network_fp16.yaml

# Code can be generated with exploration options:
# --generate-txt-cmds: explore clusters commands in readable format
# --draw-graph-pdf: export generated graph transformed by kann, showing buffers, operators, computing steps...
# 	File "neural_network.dot" is generated within the code generation directory and can be viewed with xdot executable

kann generate --arch=kv3-2 --generate-txt-cmds --draw-graph-pdf ../examples/networks/UNet2D_Tiny_Med/onnx/network_fp16.yaml
```

## Prepare inputs

This step generates an input data stream from video or a set of pictures (png format). We will be using two images: `cat.png` and `cup.png`.

```bash
GENERATED_DIR=generated_kv3_2_UNet2D_Tiny_Medical_MRI_brain_onnx_5c_fp16

# Enter test_unet dir
# Notice the dir "test_unet" is parallel to "kaf" and not inside of "kaf"
cd /work1/$USER/test_unet

# Create directory for IO files
INPUTS_OUTPUTS_DIR="${GENERATED_DIR}/inputs_outputs_kann"
if [ ! -d "$INPUTS_OUTPUTS_DIR" ]; then
    mkdir -p "$INPUTS_OUTPUTS_DIR"
    echo "Directory created: $INPUTS_OUTPUTS_DIR"
else
    echo "Directory already exists: $INPUTS_OUTPUTS_DIR"
fi

# Open ./generated_kv3_2_UNet2D_Tiny_Medical_MRI_brain_onnx_5c_fp16/network.dump.yaml file, 
# and look at the input and output file names
# The input stream name is located at: "input_nodes_name"(here: input_1)
# The output stream name is located at: "output_nodes_name" (here: Identity)
# $ vi generated_kv3_2_UNet_FP16_tensorflow_5c_fp16/network.dump.yaml

# We will work with two images: cat.png and cup.png
INPUT_STREAM=${GENERATED_DIR}/inputs_outputs_kann/images # input stream name
IMAGE1=../kaf/kann/examples/networks/UNet2D_Tiny_Med/onnx/data/MRI_brain/TCGA_CS_4941_19960909_1.tif
IMAGE2=../kaf/kann/examples/networks/UNet2D_Tiny_Med/onnx/data/MRI_brain/TCGA_CS_4941_19960909_2.tif

# Generate a stream of batch size=2 
python $GENERATED_DIR/input_preparator.py $INPUT_STREAM  $IMAGE1 $IMAGE2 --batch-size 2
```

## Run the NN

A test application for model execution has been compiled in “Build KaNN Runtime” step. This step triggers inference of the input batch stream (2 images) on MPPA.

```bash
# Executed in test_unet dir.

# Set KANN_POCL_FILE var if not done already
export KANN_POCL_FILE=$KANN_BUILD_DIR_CV2/opencl_kernels/mppa_kann_opencl.cl.pocl

# Launch execution
$KANN_BUILD_DIR_CV2/bin/kann_opencl_cnn $GENERATED_DIR/serialized_params_KaNNv5.3.0-UNet2D-Tiny-Medical-MRI-brain-fp16-5c.bin $INPUTS_OUTPUTS_DIR

# Output stream is stored in inputs_outputs_kann directory. 
```

# Notes from KaNN: `kaf_applications`

Remember to call “make” on the terminal to execute the makefile utility and produce the necessary binaries.

## `/kaf_acceleration_examples/README.template`

```bash
-----------------------------------------------------
	 Kalray ACE version  : v${shell:pkg-config kalray-ace --modversion}
	 KaNN version        : v${shell:pkg-config kann-runtime --modversion}
	 KaNN Service version: v${shell:pkg-config kann-service --modversion}
-----------------------------------------------------

Table of Contents
-----------------
1. Introduction

2. General Information
    2.1. KaNN Service version
    2.2. Building examples
    2.3. Running examples and L2 Cache Policy
    2.4. Example networks for testing
    2.5. Example utility functions
        2.5.1. Python utility script
        2.5.2. Python script for random image generation
        2.5.3. OpenCL utility script

3. KaNN Service
    3.1. Installing KaNN & link to documentation
    3.2. kann-video-demo examples
        3.2.1. kann-video-demo presentation
        3.2.2. kann-video-demo with a webcam
        3.2.3. kann-video-demo with a video file
    3.3. Simple example
    3.4. Batched example
    3.5. Service multi-instance example
    3.6. Pipelining example
    3.7. Multi device examples
        3.7.1. Single Process Multi Thread example
        3.7.2. Multi Process Single Thread example
        3.7.3. Heterogeneous example (KaNN+OpenCL-C Whitebox)
    3.8. Custom layer example
    3.9. Profiling example
    3.10. Python API example
    3.11. Input check example
    3.12. ONNX quantization example

4. OpenCL examples
    4.1. OpenCL-C Whitebox example

5. Misc examples
    5.1 PCIe bus / MPPA info example

-------------------------------------------------------------------------------
------------------------------1. Introduction----------------------------------
-------------------------------------------------------------------------------

This package contains the source code of examples showing how to use the Kalray Neural Network (KaNN) Service.

-------------------------------------------------------------------------------
----------------------------2. General Information-----------------------------
-------------------------------------------------------------------------------

2.1. KaNN Service version
--------------------------
KaNN Service: v${shell:pkg-config kann-service --modversion}

ACE ${shell:pkg-config kalray-ace --modversion} must be installed to build and run KAF acceleration examples.

2.2. Building examples
----------------------
The 'make' command builds all examples. Output binaries are located in output/bin directory.
$ make

2.3. Running examples and L2 Cache policy
-----------------------------------------
In many examples, we use the psutil package for CPU-usage analysis. Be sure to have it installed on your machine.
$ pip install psutil

You can use any Python environment manager compatible with Python wheel: pip, Pipenv, Poetry, etc

All examples are compatible with either one of the following two L2 cache policies: L2 cache activated and L2 cache disabled.
L2 cache policy is managed by loading a specific firmware on MPPA, which is set using the POCL_MPPA_FIRMWARE_NAME environment variable.

All programs can be run without specifying firmware:
$ ./bin <args>

Or firmware may be specified:
$ POCL_MPPA_FIRMWARE_NAME=<firmware> ./bin <args>

Valid values for firmware are:
    POCL_MPPA_FIRMWARE_NAME=ocl_fw_l1.elf       --> L2 Cache DISABLED
    POCL_MPPA_FIRMWARE_NAME=ocl_fw_l2_d_1m.elf  --> L2 Cache ENABLED

By default, the L2 cache is enabled.

2.4. Example networks for testing
---------------------------------
We provide a variety of trained networks for testing KaNN's examples.
These networks are located in:

$ ls $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks

We provide networks of different categories, either in float16 (onnx) or int8-quantization (tflite):

- Object-Detection: YOLO_v5s6_relu (onnx)
- Segmentation: UNet2D_Tiny_Med (onnx)
- Classification: ResNet50-MLPerf (onnx/tflite)

2.5. Example utility functions
-------------------------------
2.5.1. Python utility script
----------------------------
We provide a python utility script located at:
$ kann_examples/utils/example_utils.py

Handling networks with multiple inputs means having to call the input_preparator.py repeatedly.
To ease the process, we provide a utility function that calls the input_preparator.py for all the inputs of our network.
This function is called prepare_input_files.

2.5.2. Python script for random image generation
------------------------------------------------

We also provide a script located at:
$ kann_examples/utils/generate_random_images.py

We do not provide any images for testing our networks, but we provide a utility function and a script to easily generate random images,
in various shapes, formats, data types, etc.

The script generates a directory of _random images for each input of a given network.
For example if the network has 2 inputs inputA and inputB, the obtained generated_image_directory would have the following tree structure:

    generated_image_directory/
           |-- inputA/
           |     |-- img0.png
           |     |-- img1.png
           |-- inputB/
                 |-- img0.png
                 |-- img1.png

It requires the output directory, the yaml configuration file of your network, the format and the shape of the images.
The configuration file is used to get the names of each input.
The accepted formats are png and npy.

By default, the number of images (frames) is set to 1.

It is also possible to specify the data type and the range of values.
By default the data type is set to float16 with a range between 0 and 1 for npy images and uint8 with a range between 0 and 255 otherwise.

To run the script:
$ python3 utils/generate_random_images.py <generated_image_directory> <path_to_yaml> --format [.png|.npy] --shape <SHAPE ...> [--dtype <DTYPE> --range <RANGE ...> --nb_images <NB_IMAGES>]

How to use the script is shown below, in the KaNN examples section.

2.5.3. OpenCL utility script
----------------------------
We provide an OpenCL utility script located at:
$ kann_examples/utils/cl_utils.hpp

This header file gives a few pure OpenCL methods for accessing MPPA devices on Kalray's K300 or TC4,
as well as creating sub-devices of one or more specific clusters on the MPPA.

-------------------------------------------------------------------------------
-----------------------------3. KaNN ------------------------------------------
-------------------------------------------------------------------------------
3.1. Installing KaNN & link to documentation
--------------------------------------------
The following examples demonstrate various features of KaNN.
It is recommended to execute all examples in this order, as they get increasingly more complex.

Before executing anything, make sure that the KaNN Generator Python wheel is installed (see ACE README)

For any additional information on KaNN, please look at the KaNN user documentation: $KALRAY_TOOLCHAIN_DIR/share/doc/kann/index.html

3.2. kann-video-demo examples
-----------------------------
3.2.1. kann-video-demo presentation
-----------------------------------
A tool named kann_video_demo.py is provided to ease the launch of neural networks inference demonstrations on MPPA.
This tool is a python script wrapping a provided Host binary implementing an instance of the KaNN Service.
It takes care of pre-processing inputs, offloading the inference on the MPPA, and post-processing the outputs.
This script can be directly called in command line using:
$ python3 ./video_demo_example/kann_video_demo.py <network> <source>

<network> should be the path to a folder created by the "kann generate" command.
It should contain:
    - A .yaml configuration file describing the network
    - A .bin file containing the serialized network
    - pre and post processing scripts

<source> can either be a webcam or a video file.

Before running kann_video_demo.py, install 'screeninfo' python module:
$ pip install screeninfo

3.2.2. kann-video-demo with a webcam
------------------------------------
Note: Webcam examples uses /dev/video0 referred as 0 in video demo.
User must have sufficient permission on this device to run demos on webcam.
User may belong to "video" Linux group or manually set permission with command "sudo chmod 777 /dev/video0".

To generate a YOLOv5s6_relu in FP16 on 5 clusters
$ cd kann_examples/
$ kann generate $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml -d YOLO_fp16

Then, to launch the demo:
$ python3 video_demo_example/kann_video_demo.py YOLO_fp16 0

3.2.3. kann-video-demo with a video file
----------------------------------------
Give the path to the video file you wish to process as the <source> argument to kann-video-demo.

To generate a ResNet50 in FP16 on 5 clusters:
$ cd kann_examples
$ kann generate $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/tflite/network_int8_fp16_kv3_2_iof32_L2ON.yaml -d ResNet50_MLPerf_tflite

Then, to launch the demo:
$ python3 video_demo_example/kann_video_demo.py ResNet50_MLPerf_tflite ../misc/video_demo.mp4

3.3. Simple example
-------------------
This example shows a basic implementation of the KaNN Service for offloading a Neural Network.
The simple_example.py is a wrapper around the simple_example.cpp.
The .py file takes as arguments:
- the path to the compiled simple_example.cpp
- the path to a network's configuration .yaml file

It is made of 5 main steps:
  1. Call "kann generate" on the provided network
  2. Pre-process images using the input_preparator.py
  3. Offload computation on the MPPA by calling the binary
  4. Compute the "golden reference" on your Host using "kann genref"
  5. Compare the MPPA's output with the golden reference using "kann diff"

run:
$ cd kann_examples/
$ python3 simple_example/simple_example.py <path_to_compiled_kann_cpp> <path_to_yaml> --images_dir=<path_to_images>

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50

$ python3 simple_example/simple_example.py ../output/bin/simple_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --images_dir=example_images 

3.4. Batched example
--------------------
This example aims to demonstrate the posibility of executing the same network with different batch sizes.
The batched_simple_example.py is also using simple_example.cpp.
We consider a network that we will generate twice, using "kann generate"'s forced_batch_size option, once with forced_batch_size = 1, and one with forced_batch_size = 2).

The execution is similar to the previous example and it is done sequentially for the two generated networks.
For each inference, we will give exactly the same inputs, which we preprocess with different batch sizes and we show that we have the same output.

run:
$ cd kann_examples/
$ python3 simple_example/batched_simple_example.py <path_to_compiled_kann_cpp> <path_to_yaml> --images_dir=<path_to_images>

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50 

$ python3 simple_example/batched_simple_example.py ../output/bin/simple_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --images_dir=example_images  

Warning: For understandability, this example only works with 1input/1output networks

3.5. Service multi-instance example:
------------------------------------
In this example, we aim to demonstrate the possibility of launching multiple instances of the KaNN Service.
We consider an input network, and call "kann generate" with the "--nbr-clusters" argument set to 1.
The obtained serialized network will therefore be offloaded on 1 cluster.
Here, we have five instances of the KaNN Service running simultaneously on a separate cluster without interactions between them.

The instances are initialized and ran in parallel, from five different threads. The threads share the context and the device, however they have their own KaNN Service and sub-device.

We compare the outputs of the 5 instances to the associated golden reference, proving the exactness of our computation.
We also compare the outputs of the instances in a cross-validation manner, proving that an output is independent of which cluster(s) the instance was running on.

run:
$ cd kann_examples/
$ python3 multi_instance_example/multi_instance_example.py <path_to_compiled_kann_cpp> <path_to_yaml> --images_dir=<path_to_images> 

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/tflite/network_int8_fp16_kv3_2_iof32_L2ON.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50 

$ python3 multi_instance_example/multi_instance_example.py ../output/bin/multi_instance_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/tflite/network_int8_fp16_kv3_2_iof32_L2ON.yaml --images_dir=example_images  

Warning: For understandability, this example only works with 1 input and 1 output networks.
Warning: As 5 instances are running in parallel and independently, prints to the terminal coming from each cluster may overlap.

3.6. Pipelining example
-----------------------
In this example we show how one can try to pipeline the transfers of data between the host and the MPPA.

The pipelining_example.py is a wrapper for the pipeling_example.cpp. The .py file is the same as the one used for simple example.

// Understanding Pipeline Depth
Recall that NN inference is based on three main OpenCL kernels, sequentially enqueued in the command queue:
- Write the frame on the MPPA -- OpenCL enqueueWrite
- Process the Frame -- OpenCL enqueueNDRange
- Read the frame from the MPPA -- OpenCL enqueueRead
We define the pipeline depth as being the maximum number of OpenCL kernels enqueued during one iteration of the pipeline.
In our case, our pipeline depth is equal to 3, since we simultaneously have: 1 enqueueRead, 1 processFrame, 1 enqueueWrite.

By using a pipelining approach, we minimize the time where the MPPA is idle.
Indeed, when processing a group of frames, the frames required for the next processFrame are being sent to the MPPA.
Therefore, data is always immediately available for each call to processFrame.
Pipelining is often a good method for maximising the performance of a host application.

Below, we show what a pipeline would look like if we were to process frames by bunches of size 5 on a dataset of 28 images.

Legend:
W -> enqueueWrite Kernel
P -> processFrame Kernel
R -> enqueueRead Kernel

K[N; N+M] -> any type of kernel K operating on frames ranging between N and N+M. e.g. W[10;14] = write frames 10 to 14. 

         | Prologue1    | Prologue2    | Loop 0       | Loop 1       | Loop 2       | Loop 3       | Epilogue 1   | Epilogue2    |
         | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
         | iterations=0 | iterations=1 | iterations=2 | iterations=3 | iterations=4 | iterations=5 | iterations=6 | iterations=7 |
| ------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| Pipe 0 | W[0;4]       | P[0;4]       | R[0;4]       | W[15;19]     | P[15;19]     | R[15;19]     |              |              |
| Pipe 1 |              | W[5;9]       | P[5;9]       | R[5;9]       | W[20;24]     | P[20;24]     | R[20;24]     |              |
| Pipe 2 |              |              | W[10;14]     | P[10;14]     | R[10;14]     | W[25;27]     | P[25;27]     | R[25;27]     |
| ------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |

run:
$ cd kann_examples/
$ python3 pipelining_example/pipelining_example.py <path_to_compiled_kann_cpp> <path_to_yaml> --images_dir=<path_to_images>  

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50

$ python3 pipelining_example/pipelining_example.py ../output/bin/pipelining_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --images_dir=example_images  

3.7. Multi Device examples:
---------------------------
3.7.1. Single Process Multi Thread example
------------------------------------------
This example shows how to parallelize the offloading of a neural network on multiple devices, using multithreading with one thread per device.
This example is compatible with "single device" setup (e.g. K300) or "multiple device" setup (e.g. TC4).
The offloading algorithm used is the same one as implemented in simple_example.
In the main function, we create a host buffer containing all the frames to process.
Every time a thread goes to compute a frame, it increments a shared counter called "frame_offset". 
WARNING: if number of frames to process is the same order of magnitude as number of MPPAs, some MPPAs might process no frames (due to multithreading concurrency).

run:
$ cd kann_examples/
$ python3 multi_device_examples/single_process_multi_thread.py <path_to_compiled_kann_cpp> <path_to_yaml> --images_dir=<path_to_images> 

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/UNet2D_Tiny_Med/onnx/network_fp16.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50 

$ python3 multi_device_examples/single_process_multi_thread.py ../output/bin/single_process_multi_thread_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/UNet2D_Tiny_Med/onnx/network_fp16.yaml --images_dir=example_images

3.7.2. Multi Process Single Thread example
------------------------------------------
This example shows how one can create different independent processes on one (or more) devices, with one process per MPPA.
This example is not compatible with "single device" setup (e.g. K300) but it is compatible with "multiple device" setup (e.g. TC4).
All the rationale is done in the multi_process_single_thread.py. We list all available devices by looking at the machine's /mppa directory.
We then offload the compiled simple_example.cpp (cf. section 3.3.) on each available device.

run:
$ cd kann_examples/
$ python3 multi_device_examples/multi_process_single_thread.py <path_to_compiled_kann_cpp> <path_to_yaml> --images_dir=<path_to_images> 

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50 

$ python3 multi_device_examples/multi_process_single_thread.py ../output/bin/simple_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --images_dir=example_images

3.7.3. Heterogeneous example (KaNN+OpenCL Whitebox)
---------------------------------------------------
This example shows how to offload a pure OpenCL example on one MPPA, and a KaNN example on another MPPA.
This example is not compatible with "single device" setup (e.g. K300) but it is compatible with "multiple device" setup (e.g. TC4).
For KaNN, we offload the simple_example (cf. section 3.3.).
For OpenCL, we offload the opencl-c_whitebox_example (see section 4.1.).

run:
$ cd kann_examples/
$ python3 multi_device_examples/heterogeneous_example.py <path_to_compiled_kann_cpp> <path_to_yaml> <path_to_compiled_opencl_cpp> <path_to_pocl> --images_dir=<path_to_images>  

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50 

$ python3 multi_device_examples/heterogeneous_example.py ../output/bin/simple_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/YOLO_v5s6_relu/onnx/network_fp16.yaml ../output/bin/opencl-c_whitebox_example ../output/opencl_kernels/opencl-c_whitebox_example.cl.pocl --images_dir=example_images 

3.8. Custom layer example:
---------------------------
This example showcases how to run a neural network using a custom layer in KaNN.
To illustrate how a custom layer works, we are using a SeLU layer as an example.
The SeLU layer is a layer derived from the SimpleMapping layer which does the following computations:
  x -> (scale * x) if (x > 0) else (scale * alpha * (exp(x) - 1))

For this example, that we have created a SeLU class to represent this layer inside the KaNN generator.
More information on how to implement can be found in the KaNN documentation.
The example directory contains the script for the input preprocessing, the .yaml file which contains the configuration of the network and an ONNX model which is used to compare the output.

run:
$ cd kann_examples/
$ python3 utils/generate_random_images.py custom_layer_example/input_sample custom_layer_example/network.yaml --format '.png' --shape 64 64 3 --dtype 'uint8' --range 0 255 --nb_images 1 
$ cd custom_layer_example/
$ ./custom_layer_example.sh input_sample

3.9. Profiling example:
------------------------
In order to understand how the execution time is spent between the different layers of a network, kann provides a profiling solution.
It uses tracepoints logged through pcie, allowing to perform postmortem profiling.
Profiling tracepoints are timestamps fired at the beginning and at the end of each kernel execution at runtime, allowing to compute cycle accurate timings for each kernel.
The following are then linked to each layer of the network through its kann representation. 
Kann profile traces can be visualized with kcachegrind, qcachegrind, or the KaNN viewer.
See kann user manual profiling section for more details on how to understand kcachegrind displayed informations.

Simple profiling example can be done by running:
$ cd kann_examples/
$ python3 utils/generate_random_images.py profiling_example/input_sample ${KALRAY_TOOLCHAIN_DIR}/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 2
$ cd profiling_example/
$ ./profiling_example.sh ${KALRAY_TOOLCHAIN_DIR}/share/kann/kann-neural-networks/UNet2D_Tiny_Med/onnx/network_fp16.yaml input_sample
# Then visualize any *_profile.out in the trace directory
$ kcachegrind trace/Cluster0_kann_profile.out
# Or with KaNN viewer
$ kann profile kernel_timestamps_viewer trace/Cluster0_kann_profile.out

Kann tracepoints can be enabled and disabled at runtime as showcased in profiling_runtime_example.cpp
Profiling runtime example can be executed by running:
$ cd kann_examples/
$ python3 utils/generate_random_images.py profiling_example/input_sample ${KALRAY_TOOLCHAIN_DIR}/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 2
$ cd profiling_example/
$ ./profiling_runtime_example.sh ../../output/bin/profiling_runtime_example ${KALRAY_TOOLCHAIN_DIR}/share/kann/kann-neural-networks/UNet2D_Tiny_Med/onnx/network_fp16.yaml input_sample
# Then visualize any *_profile.out in the trace directory
$ kcachegrind trace/Cluster0_kann_profile.out
# Or with KaNN viewer
$ kann profile kernel_timestamps_viewer trace/Cluster0_kann_profile.out

3.10. Python API example:
-------------------------
This example showcases how to use KaNN generate from the Python API.
It also shows how we can pass arguments and options to the function and customize the network generation on each generate call.
This example will generate directories directly in the folder : kann_examples/python_api_example/

run:
$ python3 kann_examples/python_api_example/python_api_example.py ${KALRAY_TOOLCHAIN_DIR}/share/kann/kann-neural-networks/ResNet50-MLPerf/tflite/network_int8_fp16_kv3_2_iof32_L2ON.yaml

3.11. Input check example:
-------------------------------
This example aims to check the consistency of the inputs processed by a neural network.
After writing the input from host to MPPA and call process frame, it reads this input from MPPA DDR back to host and save it to the mppa_io folder.

run:
$ cd kann_examples/
$ python3 input_check_example/input_check_example.py <path_to_compiled_cpp> <path_to_yaml> --images_dir=<path_to_images> 

e.g.:
# [optional] If you do not have your own set of images 
# Generate 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py example_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50

$ python3 input_check_example/input_check_example.py ../output/bin/input_check_example $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --images_dir=example_images  

Warning: For understandability, this example only works with 1 input and 1 output networks.

3.12. ONNX quantization example:
----------------------------------
This example showcases how to quantize a network with onnx.
We provide 4 files:
       run_quantization.py - which is the script used to quantize a network
       data_reader.py - containing a class used for the calibration dataset
       input_preparator.py - A preprocessing function which is used for both the calibration dataset and executing the network.
       network_int8.yaml - configuration file for the quantized network

To quantize model.onnx, simply use:
$ python3 run_quantization.py --input_model <model.onnx> --output_model <model.quant.onnx> --calibrate_dataset <img_folder> [--per_channel <false/true>]

By default, per_channel is set to false.
The calibration dataset is optional. If not given, we generate 1000 random uniform images with values of range (0,255).
We apply a preprocessing function on each image. The provided preprocessing function is the one used for ResNet or MobileNet.

Note: Onnx recommends preprocessing the network before quantizing using the following command:

$ python3 -m onnxruntime.quantization.preprocess --input model.onnx --output model-infer.onnx

The provided scripts are a modified version of the example given by onnx in:
https://github.com/microsoft/onnxruntime-inference-examples/tree/main/quantization/image_classification/cpu

For more information on how to use ONNX quantization, go to the above page.

e.g.:
# We use one of the provided networks ResNet50 to compress the network
# Generate a calibration dataset of 50 .png images of shape (512,512,3) with dtype uint8 and range (0,255)
$ python3 utils/generate_random_images.py calibration_images $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/network_fp16_b5.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 50

# Quantize model:
$ python3 -m onnxruntime.quantization.preprocess --input $KALRAY_TOOLCHAIN_DIR/share/kann/kann-neural-networks/ResNet50-MLPerf/onnx/model.onnx --output onnx_quantization_example/model-infer.onnx
$ python3 onnx_quantization_example/run_quantization.py --input_model onnx_quantization_example/model-infer.onnx --output_model onnx_quantization_example/model.quant.onnx --calibration_dataset calibration_images/images

# Generate a smaller dataset of 10 images for the inference
$ python3 utils/generate_random_images.py example_images onnx_quantization_example/network_int8.yaml --format '.png' --shape 512 512 3 --dtype 'uint8' --range 0 255 --nb_images 10

# Run network with simple example
$ python3 simple_example/simple_example.py ../output/bin/simple_example onnx_quantization_example/network_int8.yaml --images_dir=example_images

Note:
In order to execute the model with "simple_example", a .yaml configuration file is required.
A simple configuration file (network_int8.yaml) is provided in this example, and it is primarily designed to work with ResNet50.
If you intend to test another network, ensure that the input and output names and shapes correspond to the network you are testing.
Detailed instructions on preparing the network for KaNN and creating your own configuration file are provided in the documentation.

-------------------------------------------------------------------------------
----------------------------4. OpenCL examples---------------------------------
-------------------------------------------------------------------------------
4.1. OpenCL-C Whitebox example
-----------------------------
This example shows how one can offload pure OpenCL kernels on an MPPA.
We create a simple OpenCL-C kernel in opencl-c_whitebox_example.cl which computes the addition of two input arrays x and y into an output array dst.
The opencl-c_whitebox_example.cpp takes care of offloading the OpenCL-C kernel on the MPPA.
The number of points is an argument to the cpp function.

$ ./output/bin/opencl-c_whitebox_example <path_to_pocl_file> <nb_points>

e.g.
$ ./output/bin/opencl-c_whitebox_example output/opencl_kernels/opencl-c_whitebox_example.cl.pocl 10000

-------------------------------------------------------------------------------
-----------------------------5. Misc examples----------------------------------
-------------------------------------------------------------------------------
5.1 PCIe bus / MPPA info example
--------------------------------
This example showcases the extensions that report PCIe bus and MPPA-specific info.
It iterates through all MPPAs (all OpenCL devices), and prints the PCIe bus ID, the flashed firmware version, the position of the MPPA within its board, as well as the chip and board serials.

run:
$ ./output/bin/board_info_extensions

```

## …

…

# Notes from KaNN: Training session

## Example from `kann-models-zoo`

```bash
$ ./generate networks/classifiers/regnet-x-1.6g/onnx/network_f16.yaml -d r1.6

# [INFO] ===> COPYING EXTRA DATA
# [INFO]     ~> Copy '/work1/dangulo/kann-models-zoo/networks/classifiers/regnet-x-1.6g/onnx/input_preparator.py' to './r1.6/input_preparator.py'
# [INFO]     ~> Copy '/work1/dangulo/kann-models-zoo/networks/classifiers/regnet-x-1.6g/onnx/output_preparator' directory to './r1.6/output_preparator'
# [INFO]     ~> Copy '/work1/dangulo/kann-models-zoo/networks/classifiers/regnet-x-1.6g/onnx/classes.txt' to './r1.6/classes.txt'
# [INFO] ===> DUMPING NETWORK'S YAML
# [INFO] ===> KaNN GRAPH CREATION
# [INFO] Neural Network Name : KaNNv5.3.1-RegNet-X-16g-fp16-5c
# [INFO] ===> KaNN GRAPH PARSING
# [WARNING] No module kann_custom_layers found.
# [INFO] Convert to ONNX opset 20...
# [INFO] Optimize ONNX model...
# [INFO] ~> Saving Optimized Model to ./r1.6/optimized-model.onnx
# [INFO] ===> KaNN HIGH-LEVEL TRANSFORMATION AND OPTIMIZATION ON GRAPH
# [INFO]     Optimisation pass: Using Quantized Operations if possible
# [INFO]     Optimisation pass: Setting images layout
# [INFO]         -> 2 transpose layers have been added
# [INFO]     Optimisation pass: Replace max(mul()) by prelu when possible
# [INFO]     Optimisation pass: Quantizing/Converting network
# [INFO]     Optimisation pass: Folding all consecutive scale layers together
# [INFO]     Optimisation pass: Merging ReLUs
# [INFO]         -> Merging ReLUs done: 55/55 removed
# [INFO]     Optimisation pass: Merge consecutive adds to multi-input add
# [INFO]     Optimisation pass: Optimize multi inputs adds
# [INFO]     Optimisation pass: Swap resize and convert layers if possible
# [INFO]     Optimisation pass: Padding images to reduce Convolution kernels calls
# [INFO]     Optimisation pass: Splitting (de)convolutions with lots of weights into concats of (de)convolutions
# [INFO]     Optimisation pass: Putting big image to DDR if image size > threshold_image_to_ddr (=50000000)
# [INFO] ===> KaNN COMPILE
# Allocation: 100%|████████████████████████████| 473/473 [00:00<00:00, 1905.36it/s]
# Generation: 100%|█████████████████████████████| 473/473 [00:10<00:00, 44.32it/s]

# [INFO] 
# [INFO] ===> OPERATION STATISTICS
# [INFO]   flop(s) required:  3.2400 G flop(s)
# [INFO]   fma in convolutions: 1.6191 GFMA(s)
# [INFO] 
# [INFO] ===> PERSISTENT DATA STATISTICS
# [INFO]   # of layers whose parameters are persistent in SMEM:      4/211
# [INFO]   amount of parameters that are persistent in SMEM:    4.1 KB/13.5 MB
# [INFO]   # of layers whose parameters in DDR:                  207/211
# [INFO]   amount of parameters that are in DDR:                13.5 MB/13.5 MB
# [INFO] 
# [INFO] ===> MEMORY STATISTICS
# [INFO]   total transfer from DDR:              24.0 MB
# [INFO]   total transfer to DDR:                4.0 KB
# [INFO]   total broadcast transfers (src/dst):   10.0 MB / 50.0 MB
# [INFO]   detail transfer from DDR:              0: 10.3 MB   1: 3.4 MB    2: 3.4 MB    3: 3.3 MB    4: 3.6 MB    
# [INFO]   detail transfer to DDR:                0: 768 Bs    1: 768 Bs    2: 768 Bs    3: 896 Bs    4: 800 Bs    
# [INFO]   transfer between clusters over NoC: 40.0 MB
# [INFO]   max data sent by a cluster:     10.0 MB
# [INFO]   max data received by a cluster: 13.6 MB
# [INFO]   max cluster operation latencies: 327.8780 Kcycle
# [INFO]   cluster operation latencies: 322.8 Kcycle 316.0 Kcycle 322.0 Kcycle 327.9 Kcycle 204.8 Kcycle

# [INFO] 
# [INFO] ===> COMMAND COUNTS PER CLUSTER
# [INFO]   COMMAND NAME                                    : Cluster 0      | Cluster 1      | Cluster 2      | Cluster 3      | Cluster 4     
# [INFO]   average_tf16_tf16                               :     1[8.9 K]   |     1[8.9 K]   |     1[9.0 K]   |     1[8.9 K]   |     1[9.0 K]  
# [INFO]   broadcast_ddr_data_notif_all                    :   351[0 ]      |     0[0 ]      |     0[0 ]      |     0[0 ]      |     0[0 ]     
# [INFO]   convert_tf16_tf32                               :     3[0 ]      |     3[0 ]      |     3[0 ]      |     3[0 ]      |     3[0 ]     
# [INFO]   convert_tf32_tf16                               :     1[0 ]      |     1[0 ]      |     1[0 ]      |     1[0 ]      |     1[0 ]     
# [INFO]   convolution_v2_f16_generic                      :    89[284.2 M] |    96[421.7 M] |    96[417.0 M] |    96[421.7 M] |    96[408.6 M]
# [INFO]   convolution_v2_f16_half_tile                    :   275[161.6 M] |   308[254.7 M] |   309[245.1 M] |   306[253.4 M] |   314[261.2 M]
# [INFO]   convolution_v2_f16_small_inners_2               :     4[14.1 M]  |     4[15.2 M]  |     4[14.6 M]  |     4[15.2 M]  |     4[15.4 M] 
# [INFO]   convolution_v2_f16_small_inners_3               :     1[4.4 M]   |     1[4.4 M]   |     1[4.6 M]   |     1[4.4 M]   |     1[4.6 M]  
# [INFO]   copy_inter_clus_tu8_tu8                         :    48[0 ]      |    81[0 ]      |    82[0 ]      |    79[0 ]      |    62[0 ]     
# [INFO]   copy_tf16_sf16                                  :    52[0 ]      |    33[0 ]      |    33[0 ]      |    33[0 ]      |    47[0 ]     
# [INFO]   copy_tu8_tu8                                    :     1[0 ]      |     1[0 ]      |     1[0 ]      |     1[0 ]      |     2[0 ]     
# [INFO]   read_data_ddr_3Du8                              :    17[0 ]      |    57[0 ]      |    58[0 ]      |    55[0 ]      |    63[0 ]     
# [INFO]   relu_fma_tf16_tf16_sf16_tf16                    :    18[938.1 K] |    18[1.2 M]   |    18[1.1 M]   |    18[1.2 M]   |    18[1.2 M]  
# [INFO]   reshape_tf16_tf16                               :     0[0 ]      |     0[0 ]      |     0[0 ]      |     0[0 ]      |     1[0 ]     
# [INFO]   send_data_ddr_3Du8                              :     1[0 ]      |     1[0 ]      |     1[0 ]      |     1[0 ]      |     1[0 ]     
# [INFO]   trigger_clus_data_sent                          :    48[0 ]      |    72[0 ]      |    74[0 ]      |    72[0 ]      |    57[0 ]     
# [INFO]   trigger_ready_to_get_data                       :    40[0 ]      |    75[0 ]      |    73[0 ]      |    74[0 ]      |    61[0 ]     
# [INFO]   trigger_ready_to_get_weights                    :     0[0 ]      |   207[0 ]      |   207[0 ]      |   207[0 ]      |   207[0 ]     
# [INFO]   wait_clus_data_sent                             :    21[0 ]      |    32[0 ]      |    33[0 ]      |    35[0 ]      |    29[0 ]     
# [INFO]   wait_notifs_ddr_data_broadcast                  :   351[0 ]      |   351[0 ]      |   351[0 ]      |   351[0 ]      |   351[0 ]     
# [INFO]   wait_ready_to_get_data                          :    48[0 ]      |    72[0 ]      |    74[0 ]      |    72[0 ]      |    57[0 ]     
# [INFO]   wait_ready_to_get_weights                       :   207[0 ]      |     0[0 ]      |     0[0 ]      |     0[0 ]      |     0[0 ]     
# [INFO]   wait_transfers                                  :    18[0 ]      |    58[0 ]      |    59[0 ]      |    56[0 ]      |    64[0 ]     
# [INFO]   TOTAL                                           :  1595          |  1472          |  1479          |  1466          |  1440         

# [INFO] 
# [INFO] ===> SERIALISATION
# [INFO]     ~> Serialization done, params file written to: './r1.6/serialized_params_KaNNv5.3.1-RegNet-X-16g-fp16-5c.bin'
# [INFO]     KaNN compilation completed into: './r1.6'
# [INFO]     ~> Network's yaml dumped at './r1.6/network.dump.yaml'
# [INFO]     ~> All logs generated in './r1.6/log.txt'
```

```bash
$ ./run infer r1.6

# [INFO]: Generating IO dir into /tmp/tmpr_ef7zvm
# [INFO]: [+] Inputs/Outputs directory is located to /tmp/tmpr_ef7zvm
# Running: /work1/dangulo/kaf/kEnv/kvxtools/opt/kalray/accesscore/bin/kann_opencl_cnn /work1/dangulo/kann-models-zoo/r1.6/serialized_params_KaNNv5.3.1-RegNet-X-16g-fp16-5c.bin /tmp/tmpr_ef7zvm
# [INFO]: Done

# [app] Creating instance of KaNN::Service.
#  [KaNN_service] Calling constructor with /work1/dangulo/kann-models-zoo/r1.6/serialized_params_KaNNv5.3.1-RegNet-X-16g-fp16-5c.bin
#  [KaNN_service] Instance "KaNNv5.3.1-RegNet-X-16g-fp16-5c": created
#  [app] Creating an instance of KaNN::Service for a network requiring 5 clusters
#  [app] Accessing default platform
#  [app] Accessing all acceleration devices available on the platform
#  [app] Found 1 devices
#  [app] Accessing the device n°0 in the list
#  [app] Creating a context on the device
#  [app] Requesting 6553600B on device
#  [app] Partitioning the device into sub-devices
#  [app] 1 sub-devices were created
#  [app] Accessing the first sub-device in the list
#  [app] Creating the command queue...
#  [app] Initialising device...
#  [KaNN_service] Using custom $KANN_POCL_FILE file as OpenCL program.
#  [KaNN_service] The following .pocl file will be used : /work1/dangulo/kaf/kEnv/kvxtools/opt/kalray/accesscore/kvx-cos/lib/kv3-2/KAF/services/mppa_kann_opencl.cl.pocl
#  [KaNN_service] OpenCL program created from /work1/dangulo/kaf/kEnv/kvxtools/opt/kalray/accesscore/kvx-cos/lib/kv3-2/KAF/services/mppa_kann_opencl.cl.pocl
#  [KaNN_service] Instance "KaNNv5.3.1-RegNet-X-16g-fp16-5c": initDevice done
#  [app] KaNN::service version: 1.1.0
#  [app][host] Performance of frame 1: 1.9212 ms - 520.507 fps
#  [app][host] Performance of frame 2: 1.81314 ms - 551.529 fps
#  [app][host] Performance of frame 3: 1.81535 ms - 550.859 fps
#  [app][host] Performance of frame 4: 1.81199 ms - 551.879 fps
#  [app][host] Performance of frame 5: 1.81167 ms - 551.977 fps
#  [app][host] Performance of frame 6: 1.81265 ms - 551.678 fps
#  [app][host] Performance of frame 7: 1.81676 ms - 550.43 fps
#  [app][host] Performance of frame 8: 1.81504 ms - 550.953 fps
#  [app][host] Performance of frame 9: 1.7814 ms - 561.355 fps
#  [app][host] Performance of frame 10: 1.81335 ms - 551.465 fps
 
#  Total: 1876698 cycles are required for a single process_frame (result averaged over 10 frames).
#  Timings of the last frame:
#                           clusters| clus_0 |   %| clus_1 |   %| clus_2 |   %| clus_3 |   %| clus_4 |   %|
#                              total| 1860298|100%| 1861170|100%| 1862008|100%| 1863970|100%| 1864026|100%|
#                  average_tf16_tf16|   53060|  3%|   56378|  3%|   56501|  3%|   56183|  3%|   56969|  3%|
#       broadcast_ddr_data_notif_all|  130891|  7%|       0|  0%|       0|  0%|       0|  0%|       0|  0%|
#                  convert_tf16_tf32|   15606|  1%|   15868|  1%|   15987|  1%|   16172|  1%|   15775|  1%|
#                  convert_tf32_tf16|    2954|  0%|    2831|  0%|    2951|  0%|    3338|  0%|    3241|  0%|
#         convolution_v2_f16_generic|  214047| 12%|  291709| 16%|  288580| 15%|  288974| 16%|  288650| 15%|
#       convolution_v2_f16_half_tile|  291292| 16%|  383866| 21%|  378061| 20%|  382335| 21%|  392645| 21%|
#  convolution_v2_f16_small_inners_2|   15745|  1%|   16119|  1%|   15531|  1%|   16031|  1%|   17132|  1%|
#  convolution_v2_f16_small_inners_3|    9017|  0%|    8351|  0%|    8880|  0%|    9049|  0%|    8603|  0%|
#            copy_inter_clus_tu8_tu8|   68813|  4%|  102283|  5%|  109167|  6%|  109656|  6%|   80314|  4%|
#                     copy_tf16_sf16|   34139|  2%|   13373|  1%|   13600|  1%|   13493|  1%|   27474|  1%|
#                       copy_tu8_tu8|    3417|  0%|    2626|  0%|    3235|  0%|    3657|  0%|    4876|  0%|
#                 read_data_ddr_3Du8|    6542|  0%|   21820|  1%|   22189|  1%|   21133|  1%|   24773|  1%|
#       relu_fma_tf16_tf16_sf16_tf16|   62074|  3%|   75287|  4%|   72402|  4%|   74744|  4%|   76822|  4%|
#                  reshape_tf16_tf16|       0|  0%|       0|  0%|       0|  0%|       0|  0%|   24395|  1%|
#                 send_data_ddr_3Du8|     755|  0%|     554|  0%|     515|  0%|     524|  0%|     544|  0%|
#             trigger_clus_data_sent|   10736|  1%|   16205|  1%|   16666|  1%|   16149|  1%|   13014|  1%|
#          trigger_ready_to_get_data|    9194|  0%|   17011|  1%|   16406|  1%|   16589|  1%|   13683|  1%|
#       trigger_ready_to_get_weights|       0|  0%|   46756|  3%|   46615|  3%|   46575|  2%|   46373|  2%|
#                wait_clus_data_sent|   65662|  4%|  183151| 10%|  100477|  5%|   86513|  5%|   57815|  3%|
#     wait_notifs_ddr_data_broadcast|  210170| 11%|  208523| 11%|  284425| 15%|  288581| 15%|  296574| 16%|
#             wait_ready_to_get_data|   11838|  1%|   17680|  1%|   21391|  1%|   21631|  1%|   17436|  1%|
#          wait_ready_to_get_weights|  442648| 24%|       0|  0%|       0|  0%|       0|  0%|       0|  0%|
#                     wait_transfers|   17623|  1%|  199385| 11%|  204253| 11%|  218093| 12%|  216825| 12%|
#                              other|  167093|  9%|  156036|  8%|  156685|  8%|  155670|  8%|  153032|  8%|
#                  get_new_code_bloc|   16982|  1%|   25358|  1%|   27491|  1%|   18880|  1%|   27061|  1%|
#                 l2 miss last frame|     152|  0%|   24050|  1%|     130|  0%|   23955|  1%|   24659|  1%|
#                              PMC_0| 1857405|100%| 1857978|100%| 1858891|100%| 1860652|100%| 1860987|100%|
#                              PMC_1|     896|  0%|     829|  0%|     829|  0%|     819|  0%|     902|  0%|
#                              PMC_2|   16001|  1%|   16374|  1%|   16075|  1%|   16323|  1%|   17018|  1%|
#                              PMC_3|    2248|  0%|    2309|  0%|    2304|  0%|    2284|  0%|    2318|  0%|
#  [KaNN_service] Instance "KaNNv5.3.1-RegNet-X-16g-fp16-5c": terminateDevice done
#  [app] Exiting

# [INFO]: Log is available at inference_r1.6_2.log
# [INFO]: ***********************************
# [INFO]: DATA EXTRACTED FROM INFERENCE LOG:
# [INFO]: ***********************************
# [INFO]: Batch size / query:       1
# [INFO]: Number of queries:       10
# [INFO]: PERF HOST (ms):        1.82 ms
# [INFO]: PERF HOST (qps):     549.26 qps
# [INFO]: PERF HOST (fps):     549.26 fps
# [INFO]: PERF DEVICE (ms):      1.71 ms
# [INFO]: PERF DEVICE (qps):   586.14 qps
# [INFO]: PERF DEVICE (fps):   586.14 fps
# [INFO]: ***********************************
# [INFO]: Removing IO dir /tmp/tmpr_ef7zvm
# [INFO]: Done
```

```bash
./run demo r1.6 utils/sources/dog.jpg --no-replay --no-display -v

# [KaNN Demo] Video backend: FFMPEG
# [KaNN Demo] <classes_file> at /work1/dangulo/kann-models-zoo/r1.6/classes.txt contains 1000 classes
#   >> [Post-proc] prediction: 0.757 - n02099601 golden retriever
# [KaNN Demo] frame:2/0   read: 0.02ms    pre: 1.94ms     onnx: 8.61ms    post: 0.38ms    draw: 0.03ms    show: 0.00ms    total: 10.98ms (91.0fps)
```

```bash
./run demo r1.6 utils/sources/dog.jpg --no-replay --no-display -v -d cpu

# [KaNN Demo] Video backend: FFMPEG
# [KaNN Demo] <classes_file> at /work1/dangulo/kann-models-zoo/r1.6/classes.txt contains 1000 classes
#  >> [Post-proc] prediction: 0.757 - n02099601 golden retriever
# [KaNN Demo] frame:2/0   read: 0.01ms    pre: 2.52ms     onnx: 10.04ms   post: 0.39ms    draw: 0.03ms    show: 0.00ms    total: 13.00ms (76.9fps)
```

## Efficiency computation

Efficiency of execution of a program on a hardware is a measure between $0$ and $1$ representing how close we are to the **peak** theoretical execution time. We want to be as close to $1$ as possible. It is computed as follows:

$$
\text{Efficiency} = \frac{\text{Theoretical Execution Time}}{\text{Actual Execution Time}} 
$$

For the theoretical time term, we need to retrieve the flops required from the `kann generate` logs. Then, we need to retrieve the theoretical hardware flops. The theoretical execution time is then:

$$
\text{Theoretical Execution Time = } \frac{\text{FLOPS required}}{\text{Reference FLOPS}}
$$

As an example, the flops required in the previous example in `kann-models-zoo` is 3.24 GFLOPS, and the reference FLOPS is 25 TFLOPS for MPPA. This gives then:

$$
\text{Theoretical Execution Time = } \frac{\text{3.24 GFLOPS}}{\text{25 TFLOPS}} = \frac{\text{3.24 GFLOPS}}{\text{25000 GFLOPS}} = 0.000129 s
$$

So theoretically it takes $0.000129s$ or $129 \mu s$ to execute the CNN algorithm. 

When it comes to the actual execution time, we need to look again at the `kann generate` log, particularly the memory statistics section.

```bash
# [INFO] ===> MEMORY STATISTICS
# ...
# [INFO]   max cluster operation latencies: 327.8780 Kcycle
# [INFO]   cluster operation latencies: 322.8 Kcycle 316.0 Kcycle 322.0 Kcycle 327.9 Kcycle 204.8 Kcycle
```

A kcycle or kilo-cycle is a measure of time based on the number of processor clock cycles, with each kcycle representing 1,000 clock cycles. 

…

$$
\text{Actual Execution Time} = ...
$$

Finally, putting everything together:

$$
\text{Efficiency} = \frac{129 \mu s}{\text{327 kcycles}} = 39\%
$$

NB PE * (taille matrix) 4 * 8 * 4 * 2 (FLOPS) * MPPA FREQ (1,1 GHZ)

1GLOPS/s / 21e^3 TFLOPS/s * (1 - loss)tableau: model (glops / params), t_host (init, fetch…), t_dpu (preprosc, processing)

t_host == t_mpa + t_pcie

t_mppa = 990 kc