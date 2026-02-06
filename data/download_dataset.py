import os, json
from argparse import ArgumentParser
from datasets import load_dataset

def download_and_save_dataset(dataset_name, subset, split, save_path):
    dataset = load_dataset(dataset_name, subset, split=split, trust_remote_code=True)
    
    data_path = os.path.join(save_path, f"{split}.jsonl")
    with open(data_path, 'w') as jsonl_file:
        for record in dataset:
            jsonl_file.write(json.dumps(record) + '\n')
    
    print(f"{[split]} {dataset_name}-{subset} dataset downloaded and saved to {data_path}.")



if __name__ == '__main__':
    dataset_name = 'sagnikrayc/mctest'
    subsets = ['mc160', 'mc500']
    splits = ['train', 'validation', 'test']
    
    for subset in subsets:
        save_path = os.path.join(subset)
        os.makedirs(save_path, exist_ok=True)
        for split in splits:            
            download_and_save_dataset(dataset_name, subset, split, save_path)