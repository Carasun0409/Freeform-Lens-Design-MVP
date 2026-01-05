import yaml
import os

def load_config(path):
    """
    Load configuration from a YAML file.
    
    Args:
        path (str): Path to the YAML configuration file.
        
    Returns:
        dict: Configuration dictionary.
        
    Raises:
        FileNotFoundError: If the config file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found at: {path}")
        
    with open(path, 'r', encoding='utf-8') as f:
        try:
            config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML configuration: {e}")
