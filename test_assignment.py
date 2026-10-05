import pytest

from assignment import (
    write_shopping_list,
    read_names,
    append_entry,
    search_file,
    number_the_lines,
)


@pytest.mark.parametrize(
    "items, expected",
    [
        [["Bread", "Milk", "Eggs"], "1. Bread\n2. Milk\n3. Eggs\n"],
        [["Rice"], "1. Rice\n"],
        [[], ""],
        [["Tea", "Sugar", "Flour", "Salt"],
         "1. Tea\n2. Sugar\n3. Flour\n4. Salt\n"],
    ]
)
def test1(tmp_path, items, expected):
    path = tmp_path / "shopping.txt"
    write_shopping_list(items, path)
    assert path.read_text() == expected


def test1_overwrites(tmp_path):
    path = tmp_path / "shopping.txt"
    write_shopping_list(["Bread", "Milk"], path)
    write_shopping_list(["Rice"], path)
    assert path.read_text() == "1. Rice\n"


@pytest.mark.parametrize(
    "content, expected",
    [
        ["Bat\nSaraa\nAnu\n", ["Bat", "Saraa", "Anu"]],
        ["Bat\n\nSaraa\n\n\nAnu\n", ["Bat", "Saraa", "Anu"]],
        ["  Bat  \n   Saraa\n", ["Bat", "Saraa"]],
        ["Bat", ["Bat"]],
        ["", []],
        ["\n\n\n", []],
    ]
)
def test2(tmp_path, content, expected):
    path = tmp_path / "names.txt"
    path.write_text(content)
    assert read_names(path) == expected


@pytest.mark.parametrize(
    "content, text, expected_content, expected_count",
    [
        ["Mon\nTue\n", "Wed", "Mon\nTue\nWed\n", 3],
        ["Mon\n", "Tue", "Mon\nTue\n", 2],
        ["", "Mon", "Mon\n", 1],
    ]
)
def test3(tmp_path, content, text, expected_content, expected_count):
    path = tmp_path / "log.txt"
    path.write_text(content)
    result = append_entry(path, text)
    assert path.read_text() == expected_content
    assert result == expected_count


def test3_new_file(tmp_path):
    path = tmp_path / "brand_new.txt"
    assert append_entry(path, "first line") == 1
    assert path.read_text() == "first line\n"


def test3_twice(tmp_path):
    path = tmp_path / "log.txt"
    path.write_text("Mon\n")
    append_entry(path, "Tue")
    assert append_entry(path, "Wed") == 3
    assert path.read_text() == "Mon\nTue\nWed\n"



SAMPLE = "I like Python\nPython is fun\nGoodbye world\npython again\n"


@pytest.mark.parametrize(
    "word, expected",
    [
        ["Python", [1, 2, 4]],    
        ["python", [1, 2, 4]],
        ["fun", [2]],
        ["world", [3]],
        ["mongolia", []],
        ["o", [1, 2, 3, 4]],
    ]
)
def test4(tmp_path, word, expected):
    path = tmp_path / "text.txt"
    path.write_text(SAMPLE)
    assert search_file(path, word) == expected


def test4_empty_file(tmp_path):
    path = tmp_path / "text.txt"
    path.write_text("")
    assert search_file(path, "anything") == []

@pytest.mark.parametrize(
    "content, expected, expected_count",
    [
        ["apple\nbanana\ncherry\n", "1: apple\n2: banana\n3: cherry\n", 3],
        ["only one line\n", "1: only one line\n", 1],
        ["", "", 0],
    ]
)
def test5(tmp_path, content, expected, expected_count):
    source = tmp_path / "in.txt"
    destination = tmp_path / "out.txt"
    source.write_text(content)
    result = number_the_lines(source, destination)
    assert destination.read_text() == expected
    assert result == expected_count


def test5_does_not_change_source(tmp_path):
    source = tmp_path / "in.txt"
    destination = tmp_path / "out.txt"
    source.write_text("apple\nbanana\n")
    number_the_lines(source, destination)
    assert source.read_text() == "apple\nbanana\n"
