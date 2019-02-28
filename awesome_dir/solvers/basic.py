import logging

logger = logging.getLogger('solver/basic.py')

# [{'nr': 0, 'nTags': '3', 'direction': 'H', 'tags': ['cat', 'beach', 'sun']}]

def solve(photos):
    logger.info('Not actually solving anything')

    hor = filter(lambda x: x["direction"] == "H", photos)
    vert = filter(lambda x: x["direction"] == "V", photos)

    sorted_hor = sorted(hor, key=lambda x: x["nTags"])
    sorted_vert = sorted(vert, key=lambda x: x["nTags"])


    slides = []

    logger.debug('Found some slides...')

    return slides


def compareThem(photoA, photoB):
    sameTags = 0
    for photoAsTag in photoA["tags"]:
        for photoBsTag in photoB["tags"]:
            if photoAsTag == photoBsTag:
                sameTags = sameTags + 1
    return sameTags


def returnSmallestSum(sums):
    smallestSum = sums[0]
    for sum in sums:
        if smallestSum > sum:
            smallestSum = sum
    return smallestSum
