# Postprocesses

Old postprocess files : __init__ and output_processor.py. EVERY FUNCTION IN `OUT_PROC.PY`.

- post-process:
    - get_classes
    - sess.run()
    - filter_out_boxes
        - xywh2xyxy
        - nms
    - process_detections
        - scale_coords
            - clip_coords
        - plot_box

New postprocess files : __init__, cmap.py, output_processor.py, utils.py.

- post_process (out_proc.py)
    - get_classes (utils.py)
    - process_detections (utils.py)
        - distFocalLoss (class)
        - detect
            - dist2bbox
            - make_anchors
        - plot_box
        - scale_coords
            - clip_coords
        - non_max_suppression
            - xywh2xyxy
            - nms
        - nms

---

The core issue lies in the detect function within utils.py. This function was copied from the YOLOv8 implementation and assumes the output format specific to YOLOv8, which uses Distribution Focal Loss (DFL) resulting in output shapes like `[batch, height, width, 4 * reg_max + num_classes]`.

YOLOv5, however, has a different output structure, typically `[batch, num_anchors, height, width, 5 + num_classes]` (or permutations thereof depending on export settings), where `5` represents x, y, w, h, objectness_confidence. The detect function in yolov5s-new incorrectly interprets the YOLOv5 output using YOLOv8's DFL logic (dfl and dist2bbox).

Furthermore, the original working implementation in output_preparator.py relies on a separate ONNX model (`yolov5s.postproc.onnx`) executed via sess.run(None, nn_outputs) to perform the complex decoding and NMS steps. The yolov5s-new approach, mimicking yolov8l, aims to do this decoding in Python.

To fix utils.py, you need to replace the current detect function with one that correctly decodes the standard YOLOv5 output format. This involves:

1. **Understanding the exact output format:** Check the `onnx_model` specified in network.dump.yaml and its corresponding `output_nodes_shape`. The shapes `[80, 1, 80, 255]`, `[40, 1, 40, 255]`, `[20, 1, 20, 255]` suggest a format like `[height, batch, width, num_anchors * (5 + num_classes)]` or similar, where `num_anchors=3` and `num_classes=80`.
2. **Implementing YOLOv5 decoding:**
    - Iterate through each output tensor in nn_outputs.
    - Reshape each tensor to separate anchor predictions, grid cell predictions, and class/box information (e.g., `[batch, num_anchors, height, width, 5 + num_classes]`).
    - Create anchor grids and grid cell coordinates.
    - Apply sigmoid function to x, y offsets, `objectness`, and class scores.
    - Decode w, h using anchor dimensions and exponential function.
    - Combine x, y, w, h to get bounding boxes relative to the input image size.
    - Concatenate predictions from all output scales.
3. **Adjust process_detections:** Ensure the output of your new YOLOv5 decoding logic is correctly passed to the non_max_suppression function. The NMS function itself might be largely compatible, as it expects boxes (xyxy), scores, and an IOU threshold.

You need to replace the detect function and remove the dfl dependency in utils.py with logic appropriate for the YOLOv5 output structure defined in network.dump.yaml.