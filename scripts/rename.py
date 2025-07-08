def add_space_to_emoji(dirnames: List[str], emoji_list: List[str]) -> List[str]:
    results = []
    for name in dirnames:
        new = name
        for e in emoji_list:
            # 前にスペースがなければ付ける
            new = re.sub(rf"(?<!\s){re.escape(e)}", r" \g<0>", new)
            # 後ろにスペースがなければ付ける
            new = re.sub(rf"{re.escape(e)}(?!\s)", r"\g<0> ", new)
        # 連続スペースを 1 つに、行頭尾のスペースを除去
        new = re.sub(r" +", " ", new).strip()
        results.append(new)
    return results


def make_display_text(dirnames: List[str]) -> List[str]:
    """ディレクトリ名のリストを表示用のテキストに変換する関数."""
    pass
