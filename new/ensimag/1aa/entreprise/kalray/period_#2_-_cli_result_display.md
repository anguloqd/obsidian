# Period #2 - CLI result display

> [!important] ❗
>
> - [x]  Uniformiser les outputs des Object-detection
> - [ ]  Modifier unit_tests.py pour reporter les résultats des obj-det et seg
> - [ ]  Ajouter des critères dans unit_tests pour confirmer dans les deux MPPA et CPU si les labels sont égaux et si la différence de confiance (proba) est suffisamment petite
> - [ ]  Montrer les résultats de Segmentation

- [ ]  Object-detection:
    - [x]  efficientdet-d0
    - [x]  retinanet-resnet50
    - [x]  retinanet-resnet50-mlperf
    - [x]  retinanet-resnet101
    - [x]  yolov3
    - [x]  yolov4-csp-mish
    - [x]  yolov4-csp-relu
    - [x]  yolov4-csp-s-mish
    - [x]  yolov4-csp-s-relu
    - [x]  yolov4-csp-x-relu
    - [x]  yolov5m6-relu
    - [x]  yolov5s
    - [x]  yolov5s6-relu
    - [x]  yolov7
    - [x]  yolov7-tiny
    - [x]  yolov8l
    - [x]  yolov8m
    - [x]  yolov8n
    - [x]  yolov8n-relu
    - [x]  yolov8n-relu-vga
    - [x]  yolov8s
    - [x]  yolov8s-relu
    - [x]  yolov9m
    - [x]  yolov9s
    - [x]  yolov9t
    - [ ]  TF: ssd-mobilenet-v1-mlperf
    - [ ]  TF: ssd-mobilenet-v2
    - [ ]  TF: ssd-resnet34-mlperf
    - [ ]  TF: yolov3-tiny
    - [ ]  ERROR: faster-rcnn-rn50
    - [ ]  ERROR: yolov4-tiny
    - [ ]  ERROR: yolov4

```bash
# From /work1/dangulo
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
kaf-activate-env
pip install ultralytics
yolo --help
yolo val model=yolo11n.pt data=coco8.yaml batch=1 imgsz=640

val: Scanning /work1/dangulo/ultralytics/datasets/coco8/labels/val.cache... 4 images, 0 backgrounds, 0 corrupt: 100%|██████████| 4/4 [00:00<?, ?it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 4/4 [00:00<00:00, 25.80it/s]
                   all          4         17      0.574       0.85      0.815       0.61
                person          3         10       0.57        0.6      0.657       0.31
                   dog          1          1      0.527          1      0.995      0.796
                 horse          1          2      0.684          1      0.995      0.536
              elephant          1          2      0.281        0.5      0.254      0.127
              umbrella          1          1      0.554          1      0.995      0.995
          potted plant          1          1      0.825          1      0.995      0.895
```

Ok donc, pour rendre unit_tests.py plus générique, il faut déjà :

- Dans la fonction post-process, dans `if dbg:` pour le score sous forme de variable numpy “`p`”, il faut faire `p.tofile(…)`. Puis, depuis la fonction `get_prediction_demo()` allez le récupérer. La finalité est de “faire plus propre” et de parser le vecteur de sortie (`label`, `conf`, `bbox`) en utilisant un `numpy.fromfile()` et non pas en parsant un log de texte.
- TODO: creer dir dans `valid/jenkins/single_tests…/` qui s’apellent “scores” et “labels” pour aller remplace le dossier “log”. C’est de là qu’on va aller écrire puis aller lire.
- Rendre le plus générique possible de coeur de boucle de unit_tests.py !!!
- Ne pas modifier `kann-video-demo.py`
- `check_outputs()` qui fait “`kann … --check`” pour checker les scores, puis tu checkes les bbox et le label via le log.