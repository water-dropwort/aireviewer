import os
import sys

if not __package__:
    package_source_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, package_source_path)

if __name__ == '__main__':
    print("DEVELOPMENT")
    from aireviewer.cli import main
    main()
