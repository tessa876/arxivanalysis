import copy  # needed in examples of functions that modify input dict
from typing import TextIO

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


################################################################################
# Sample data for use in docstring examples
################################################################################
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

EXAMPLE_BY_AUTHOR = {
    ("Campbell", "Jen"): ["108"],
    ("Grossman", "Tovi"): ["03221"],
    ("Kim", "Joonho"): ["6795"],
    ("Sharmin", "Sadia"): ["0001"],
    ("Smith", "Jacqueline E."): ["0001", "108"],
    ("Yanez", "Fernando"): ["5090"],
    ("Zavaleta-Bernuy", "Angela"): ["108", "5090"],
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
author_dict = {
    ('Campbell', 'Jen'): ['108'],
    ('Grossman', 'Tovi'): ['03221'],
    ('Kim', 'Joonho'): ['6795'],
    ('Sharmin', 'Sadia'): ['0001'],
    ('Smith', 'Jacqueline E.'): ['0001', '108'],
    ('Yanez', 'Fernando'): ['5090'],
    ('Zavaleta-Bernuy', 'Angela'): ['108', '5090']
}

article = {
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
}


def clean_word(word: str) -> str:
    """Return word with all non-alphabetic characters removed and converted to
    lowercase.

    Precondition: word contains no whitespace

    >>> clean_word('Hello!!!')
    'hello'
    >>> clean_word('12cat.dog?')
    'catdog'
    >>> clean_word("DON'T")
    'dont'
    """
    new_word = ""
    for ch in word:
        if ch.isalpha():
            new_word = new_word + ch.lower()
    return new_word


################################################################################
# Task 1 - Working with ArxivType
################################################################################
def created_in_year(data: ArxivType, ids: str, year: int) -> bool:
    """Return True if and only if and article with the provide id occurs in the data and
      was published in the given year.

      >>> created_in_year(EXAMPLE_ARXIV, "6795", 2024)
      True
      >>> created_in_year(EXAMPLE_ARXIV, "42", 2024)
      False
      """

    if ids in data:
        created_date = data[ids].get(CREATED, '')
        if created_date:
            created_year = int(created_date.split("-")[0])
            return created_year == year
    return False


def clean_authors(authors: list) -> str:
    """Clean and join author names from a list of tuples.
    Return the names in a string format.
    """
    cleaned_names = []
    for author in authors:
        last_name = author[1]
        first_name = author[0]
        cleaned_last = clean_word(last_name)
        cleaned_first = clean_word(first_name)
        cleaned_names.append(cleaned_last + cleaned_first)
    return ' '.join(cleaned_names)


def contains_keyword(data: ArxivType, keyword: str) -> list[str]:
    """Return the list of IDs of the articles containing the given keyword.
    The key word must be in the title, author name, and/or abstract.
    List will be sorted in lexicographic order.

    >>> contains_keyword(EXAMPLE_ARXIV, "Smith")
    ['0001', '108']
    >>> contains_keyword(EXAMPLE_ARXIV, "Cats")
    ['0001']
    """
    matching_ids = []
    cleaned_keyword = clean_word(keyword)

    for ids in data:
        clean_title = clean_word(data[ids].get(TITLE, '')) + ''
        clean_abstract = clean_word(data[ids].get(ABSTRACT, '')) + ''
        clean_author = clean_authors(data[ids].get(AUTHORS, ''))

        if cleaned_keyword in clean_title:
            matching_ids.append(ids)
        elif cleaned_keyword in clean_abstract:
            matching_ids.append(ids)
        elif cleaned_keyword in clean_author:
            matching_ids.append(ids)
    return sorted(matching_ids)


def average_author_count(data: ArxivType) -> float:
    """Return the average author count per article in the arxiv metadata.
    If there are no articles in this data, the function returns 0.0

    >>> average_author_count(EXAMPLE_ARXIV)
    1.5
    >>> average_author_count(NEW_ARXIV)
    2.0
    """

    total = 0
    num_articles = 0
    for ids in data:
        if data[ids].get(ABSTRACT, '') != '':
            num_articles += 1
            if data[ids].get(AUTHORS, '') != '':
                total += len(data[ids].get(AUTHORS, ''))
        else:
            return 0.0
    if num_articles == 0:
        return 0.0
    return total / num_articles


################################################################################
# Task 2 - Reading in the arxiv metadata
################################################################################
def read_arxiv_file(file: TextIO) -> ArxivType:
    """Return a ArxivType dictionary containing the arxiv metadata in f.

    Note we do not include example calls for functions that take open files.
    """
    arxiv_data = {}
    current_id = None
    current_article = {}
    abstract_lines = []

    for line in file:
        line = line.strip()
        if line == "END":
            if current_id:
                current_article[ABSTRACT] = clean_abstract(abstract_lines)
                arxiv_data[current_id] = current_article
                current_id = None
                current_article = {}
                abstract_lines = []
        elif not current_id:
            current_id = line
            current_article = {ID: current_id}
        elif TITLE not in current_article:
            current_article[TITLE] = line
        elif CREATED not in current_article and line:
            current_article[CREATED] = line
        elif MODIFIED not in current_article and line:
            current_article[MODIFIED] = line
        elif AUTHORS not in current_article and line:
            current_article[AUTHORS] = get_authors(line)
        elif ABSTRACT in current_article:
            abstract_lines.append(line)
        else:
            if CREATED not in current_article:
                current_article[CREATED] = ""
            if MODIFIED not in current_article:
                current_article[MODIFIED] = ""
            if AUTHORS not in current_article:
                current_article[AUTHORS] = []
            if ABSTRACT not in current_article:
                current_article[ABSTRACT] = ""

    return arxiv_data


def get_authors(authors_str: str) -> list[tuple]:
    """Edit the authors from a comma-separated string into a list of tuples.

    >>> get_authors("Smith, Jacqueline E")
    [('Smith', 'Jacqueline E')]
    >>> get_authors("")
    []
    """
    new_authors = []
    if authors_str:
        lst_authors = authors_str.split(',')
        for i in range(0, len(lst_authors), 2):
            last_name = lst_authors[i].strip()
            if i + 1 < len(lst_authors):
                first_name = lst_authors[i + 1].strip()
            else:
                first_name = ''
            new_authors.append((last_name, first_name))
    return new_authors


def clean_abstract(lines: list) -> str:
    """
    Return a strings containing the abstract of the given lines that have been cleaned
    and join together is they were on separate lines.
    """
    stripped_lines = [line.strip() for line in lines]

    abstract = "\n".join(stripped_lines)

    return abstract.strip()


################################################################################
# Task 3 - Working with Authors and Coauthors
################################################################################
def make_author_to_articles(id_to_article: ArxivType) -> dict[NameType, list[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True
    >>> make_author_to_articles({})
    {}
    """

    author_to_articles = {}

    for article_id, article_info in id_to_article.items():
        authors = article_info.get(AUTHORS, [])
        for last_name, first_name in authors:
            author = (last_name, first_name)
            if author not in author_to_articles:
                author_to_articles[author] = []
            author_to_articles[author].append(article_id)

    for articles in author_to_articles.values():
        articles.sort()

    return author_to_articles


def get_coauthors(data: ArxivType, name: NameType) -> list[NameType]:
    """
    Return a sorted list of manes from the coauthors of the given name from the data.

    >>> get_coauthors(EXAMPLE_ARXIV, ("Smith", "Jacqueline E."))
    [('Campbell', 'Jen'), ('Sharmin', 'Sadia'), ('Zavaleta-Bernuy', 'Angela')]

    >>> get_coauthors(EXAMPLE_ARXIV, [])
    []
    """
    coauthors = []

    for article in data.values():
        authors = article.get(AUTHORS, [])
        if name in authors:
            for author in authors:
                if author != name:
                    coauthors.append(author)

    return sorted(coauthors)


def get_most_published_authors(data: ArxivType) -> list[NameType]:
    """
    Return a sorted list of author names from the most published authors.
    >>> get_most_published_authors(EXAMPLE_ARXIV)
    [('Smith', 'Jacqueline E.'), ('Zavaleta-Bernuy', 'Angela')]

    >>> get_most_published_authors(NEW_ARXIV)
    [('John', 'Alice')]
    """
    new_dict = make_author_to_articles(data)
    max_publications = 0
    for articles in new_dict.values():
        num_articles = len(articles)
        if num_articles > max_publications:
            max_publications = num_articles

    most_published_authors = []
    for author, articles in new_dict.items():
        if len(articles) == max_publications:
            most_published_authors.append(author)

    return sorted(most_published_authors)


def suggest_collaborators(data: ArxivType, name: NameType) -> list[NameType]:

    """ Return a list of suggested collaborators for the given author from the data.

    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Yanez', 'Fernando'))
    [('Campbell', 'Jen'), ('Smith', 'Jacqueline E.')]

    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Grossman', 'Tovi'))
    []
    """
    collaborators = get_coauthors(data, name)
    potential_collaborators = []
    for author in collaborators:
        co_of_co = get_coauthors(data, author)
        potential_collaborators.extend(co_of_co)
    if name in potential_collaborators:
        potential_collaborators.remove(name)
    filtered_collaborators = []
    for collaborator in potential_collaborators:
        if collaborator != name and collaborator not in collaborators:
            filtered_collaborators.append(collaborator)
    return sorted(filtered_collaborators)


################################################################################
# Task 4 - Prolific Authors
################################################################################


def has_prolific_authors(author_to_articles: dict[NameType, list[str]],
                         articles: ArticleType, min_pubs: int) -> bool:
    """ Return True if the given article has a prolific author, False otherwise.
    article =
    >>> has_prolific_authors(author_dict, article, 2)
    True
    >>> has_prolific_authors(author_dict, article, 3)
    False
    """
    prolific_authors = []

    lst_authors = articles.get(AUTHORS, [])
    for author, art in author_to_articles.items():
        if len(art) >= min_pubs:
            prolific_authors.append(author)
    for i in lst_authors:
        if i in prolific_authors:
            return True
    return False



def keep_prolific_authors(id_to_article: ArxivType, min_publications: int) -> None:
    """Update id_to_article so that it contains only articles published by
    authors with min_publications or more articles published. As long
    as at least one of the authors has min_publications, the article
    is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    """
    prolific = []
    kept_articles = []

    author_to_articles = make_author_to_articles(id_to_article)
    for author, articles in author_to_articles.items():
        if len(articles) >= min_publications:
            prolific.append(author)
    for article_id, article in id_to_article.items():
        for author in article[AUTHORS]:
            if author in prolific:
                kept_articles.append(article_id)
                break
    for article_id in list(id_to_article.keys()):
        if article_id not in kept_articles:
            del id_to_article[article_id]


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    
    example_data = open('example_data.txt')
    example_arxiv = read_arxiv_file(example_data)
    example_data.close()
    if example_arxiv == EXAMPLE_ARXIV:
        print('The result from your read_arxiv_file matches EXAMPLE_ARXIV!')
        print('This is a good sign, but do more of your own testing!')
    else:
        print('Not quite! You got')
        print(example_arxiv)
        print()
        print('If you are getting this message, then the dictionary produced')
        print('by your read_arxiv_file function does not match the provided')
        print('EXAMPLE_ARXIV. Scroll up to see the dictionary your function')
        print('produced. You should write additional testing code to help')
        print('figure out why it does not match. You can also try setting a')
        print('breakpoint on the first line of read_arxiv_file and running')
        print('the debugger.')

    
    data = open('data.txt')
    arxiv = read_arxiv_file(data)
    data.close()
    
    author_to_articles = make_author_to_articles(arxiv)
    most_published = get_most_published_authors(arxiv)
    print(most_published)
    print(get_coauthors(arxiv, ('Varanasi', 'Mahesh K.')))
    print(get_coauthors(arxiv, ('Chablat', 'Damien')))
