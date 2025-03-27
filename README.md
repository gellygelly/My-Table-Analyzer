# My-Table-Analyzer
My personal Table Analyzer with RAG

## 환경 설정
### apt install
apt update
apt install -y libgl1-mesa-glx
apt install -y libglib2.0-0
apt install libgomp1

### paddleocr
pip install paddleocr

### paddlepaddle
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

### paddleX
pip install https://paddle-model-ecology.bj.bcebos.com/paddlex/whl/paddlex-3.0.0rc0-py3-none-any.whl

### paddlex HPI(High-Performance Inference Plugins)
paddlex --install hpi-gpu