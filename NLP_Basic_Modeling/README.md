- Bash commands one can use for troubleshooting various issues and setting up environment

```bash
make                  # builds NLP_env + installs everything
source NLP_env/bin/activate
# work...
deactivate
make clean            # remove caches only
make distclean        # remove entire venv too
```

```bash
source NLP_env/bin/activate # To activate environment  again
python -m spacy download en_core_web_sm  # to download seprately
```

Instead of this
```bash
python -m spacy download en_core_web_sm
do:
```
pip install \
https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
```

```bash
pip install --upgrade pip setuptools wheel
```

```bash
pip install ipywidgets notebook jupyterlab
```

or  classic Jupyter:

```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```


```bash
git rm -r --cached NLP_env
git commit -m "Stop tracking virtual environment"
git status --ignored
```

pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension --sys-prefix



- For a manual installation 
install:
	pip install -r requirements.txt
	python -m spacy download en_core_web_sm
    pip install Wikipedia-API
