import os
import datetime
import yaml
import json

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
        # The check is redundant if we assume standard behavior, but exist_ok=True is safe.
        # Removing explicit check as requested to optimize for high performance future scenarios.
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

    def save_state(self, data_package, filename):
        """
        Save the intermediate state as a JSON file.
        
        Args:
            data_package (dict): The complete data package (including metadata) to save.
            filename (str): The filename for the saved data (e.g., 'iter_001_data.json').
        """
        save_path = os.path.join(self.output_dir, filename)
        
        try:
            # Use json.dump for self-describing data format
            with open(save_path, 'w', encoding='utf-8') as f:
                 json.dump(data_package, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"❌ [IO操作] 保存数据失败: {e}")
            return

        print(f"   [IO操作] 数据已归档至：{save_path}")

    def save_report(self, report_data):
        """
        Save the final run report.
        
        Args:
            report_data (dict): Dictionary containing run statistics and results.
        """
        file_path = os.path.join(self.output_dir, "report.json")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=4, ensure_ascii=False)
            print(f"   [报告生成] 运行报告已保存至：{file_path}")
        except Exception as e:
            print(f"❌ [报告生成] 保存报告失败: {e}")
