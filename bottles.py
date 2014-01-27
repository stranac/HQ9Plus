VERSE = (
'''{0} bottle{1} of beer on the wall,
{0} bottle{1} of beer.
{2}
{3} bottle{4} of beer on the wall.
'''
)

TAKE = 'Take one down and pass it around,'
BUY = 'Go to the store and buy some more,'

def verses():
    """
    Yield verses of "99 Bottles of Beer" one at a time.
    """
    for n in xrange(99, 2, -1):
        yield VERSE.format(n, _ending(n), TAKE, n-1, _ending(n-1))
    yield VERSE.format(1, '', TAKE, 'No more', 's')
    yield VERSE.format('No more', 's', BUY, 99, 's')


def _ending(n):
    return '' if n == 1 else 's'
