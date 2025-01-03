import os
import random
import re
import sys

DAMPING = 0.85  # PROBABILITY OF CONTINUING ON THE CURRENT PAGE INSTEAD OF LEAVING
SAMPLES = 10000  # NUMBER OF SURFER CLICKS


def crawl(directory) -> dict:  # ANALYZE HTML FILES AND CHECK THEIR LINKS TO OTHER PAGES
    # RETURNS A DICTIONARY WHERE EACH KEY IS A PAGE, AND THE VALUES ARE LISTS OF LINKS
    """
    PARSE A DIRECTORY OF HTML PAGES AND CHECK FOR LINKS TO OTHER PAGES.
    RETURN A DICTIONARY WHERE EACH KEY IS A PAGE, AND VALUES ARE A LIST OF ALL OTHER PAGES IN THE CORPUS THAT ARE LINKED TO BY THE PAGE.
    """
    pages = dict()

    # EXTRACT ALL LINKS FROM HTML FILES
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # ONLY INCLUDE LINKS TO OTHER PAGES IN THE CORPUS
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor) -> dict:  # CREATE A TRANSITION MODEL FOR PAGES
    # PARAMETERS: DICTIONARY FROM THE CRAWL FUNCTION, CURRENT PAGE, AND DAMPING PROBABILITY
    """
    RETURN A PROBABILITY DISTRIBUTION OVER WHICH PAGE TO VISIT NEXT, GIVEN A CURRENT PAGE.
    WITH PROBABILITY `damping_factor`, CHOOSE A LINK AT RANDOM LINKED TO BY `page`. WITH PROBABILITY `1 - damping_factor`, CHOOSE A LINK AT RANDOM CHOSEN FROM ALL PAGES IN THE CORPUS.
    """
    
    distribution = {}  # PROBABILITY DICTIONARY #OUTPUT OF THIS FUNCTION
    links = corpus[page]  # PAGES THAT THE CURRENT PAGE LINKS TO
    page_num = len(corpus)  # TOTAL NUMBER OF PAGES

    for i in corpus:  # FOR EACH PAGE IN THE CORPUS DICTIONARY
        distribution[i] = (1 - damping_factor) / page_num  # PROBABILITY OF GOING TO ANOTHER LINK INSTEAD OF LEAVING

    for i in links:  # FOR EACH LINK IN THE PAGE
        distribution[i] += damping_factor / len(links)  # PROBABILITY OF THE USER CHOOSING ANY LINK ON THE PAGE

    return distribution


def sample_pagerank(corpus: dict, damping_factor, n) -> dict:  # CALCULATE SAMPLING BY SURFING LINKS
    # PARAMETERS: DICTIONARY, DAMPING, AND NUMBER OF CLICKS
    """
    RETURN PAGERANK VALUES FOR EACH PAGE BY SAMPLING `n` PAGES ACCORDING TO TRANSITION MODEL, STARTING WITH A PAGE AT RANDOM.
    RETURN A DICTIONARY WHERE KEYS ARE PAGE NAMES, AND VALUES ARE THEIR ESTIMATED PAGERANK VALUE (A VALUE BETWEEN 0 AND 1). ALL PAGERANK VALUES SHOULD SUM TO 1.
    """

    # CHOOSE A RANDOM STARTING PAGE
    current_page = random.choice(list(corpus.keys()))  # PICK A RANDOM KEY FROM THE DICTIONARY
    # ANALYZE THE NUMBER OF VISITS TO EACH SITE
    quantity_visits = {}
    for page in corpus:
        quantity_visits[page] = 0

    for i in range(n):  # LOOP FOR n TIMES (SAMPLES)
        # INCREASE VISIT COUNT FOR THE CURRENT PAGE
        quantity_visits[current_page] += 1
        
        # CHECK IF PROBABILITY OF FOLLOWING A LINK IS GREATER THAN RANDOM CHOICE
        if random.random() < damping_factor:  # FOLLOW A LINK
            # TRANSITION MODEL DISTRIBUTION
            link_possibility = transition_model(corpus, current_page, damping_factor)

            # CHOOSE THE NEXT PAGE ACCORDING TO THE TRANSITION MODEL
            current_page = random.choices(
                list(link_possibility.keys()),  # CONVERT DICTIONARY TO LIST
                weights=list(link_possibility.values())  # DEFINE RELATIVE PROBABILITIES
            )[0]  # PICK THE PAGE WITH THE HIGHEST RELATIVE PROBABILITY
        else:
            # CHOOSE RANDOMLY IF NOT FOLLOWING A LINK
            current_page = random.choice(list(corpus.keys()))

    # CALCULATE PAGERANK VALUES (ALL VALUES SHOULD SUM TO 1)
    total_quantity = sum(quantity_visits.values())
    pageRankValues = {}    
    for page, quantity in quantity_visits.items():
        pageRankValues[page] = quantity / total_quantity

    return pageRankValues


def iterate_pagerank(corpus, damping_factor) -> dict:
    """
    RETURN PAGERANK VALUES FOR EACH PAGE BY ITERATIVELY UPDATING PAGERANK VALUES UNTIL CONVERGENCE.
    RETURN A DICTIONARY WHERE KEYS ARE PAGE NAMES, AND VALUES ARE THEIR ESTIMATED PAGERANK VALUE (A VALUE BETWEEN 0 AND 1). ALL PAGERANK VALUES SHOULD SUM TO 1.
    """

    dictionary = {}  # PAGE NAMES AND PERCENTAGES
    convergence = 0.001  # CONVERGENCE CRITERIA
    page_num = len(corpus)
    temp_dict = {}

    for page in corpus:  # INITIALIZE PROBABILITIES TO EQUAL VALUES (1/NUMBER OF PAGES)
        dictionary[page] = 1 / page_num

    while True:  # MARKOV ALGORITHM STARTS HERE
        temp_dict = {page: 0 for page in corpus}

        for page in corpus:
            temp_dict[page] += (1 - damping_factor) / page_num

            for links in corpus:
                if page in corpus[links]:
                    temp_dict[page] += damping_factor * (dictionary[links] / len(corpus[links]))

            if len(corpus[links]) == 0:
                if corpus[links] != set():
                    temp_dict += damping_factor * (dictionary[links] / page_num)

        if all(abs(temp_dict[page] - dictionary[page]) < convergence for page in dictionary):
            break
        
        # ROUND TO 4 DECIMAL PLACES
        dictionary = {page: round(temp_dict[page], 4) for page in temp_dict}

    return dictionary


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")  #

    corpus = crawl(sys.argv[1])
    print(corpus)

    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")    

    print(f"PageRank Results from Iteration")
    ranks = iterate_pagerank(corpus, DAMPING)
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")  