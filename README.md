# Python Training

## Project installation with PyCharm

1. Clone the repository inside `PycharmProjects` directory:

    ```shell
    cd ~/PycharmProjects/
    git clone https://github.com/iuliachiriac/python-training-may2022.git
    ```

2. Open PyCharm, go to `File` -> `Open` and select the `python-training-may2022` directory.
3. In PyCharm, go to `Preferences/Settings` -> `Project:python-training-may2022` -> `Project Interpreter`
4. Click on the settings icon -> `Add` -> `+` icon.
5. Select `Virtualenv Environment` -> check `New environment` and make sure Python3 installation path is correctly selected under `Base interpreter` -> `Ok`.
6. After the virtual environment is created, go to `Terminal` tab. 
The virtual environment should be activated (you should see `(venv)` or `(python-training-may2022)` (depending on the `virtualenv` version you're using)
before the usual prompt).

7. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

8. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

## Project installation without PyCharm

1. Clone the repository:

    ```shell
    git clone https://github.com/iuliachiriac/python-training-may2022.git
    ```

1. Move to project directory:
    ```shell
    cd python-training-may2022
    ```

1. Create a virtual environment:

    ```shell
    virtualenv venv
    ```

1. Activate virtual environment:

    Linux/MacOS:
    ```shell
    source venv/bin/activate
    ```

    Windows:
    ```shell
    venv\Scripts\activate
    ```

1. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

### Contact
Iulia Chiriac <iulia.chiriac.a@gmail.com>

Feedback form: https://forms.gle/EDt9Gk6LYVBezApX7
