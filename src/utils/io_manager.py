import os
import datetime
import yaml

class IOManager:
    def __init__(self, base_dir, project_name):
        """
        Initialize the IOManager.
        
        Args:
            base_dir (str): The base directory for output (e.g., 'data/output').
            project_name (str): The name of the project.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.output_dir = os.path.join(base_dir, f"{project_name}_{timestamp}")
        
        # Create the output directory
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"Output directory created at: {self.output_dir}")

    def save_run_config(self, config_data):
        """
        Save the configuration snapshot.
        
        Args:
            config_data (dict): The configuration data to save.
        """
        file_path = os.path.join(self.output_dir, "config_snapshot.yaml")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(config_data, f, allow_unicode=True, default_flow_style=False)
            print(f"   [档案管理] 本次运行的完整参数已备份至 config_snapshot.yaml")
        except Exception as e:
            print(f"❌ [档案管理] 备份配置失败: {e}")

    def save_state(self, data, filename):
        """
        Save the intermediate state.
        
        Args:
            data (any): The data to save (placeholder for now).
            filename (str): The filename for the saved data (e.g., 'iter_001_data.txt').
        """
        # Defensive programming: Ensure directory still exists
        if not os.path.exists(self.output_dir):
            # Attempt to recreate it or raise error. 
            # For robustness, we recreate it here to avoid crashing long simulations.
            os.makedirs(self.output_dir, exist_ok=True)

        # In a real application, we would save 'data' to a file inside self.output_dir
        # For this MVP, we just print the path.
        save_path = os.path.join(self.output_dir, filename)
        
        # Mocking file write for demonstration (optional, or just print path)
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                 f.write(str(data))
        except Exception as e:
            print(f"❌ [IO操作] 保存数据失败: {e}")
            return

        print(f"   [IO操作] 数据已归档至：{save_path}")
