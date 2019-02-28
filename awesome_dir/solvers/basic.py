import logging

logger = logging.getLogger('solver/basic.py')


def solve(photos):
    logger.info('Not actually solving anything')

    hor = filter(lambda x: x["direction"] == "H", photos)
    vert = filter(lambda x: x["direction"] == "V", photos)

    sorted_hor = sorted(hor, key=lambda x: x["nTags"])
    sorted_vert = sorted(vert, key=lambda x: x["nTags"])


    slides = []
    vertical_slides = []

    logger.debug('Found some slides...')

    return slides
