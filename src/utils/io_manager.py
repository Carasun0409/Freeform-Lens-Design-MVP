import os
import datetime

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

    def save_state(self, data, step):
        """
        Save the intermediate state.
        
        Args:
            data (any): The data to save (placeholder for now).
            step (int): The current simulation step.
        """
        # Defensive programming: Ensure directory still exists
        if not os.path.exists(self.output_dir):
            # Attempt to recreate it or raise error. 
            # For robustness, we recreate it here to avoid crashing long simulations.
            os.makedirs(self.output_dir, exist_ok=True)

        # In a real application, we would save 'data' to a file inside self.output_dir
        # For this MVP, we just print the path.
        save_path = os.path.join(self.output_dir, f"step_{step}.data")
        print(f"   [IO操作] 第 {step} 步数据已归档至：{save_path}")
