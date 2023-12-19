# **Criando um Ambiente Virtual**


**Instalando o Conda**

>1. Antes de começar, certifique-se de ter o Conda instalado no seu sistema. Você pode baixar e instalar o Anaconda ou o Miniconda, que é uma versão mínima do Conda.
>
>2. Abra o terminal (Linux/Mac) ou o prompt de comando (Windows). Certifique-se de estar conectado à internet.
>
>3. Para criar um ambiente virtual, use o seguinte comando: `conda create --name meu_ambiente python=3.10` Substitua meu_ambiente pelo nome desejado para o seu ambiente e python=3.10 pela versão do Python que você deseja usar.

**Ativando o Ambiente Virtual**

>Para ativar o ambiente virtual, utilize o seguinte comando:
>
>**No Linux/Mac:** `conda activate meu_ambiente`
>
>**No Windows:** `conda activate meu_ambiente`

**Instalando Pacotes**

>Com o ambiente virtual ativo, você pode instalar pacotes usando o comando conda install. Por exemplo, para instalar o pacote numpy, use:`conda install numpy` ou `pip install numpy`
>
>**Pacotes instalados**
>
>`bzip2`              
>
>`ca-certificates`  
>
>`libffi`
>
>`openssl`
>
>`pip`
>
>`python`
>
>`setuptools`
>
>`sqlite`
>
>`tk`
>
>`tzdata`
>
>`vc`
>
>`vs2015_runtime`
>
>`wheel`
>
>`xz`
>
>`zlib`

**Desativando o Ambiente Virtual**

>Quando terminar de trabalhar no ambiente virtual, você pode desativá-lo com o comando:`conda deactivate`




**Ativando o ambiente novamente**

>1. abrir prompt anaconda
>2. `conda activate (nome do ambiente) `
>3. abrir jupyter: `jupyter-notebook`

