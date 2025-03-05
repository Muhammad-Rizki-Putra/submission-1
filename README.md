# 📊 E-commerce Public Dataset Dashboard 🚀

## Setup Environment - Anaconda

```bash
conda create --name ecommerce-ds python=3.9
conda activate ecommerce-ds
pip install -r requirements.txt

mkdir ecom_analysis
cd ecom_analysis
pipenv install
pipenv shell
pip install -r requirements.txt

streamlit run dashboard.py
