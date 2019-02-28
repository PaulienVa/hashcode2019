import logging

logger = logging.getLogger('solver/basic.py')


def solve(photos):
    logger.info('Not actually solving anything')

    slides = []
    vertical_slides = []

    for photo in photos:
        if photo["direction"] == 'H':
            slides.append([photo["nr"]])
        elif photo["direction"] == 'V':
            vertical_slides.append(photo["nr"])
    slides.append(vertical_slides)


    logger.debug('Found some slides...')

    return slides
