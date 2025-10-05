from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
APP_DIR = PROJECT_ROOT / "app"
UTILS_DIR = PROJECT_ROOT / "utils"
TEST_DIR = PROJECT_ROOT / "test"
ZXCVBN_PATH = os.path.join(PROJECT_ROOT, 'utils', 'zxcvbn-python')
WORD_LIST_PATH = os.path.join(PROJECT_ROOT, 'app', 'word_list.txt')
