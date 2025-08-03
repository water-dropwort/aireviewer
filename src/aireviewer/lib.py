from dataclasses import dataclass
from argparse import ArgumentParser
from google import genai
from git import Repo
import os


@dataclass
class AppConfig:
    api_key: str
    repository_dirpath: str


def load_config() -> AppConfig:
    parser = ArgumentParser(prog="DiffReviewer")
    parser.add_argument("dirpath")
    args = parser.parse_args()
    repository_dirpath = args.dirpath
    if not os.path.isdir(repository_dirpath):
        raise FileNotFoundError(f"ディレクトリが存在しません: {repository_dirpath}")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("環境変数GEMINI_API_KEYが設定されていません")

    return AppConfig(api_key, repository_dirpath)


PROMPT_TEMPLATE="""# 指示
次の git diff の結果を見て、変更点をレビューしてください。
# Diffの内容
```
{}
```
# レビュー結果のフォーマット
以下のフォーマットに従って返答してください。
## 変更点概要
ここには変更点の概要を簡単に説明してください。
## レビューコメント
ここにはレビューコメントを記載してください。
## 提案
ここには開発者が取るべき次のアクションの提案をしてください。"""


def get_staged_diff(repository_dirpath: str) -> str:
    repo = Repo(repository_dirpath)
    diff_result = repo.git.diff("--cached", "HEAD")
    return diff_result


class Reviewer():
    def __init__(self, api_key):
        self.api_key = api_key


    def review_diff(self, diff_result: str) -> str:
        client = genai.Client(api_key=self.api_key)
        prompt = PROMPT_TEMPLATE.format(diff_result)
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        review_result = response.text
        return review_result

