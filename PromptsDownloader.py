import pandas as pd
n_examples = 10
df = pd.read_parquet("hf://datasets/walledai/AdvBench/data/train-00000-of-00001.parquet")
df = df.sample(frac=1).iloc[:n_examples]
harmful = df['prompt']
print(harmful)


