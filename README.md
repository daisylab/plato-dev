# plato

Dialogue enging for language education

## Installation

Prerequisites

```bash
sudo apt update
sudo apt install python3-dev python3-pip python3-venv
```



Clone repository

```bash
git clone https://github.com/daisylab/plato-dev.git
```

Change directory

```bash
cd plato
```

Make a virtual environment (if needed)

```bash
python3 -m venv ./venv
```

Activate the virtual environment (if needed)

```bash
source ./venv/bin/activate
```

Dependencies

```bash
pip install -r requirements.txt
```

"Editable" install


```bash
pip install -e .
```

## Usage

```python
from plato.qa import fr

context = r"""
I love food.
I see a cake.
I taste the cake.
It tastes sweet.
A cherry is on the cake.
It looks yummy.
I love food.
I see cookies.
Chocolate is on the cookies.
It looks sweet.
I taste the cookies.
They taste great.
"""

question = "What does the boy love?"

result = fr(question=question, context=context)

print(result['answer'])

```
