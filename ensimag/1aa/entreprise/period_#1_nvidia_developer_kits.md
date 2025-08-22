# Period #1 - NVidia Developer Kits

# NVidia Jetson AGX Orin

## SSH stuff

```bash
ssh-copy-id -i ~/.ssh/dangulo_win dangulo@ws2405
ssh -X accesscore@jetson01
ssh-keyscan jetson01 >> /nfs/home/dangulo/.ssh/known_hosts
ssh-copy-id -i ~/.ssh/dangulo_win jetson01
chmod 600 dangulo_win
chmod 600 dangulo_win.pub
```

## Commands executed

```bash
nvidia-smi # to check if AGX Orin is running correctly
dpkg-query --show nvidia-jetpack # check if JetPack is installed correctly

sudo apt-get update
sudo apt-get install nvidia-tensorrt

sudo apt-get update
sudo apt-get install python3-pip
pip3 --version

pip3 install onnxruntime

# ---------------------------------

# accesscore@jetson01:~/kann-models-zoo$
trtexec --onnx=./resnet50/optimized-model.onnx --saveEngine=resnet50_tf32.trt
trtexec --loadEngine=resnet50_tf32.trt
trtexec --onnx=./resnet50/optimized-model.onnx --saveEngine=resnet50_fp16.trt --verbose --fp16
trtexec --loadEngine=resnet50_fp16.trt
trtexec --onnx=./resnet50/optimized-model.onnx --saveEngine=resnet50_fp16.trt --verbose --fp16 --optShapes=5x3x224x224
pip install sbi4onnx
pip install onnx
pip install onnx_graphsurgeon
pip install onnxsim
sbi4onnx -if=resnet50/optimized-model.onnx -h
sbi4onnx -if=./resnet50/optimized-model.onnx -of=resnet50_n.onnx -ics N
onnxsim resnet50_n.onnx resnet50_10.onnx --overwrite-input-shape=10,3,224,224
trtexec --onnx=resnet50_10.onnx --saveEngine=resnet50_10_fp16.trt --verbose --fp16
trtexec --loadEngine=resnet50_10_fp16.trt --batch-size=10
trtexec --loadEngine=resnet50_10_fp16.trt

#----------

# We were trying to change the power cap of the AGX Orin

sudo nvpmodel -q
sudo nvpmodel -q -f pm.conf
sudo nvpmodel -f pm.conf
sudo nvpmodel -m 1
cat /var/lib/nvpmodel/status
sudo /usr/sbin/nvpmodel -m 0
car /etc/nvpmodel.conf
nvpmodel --verbose -p -f /etc/nvpmodel.conf
sudo nvpmodel --verbose -p -f /etc/nvpmodel.conf
sudo nvpmodel -m 1
cat /etc/nvpmodel.conf
sudo nvpmodel -q --verbose
sudo nvpmodel -m 0

#----------

# 26/11/2024
# accesscore@jetson01:~/kann-models-zoo$

# plus tôt, j'ai pu faire tourner avec useDLACore=1.
# le detail est de forcer le build avec "python valid/benchmark.py ... -f"

# ici je veux essayer de faire tourner à int8
# je prends un reseau avec network_i8.yaml (lequel finalement n'est pas important)
# ((quelle merde j'ai fait avec mobilenet-v2 ?))

python valid/benchmark.py --arch=agx-orin classifiers -i mobilenet-v2
python valid/benchmark.py --arch=agx-orin classifiers -i mobilenet-v2 -f
trtexec \
	--onnx=/home/accesscore/kann-models-zoo/valid/gpu/.tmp_agx_orin/trt_generated/mobilenet-v2_onnx_i8/mobilenetv2-q_batchN.onnx \
	--saveEngine=/home/accesscore/kann-models-zoo/valid/gpu/.tmp_agx_orin/trt_generated/mobilenet-v2_onnx_i8/trtEngine-DLA-int8-batch1.trt \
	--optShapes=images:1x3x224x224 --int8 --device=0 --verbose --skipInference

# je me rends compte de que cet approche ne marche pas pour aucun classifier,
# seul efficientnet-b4 fait de l'inference 
python valid/benchmark.py --arch=agx-orin classifiers -f
python valid/benchmark.py --arch=agx-orin classifiers -i efficientnet-b4 -f

# commandes de quentin (resnet50v1.5 est le meilleur pour comparer)
## pour juste builder l'engine en int8, sans DLA
trtexec \
	--onnx=./networks/classifiers/resnet50v1.5/onnx/models/resnet50-v1.5.onnx  \
	--saveEngine=resnet50v1.5_int8.trt \
	--int8 --fp16 --verbose --skipInference

## pour juste faire de l'inférence en int8, sans DLA
trtexec --loadEngine=resnet50v1.5_int8.trt

## pour builder en int8 et inférer, avec DLA
trtexec \
	--onnx=./networks/classifiers/resnet50v1.5/onnx/models/resnet50-v1.5.onnx \
	--saveEngine=resnet50v1.5_int8_dla.trt --useDLACore=0 --allowGPUFallback \
	--int8 --fp16 --verbose

## pour builder en fp16 et inférer, sans DLA
trtexec \
	--onnx=./networks/classifiers/resnet50v1.5/onnx/models/resnet50-v1.5.onnx \
	--saveEngine=resnet50v1.5_fp16.trt --fp16 --verbose

## pour builder en fp16 et inférer, avec DLA
trtexec \
	--onnx=./networks/classifiers/resnet50v1.5/onnx/models/resnet50-v1.5.onnx \
	--saveEngine=resnet50v1.5_fp16_dla.trt --useDLACore=0 --allowGPUFallback \
	--int8 --fp16 --verbose
```

## `trt_inference.py` (that I wrote)

```python
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
import time

# Initialize TensorRT logger
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

def main():
    # Load the TensorRT engine
    engine_path = "./resnet50/resnet50-opt.trt"  # Modify this path if necessary
    with open(engine_path, "rb") as f:
        engine_data = f.read()
    runtime = trt.Runtime(TRT_LOGGER)
    engine = runtime.deserialize_cuda_engine(engine_data)

    # Retrieve the correct tensor names and expected shapes
    input_tensor_name = None
    output_tensor_name = None
    for i in range(engine.num_io_tensors):
        tensor_name = engine.get_tensor_name(i)
        if engine.get_tensor_mode(tensor_name) == trt.TensorIOMode.INPUT:
            input_tensor_name = tensor_name
            print("Input tensor name:", input_tensor_name)
            expected_input_shape = engine.get_tensor_shape(tensor_name)
            print("Expected input shape:", expected_input_shape)
        elif engine.get_tensor_mode(tensor_name) == trt.TensorIOMode.OUTPUT:
            output_tensor_name = tensor_name
            print("Output tensor name:", output_tensor_name)
            expected_output_shape = engine.get_tensor_shape(tensor_name)
            print("Expected output shape:", expected_output_shape)

    # Ensure we have valid names for input and output
    if input_tensor_name is None or output_tensor_name is None:
        raise ValueError("Failed to find valid input and/or output tensor names.")

    # Create an execution context
    context = engine.create_execution_context()

    # Allocate buffers for inputs and outputs
    input_shape = expected_input_shape  # Use the expected input shape directly
    output_shape = expected_output_shape  # Use the expected output shape directly
    input_size = int(np.prod(input_shape) * np.float32().nbytes)
    output_size = int(np.prod(output_shape) * np.float32().nbytes)

    # Allocate device memory
    d_input = cuda.mem_alloc(input_size)
    d_output = cuda.mem_alloc(output_size)

    # Allocate host memory
    h_input = np.random.random(input_shape).astype(np.float32)
    h_output = np.empty(output_shape, dtype=np.float32)

    # Create a CUDA stream
    stream = cuda.Stream()

    # Transfer input data to device
    cuda.memcpy_htod_async(d_input, h_input, stream)

    # Set input and output tensor addresses using the retrieved names
    context.set_input_shape(input_tensor_name, input_shape)
    context.set_tensor_address(input_tensor_name, int(d_input))
    context.set_tensor_address(output_tensor_name, int(d_output))

    # Start time
    start_time = time.time()

    # Execute asynchronously
    context.execute_async_v3(stream_handle=stream.handle)

    # Transfer predictions back to host
    cuda.memcpy_dtoh_async(h_output, d_output, stream)

    # Synchronize the stream to ensure inference is complete
    stream.synchronize()

    # End timing after inference is complete
    end_time = time.time()  # End time
    inference_time = end_time - start_time  # Calculate inference duration

    # Output results and performance logs
    print("Inference output:", h_output)
    print(f"Inference time: {inference_time:.4f} seconds")

if __name__ == '__main__':
    main()

```

## To execute `benchmark.py` in background

```bash
# The command of interest to execute
$ python valid/benchmark.py --arch=agx-orin all -b 1 2 4 8 16 32

$ python valid/benchmark.py --arch=agx-orin all -b 1 2 4 8 16 32 2>&1 > log.txt &
$ tail -n 5 log.txt

$ jobs
$ disown %1
$ ps aux | grep benchmark

$ sleep 200 # this was just an example
$ bg 1
$ jobs
$ disown %1

$ ps
$ ps -h
```

## Hardware information

[www.nvidia.com](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf)

## (?)

Performing inference on a Convolutional Neural Network (CNN) model stored in an ONNX file on the **Nvidia Jetson AGX Orin** is straightforward, thanks to the hardware acceleration and the software tools available on the platform. Here’s a step-by-step guide to help you load and run your ONNX model on the AGX Orin using **TensorRT**, Nvidia's high-performance deep learning inference library.

### **Steps to Perform Inference on the Jetson AGX Orin Using an ONNX Model**

### 1. **Set Up Your Jetson AGX Orin**

Ensure your **Jetson AGX Orin** is set up correctly with **JetPack** installed (which includes libraries like TensorRT, CUDA, cuDNN, and other essential dependencies). You should also have the ONNX runtime installed for loading and running the ONNX model.

You can verify your setup by running:

```bash
nvidia-smi
```

This should show the GPU information, confirming that the AGX Orin is running and ready to perform inference.

### 2. **Install Required Dependencies**

If you don't already have the necessary libraries, you need to install them. These include **TensorRT**, **onnx**, and **onnxruntime**.

1. **TensorRT**: Nvidia provides TensorRT as part of the JetPack SDK. Ensure you have it by running:
    
    ```bash
    sudo apt-get install libnvinfer8 libnvinfer-dev
    ```
    
2. **ONNX Runtime**: Install ONNX runtime (if not installed):
    
    ```bash
    pip install onnxruntime
    ```
    
3. **ONNX**: If you need to install ONNX, use:
    
    ```bash
    pip install onnx
    ```
    
4. **Numpy (if required)**:
    
    ```bash
    pip install numpy
    ```
    

### 3. **Convert the ONNX Model to a TensorRT Engine (Optional for Performance)**

While you can directly use the ONNX model with ONNX Runtime, you can gain significant performance improvements on the Jetson AGX Orin by using **TensorRT** to convert the model into a more optimized engine for inference.

To convert your ONNX model into a TensorRT engine, you can use the **trtexec** tool or the **TensorRT Python API**.

- **Using `trtexec` (command-line tool)**:
The `trtexec` tool converts an ONNX model to a TensorRT engine.
    
    ```bash
    trtexec --onnx=model.onnx --saveEngine=model.trt
    ```
    
    This will generate a TensorRT engine (`model.trt`), which can be loaded and used for inference.
    
- **Using TensorRT Python API**:
You can also load an ONNX model directly into TensorRT using the Python API. Here’s an example Python script to do this:
    
    ```python
    import tensorrt as trt
    import onnx
    import onnx_tensorrt.backend as backend
    
    # Load your ONNX model
    model_path = 'model.onnx'
    onnx_model = onnx.load(model_path)
    
    # Convert the ONNX model to TensorRT engine
    engine = backend.prepare(onnx_model, device='GPU')
    
    # Perform inference
    input_data = ...  # Your input data
    result = engine.run(input_data)
    ```
    

### 4. **Load the ONNX Model and Perform Inference**

You can now run inference on the Jetson AGX Orin using either the **ONNX Runtime** or **TensorRT**.

### **Using ONNX Runtime**:

Here’s a basic example of performing inference using **ONNX Runtime** on your model:

```python
import onnxruntime as ort
import numpy as np

# Load the ONNX model
onnx_model_path = "model.onnx"
sess = ort.InferenceSession(onnx_model_path)

# Prepare your input data (replace this with actual input preprocessing)
# Example: Assuming the model expects a 1x3x224x224 input (e.g., for ImageNet)
input_data = np.random.random((1, 3, 224, 224)).astype(np.float32)

# Get input name(s) from the model
input_name = sess.get_inputs()[0].name

# Perform inference
outputs = sess.run(None, {input_name: input_data})

# Process the output (depends on your model)
print(outputs[0])  # Assuming your model has one output
```

### **Using TensorRT (via Python API)**:

Once you've converted the ONNX model to a TensorRT engine, you can use the following approach to run inference:

```python
import tensorrt as trt
import numpy as np

# Load the TensorRT engine
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
engine_path = "model.trt"
with open(engine_path, "rb") as f:
    engine_data = f.read()

runtime = trt.Runtime(TRT_LOGGER)
engine = runtime.deserialize_cuda_engine(engine_data)

# Create an execution context
context = engine.create_execution_context()

# Prepare input data (depends on the input shape of your model)
input_data = np.random.random((1, 3, 224, 224)).astype(np.float32)
input_size = np.prod(input_data.shape) * input_data.itemsize

# Allocate device memory for input and output
d_input = cuda.mem_alloc(input_size)
d_output = cuda.mem_alloc(engine.max_batch_size * np.prod(engine.get_binding_shape(1)) * np.float32.itemsize)

# Transfer input data to device memory
cuda.memcpy_htod(d_input, input_data)

# Perform inference
context.execute(batch_size=1, bindings=[int(d_input), int(d_output)])

# Retrieve and process output
output_data = np.empty(engine.get_binding_shape(1), dtype=np.float32)
cuda.memcpy_dtoh(output_data, d_output)
print(output_data)
```

### 5. **Optimizing for the Jetson Platform**

To maximize performance, you should also consider the following:

- **Precision Mode**: You can optimize the inference by using lower precision modes (FP16 or INT8), which can be done during the conversion from ONNX to TensorRT using `trtexec` or in the TensorRT API.
- **Dynamic Batching**: If your workload involves processing batches of inputs, TensorRT allows dynamic batching to improve throughput.

### 6. **Monitoring Performance**

You can monitor the performance of your inference tasks using tools like `nvidia-smi` and `tegrastats` to keep track of GPU usage and power consumption:

```bash
nvidia-smi
tegrastats
```

### **Summary**

To perform inference on an ONNX model on the **Jetson AGX Orin**, you can either use **ONNX Runtime** or **TensorRT**. Using TensorRT provides significant performance benefits by optimizing the model for the Jetson platform’s hardware. You can convert the ONNX model to a TensorRT engine for faster inference or directly use ONNX Runtime if you don’t need the optimization step. Both methods are supported on the Jetson platform and leverage its GPU and AI accelerators for high-performance inference.