aidiagnoctic
==============================
Test ex on aidiagnostic

## Описание задания

Нужно написать бейзлайн для обучения сегментационной нейросети для обнаружения плеврального выпота. 

Обучить можно любую сегментационную нейросеть, можно использовать 2D или 3D архитектуру.

Код должен быть разделен следующим образом:

- файл с архитектурой модели
- файл с препроцессингом данных для обучения
- файл с датасетом
- файл с функцией подсчета [DICE Coef](https://radiopaedia.org/articles/dice-similarity-coefficient#:~:text=The%20Dice%20similarity%20coefficient%2C%20also,between%20two%20sets%20of%20data.)
- основной файл с самим циклом обучения. В коде обучения во время валидации автоматически должна  выбираться лучшая эпоха и сохраняться веса модели в папку `output`. Также после цикла обучения в эту папку должна сохраняться картинка с изменениями коэффициента DICE с каждой эпохой. (по оси Y - коэффициент DICE, по оси X - номер эпохи). Вместо выходной картинки с графиком можно использовать любые трекеры при желании (tensorboard etc.)




A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
