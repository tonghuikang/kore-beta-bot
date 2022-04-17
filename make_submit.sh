cd src && tar --exclude='*.ipynb' --exclude="*.pyc" -czf ../submission.tar.gz * && cd ..
python3 generate_notebook.py
kaggle kernels push
