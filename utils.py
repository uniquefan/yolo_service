import yaml


def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def post_process(predictions, idx2label_fa,idx2label_en):
    results = []
    for pred in predictions:
        results.append([
            {
                "bbox": bbox,
                "prob": conf,
                "cls": cls,
                "label_fa": idx2label_fa[cls],
                "label_en": idx2label_en[cls]
            }
            for bbox, conf, cls in zip(pred.boxes.xyxy.tolist(), pred.boxes.conf.tolist(), pred.boxes.cls.tolist())
        ])
    return results
