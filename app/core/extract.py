from paddlex import create_pipeline
from PIL import Image
import numpy as np

pipeline = create_pipeline(pipeline="config/table_config.yaml",
                           use_hpip=True)

image = Image.open("core/image.png") 

# image to numpy array
image = np.array(image)
print(image.shape) # (612, 485, 3)

# Table Recognition
# output = pipeline.predict(
#     input=image,
#     use_doc_orientation_classify=False,
#     use_doc_unwarping=False,
#     use_table_cells_ocr_results=True
# )

# for res in output:
#     res.print()
#     res.save_to_img("./output/")
#     res.save_to_xlsx("./output/")
#     res.save_to_html("./output/")
#     res.save_to_json("./output/")