PROJECT_PATH=/root/autodl-tmp/stable-zero123-inference
export PYTHONPATH="$PYTHONPATH:$PROJECT_PATH"

BACKBONE_PATH=${PROJECT_PATH}/threestudio


python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/pm_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/dalle2_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/demo4_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/pm_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/sit_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/dalle8_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/monalisa_rgba.png

python ${BACKBONE_PATH}/launch.py --config ${PROJECT_PATH}/threestudio/configs/stable-zero123.yaml \
--train --gpu 0 data.image_path=${PROJECT_PATH}/load/images/single_source_rgba.png