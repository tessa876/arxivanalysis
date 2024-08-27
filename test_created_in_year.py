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


def test_article_year_match() -> None:
    """Test created_in_year with an article that was created in the given year."""
    actual = arxiv_functions.created_in_year(EXAMPLE_ARXIV, "108", 2023)
    expected = True
    assert actual == expected


def test_article_year_not_match() -> None:
    """Test created_in_year with an article that was not created in the given year."""
    actual = arxiv_functions.created_in_year(EXAMPLE_ARXIV, "42", 2024)
    expected = False
    assert actual == expected


def test_article_year_empty() -> None:
    """Test created_in_year with an article that has no given year for its creation."""
    actual = arxiv_functions.created_in_year(EXAMPLE_ARXIV, "5990", 2023)
    expected = False
    assert actual == expected


def test_article_year_does_not_exist() -> None:
    """Test created_in_year with an article that does not exist."""
    actual = arxiv_functions.created_in_year(EXAMPLE_ARXIV, "9999", 2023)
    expected = False
    assert actual == expected


if __name__ == "__main__":
    pytest.main(["test_created_in_year.py"])
