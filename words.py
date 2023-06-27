#!/usr/bin/env python3


"""Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
"""


import sys
from urllib.request import urlopen


def fetch_words(url):
    """fetch a list of words from a URL.
     
        Args:
            url: the URL of a UTF-8 text document.
            
        Returns:
            A list of words containing the words from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items one per line.

        Args:
            items: an iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each words from a text document at a URL.

        Args:
            url: the URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])