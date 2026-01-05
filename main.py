import argparse
import os
import sys

# Ensure src is in python path so imports work if running from root
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.utils.config_loader import load_config
from src.utils.io_manager import IOManager
from src.core.solver import LensDesignSolver

def main():
    try:
        # 1. Parse arguments
        parser = argparse.ArgumentParser(description="Freeform Optical Design MVP")
        parser.add_argument(
            '--config', 
            type=str, 
            default='config/default.yaml',
            help='Path to the configuration YAML file'
        )
        args = parser.parse_args()

        print(f"Loading configuration from: {args.config}")

        # 2. Load configuration
        config = load_config(args.config)

        # Extract project info
        project_name = config.get('project_name', 'DefaultProject')
        
        # 3. Instantiate IOManager
        # Output to data/output relative to project root
        base_output_dir = os.path.join(os.path.dirname(__file__), 'data', 'output')
        io_manager = IOManager(base_output_dir, project_name)

        # 4. Instantiate LensDesignSolver and run
        solver = LensDesignSolver(config, io_manager)
        solver.run()

    except ValueError as e:
        print(f"❌ 程序因配置错误终止：{e}")
    except Exception as e:
        print(f"❌ 程序发生未预期的错误：{e}")
        # Optional: print traceback for unexpected errors if needed, but keeping it clean as requested.
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
