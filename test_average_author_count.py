"""CSC108: Fall 2023 -- Assignment 3: arxiv.org

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Anya Tafliovich, Michelle Craig, Tom Fairgrieve, Sadia
Sharmin, and Jacqueline Smith.
"""

import pytest
import arxiv_functions
from constants import (
    ID,
    TITLE,
    CREATED,
    MODIFIED,
    AUTHORS,
    ABSTRACT,
    END,
    NameType,
    ArticleValueType,
    ArticleType,
    ArxivType,
)


# You can use this sample dictionary in your tests, if you choose
# You can also create your own sample dictionaries
EXAMPLE_ARXIV = {
    "5090": {
        ID: "5090",
        TITLE: "Increasing Students' Engagement to Reminder Emails",
        CREATED: "",
        MODIFIED: "2022-08-02",
        AUTHORS: [("Yanez", "Fernando"), ("Zavaleta-Bernuy", "Angela")],
        ABSTRACT: "Our metric of interest is open email rates.",
    },
    "03221": {
        ID: "03221",
        TITLE: "Stargazer: An Interactive Camera Robot for How-To Videos",
        CREATED: "2023-03-01",
        MODIFIED: "2023-03-06",
        AUTHORS: [("Grossman", "Tovi")],
        ABSTRACT: (
            "We present Stargazer, a novel approach for assisting "
            + "with tutorial content creation."
        ),
    },
    "0001": {
        ID: "0001",
        TITLE: "Cats and Dogs Can Co-Exist",
        CREATED: "2023-08-20",
        MODIFIED: "2023-10-02",
        AUTHORS: [("Smith", "Jacqueline E."), ("Sharmin", "Sadia")],
        ABSTRACT: "We show a formal proof that cats and dogs\n"
        + "can peacefully co-exist!",
    },
    "108": {
        ID: "108",
        TITLE: "CSC108 is the Best Course Ever",
        CREATED: "2023-09-01",
        MODIFIED: "",
        AUTHORS: [
            ("Smith", "Jacqueline E."),
            ("Zavaleta-Bernuy", "Angela"),
            ("Campbell", "Jen"),
        ],
        ABSTRACT: "We present clear evidence that Introduction to\n"
        + "Computer Programming is the best course",
    },
    "6795": {
        ID: "6795",
        TITLE: "Squidgets: Sketch-based Widget Design and Direct Manipulation "
        + "of 3D Scene",
        CREATED: "2024-02-09",
        MODIFIED: "",
        AUTHORS: [("Kim", "Joonho")],
        ABSTRACT: "Squidgets or 'sketch-widgets' is a novel stroke-based UI "
        + "framework for direct\nscene manipulation. Squidgets is motivated "
        + "by the observation that sketch\nstrokes comprising visual "
        + "abstractions of scene elements implicitly provide\nnatural handles "
        + "for the direct manipulation of scene parameters.",
    },
    "42": {
        ID: "42",
        TITLE: "",
        CREATED: "2023-05-04",
        MODIFIED: "2023-05-05",
        AUTHORS: [],
        ABSTRACT: "This is a strange article with no title\n"
        + "and no authors.\n\nIt also has a blank line in its abstract!",
    },
}
NEW_ARXIV = {
    "5678": {
        ID: "5678",
        TITLE: "Bunny Found in Backyard",
        CREATED: "",
        MODIFIED: "2022-08-02",
        AUTHORS: [("John", "Alice"), ("Spring", "Maya")],
        ABSTRACT: "How to deal with wild bunnys in your backyard.",
    },
    "2021": {
        ID: "2021",
        TITLE: "What Does Your Astrology Sign Mean?",
        CREATED: "2023-03-01",
        MODIFIED: "2023-03-06",
        AUTHORS: [("John", "Alice")],
        ABSTRACT: (
                "Based on the day you were born in the year "
                + "we can tell you all about your personality!"
        ),
    },
    "0001": {
        ID: "0001",
        TITLE: "Cats and Dogs Can Co-Exist",
        CREATED: "2023-08-20",
        MODIFIED: "2023-10-02",
        AUTHORS: [("Smith", "Jacqueline E."), ("Sharmin", "Sadia")],
        ABSTRACT: "We show a formal proof that cats and dogs\n"
                  + "can peacefully co-exist!",
    },
    "108": {
        ID: "108",
        TITLE: "CSC108 is the Best Course Ever",
        CREATED: "2023-09-01",
        MODIFIED: "",
        AUTHORS: [
            ("Spring", "Maya"),
            ("Zavaleta-Bernuy", "Angela"),
            ("Campbell", "Jen"),
            ("John", "Alice")
        ],
        ABSTRACT: "We present clear evidence that Introduction to\n"
                  + "Computer Programming is the best course",
    },
    "6795": {
        ID: "6795",
        TITLE: "Squidgets: Sketch-based Widget Design and Direct Manipulation "
               + "of 3D Scene",
        CREATED: "2024-02-09",
        MODIFIED: "",
        AUTHORS: [("John", "Alice")],
        ABSTRACT: "Squidgets or 'sketch-widgets' is a novel stroke-based UI "
                  + "framework for direct\nscene manipulation. Squidgets is motivated "
                  + "by the observation that sketch\nstrokes comprising visual "
                  + "abstractions of scene elements implicitly provide\nnatural handles "
                  + "for the direct manipulation of scene parameters.",
    },
}


def test_average_author_count() -> None:
    """Test the average article count, correct."""
    actual = arxiv_functions.average_author_count(EXAMPLE_ARXIV)
    expected = 1.5
    assert actual == expected


def test_average_author_count_float() -> None:
    """Test the average article count making sure it is a float."""
    actual = arxiv_functions.average_author_count(NEW_ARXIV)
    expected = 2.0
    assert actual == expected


def test_average_author_count_no_articles() -> None:
    """Test the average article count on an article that does not exist."""
    empty = {}
    actual = arxiv_functions.average_author_count(empty)
    expected = 0.0
    assert actual == expected


if __name__ == "__main__":
    pytest.main(["test_average_author_count.py"])
