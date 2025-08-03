from .lib import load_config, get_staged_diff, Reviewer
import sys

def main():
    appconfig = load_config()
    diff_result = get_staged_diff(appconfig.repository_dirpath)
    if not diff_result:
        print("ステージされた変更がないので処理を終了します。")
        sys.exit(0)
    reviewer = Reviewer(appconfig.api_key)
    review_result = reviewer.review_diff(diff_result)
    print(review_result)
